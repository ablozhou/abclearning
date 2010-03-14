#!/bin/dev python
# coding=utf8
from log4py import *
from char import *
import exceptions
import memory
import codecs
log = log4py.log4py('[group]')
class OverflowException(Exception):
    pass

class Iter():
    def __init__(self,maxsize):
        self.items = []
        self.maxsize = maxsize

    def __iter__(self):
        self._cur = 0
        return self

    def next(self):
        if  self._cur < len(self.items):
            it =  self.items[self._cur]
            self._cur += 1
            return it
        else:
            raise StopIteration

    def additem(self,item):

        if self.len() <= self.maxsize:
            self.items.append(item)
        else:
            log.error('len is overflow:',self.len())
            raise OverflowException


    def len(self):
        return len(self.items)

    def getlastitem(self):
        if self.len() == 0:
            return None
        return self.items[len(self.items)-1]


class Group(memory.Memory,Iter):
    def __init__(self,maxsize, pagesize, parent = None):
        Iter.__init__(self,maxsize)
        Memory.__init__(self)
        self.curpoint = 0
        self.parent = parent
        self.pagesize = pagesize
        self._countpage = 0


    def isfull(self):
        '''check group is full or not'''
        #f=log.dbgfc('isfull')
        lens = self.len()
        log.debug('check group is full or not, group len = %s'%lens)
        if lens < self.maxsize:
            return False

        else:
            log.debug('group lens == groupsize')
            item = self.getlastitem()
            if item == None: #should not be none
                log.warn('item should not be none?')
                return False

            if item.isfull():
                return True
            else:
                return False


    def getemptypage(self):
        #f=log.dbgfc('getemptypage')
        if self.isfull():
            log.warn('getemptypage, group is full,return None')
            return None

        page = self.getlastitem()
        if page == None or page.isfull():
            log.debug('page is None or full, new a page')
            page = Page(self.pagesize,self)
            self.additem(page)

        return page



class Page(Iter):
    def __init__(self,maxsize,parent):
        Iter.__init__(self,maxsize)
        self.parent = parent

    def isfull(self):
        if self.len() == self.maxsize:
            return True
        else:
            return False

    def display(self):
        for item in self:
            item.display()

    def getstr(self):
        str = ''
        for item in self:
            str += item.display()
        return str

class Groups(Iter):
    def __init__(self,groupsize=10,pagesize=10):

        Iter.__init__(self,99999)
        ''' groupsize 组内包含多少item
        pagesize 页内包含多少对象
        '''
        self.groupsize = groupsize
        self.pagesize = pagesize
        self.curgroup = 0
        self.curpage = 0
        self.dict = CharDict()


    def getlastgroup(self):
        return self.getlastitem()

    def getemptygroup(self):
        #f=log.dbgfc('getemptygroup')
        group = self.getlastgroup()
        if group == None or group.isfull():
            log.debug('group is none or full,Init a group')
            group = Group(self.groupsize,self.pagesize,self)
            self.additem(group)

        return group


    def addunit(self,unit):
        ''' unit是基本单位。如果group为空，创建group,加入groups;
        如果page为空，创建page，并加入group
        '''
        group =  self.getemptygroup()
        page = group.getemptypage()

        try:
            page.additem(unit)
            self.dict.addchar(unit)
        except OverflowException:
            log.error('page error over flow')

    def getunit(self,unit):
        try:
            a = self.dict[unit]
            return a
        except KeyError:
            return unit

    def open(self,file):
        splitline = []
        f=codecs.open(file, 'r','utf8')
        if not f:
            log4py.debug('error ,cannot open file %s' % file)
            return False

        lines = f.read().split('\n')
        for line in lines:

            splitline = line.split('\t',5)
            #log.debug(splitline)
            char = Char(splitline[1])
            char.freq = int(splitline[2])
            char.phonetic = splitline[4]
            char.english = splitline[5]
            #char.printhz()
            try:
                self.addunit(char)
            except OverflowException:
                log.error('overflow exception')

        f.close()
        return True

    def getgroup(self,groupid):
        log.debug('groupid=',groupid)
        if len(self.groups) == 0:
            return None
        return self.groups[groupid]

    def getnextgroup(self):
        log.debug('current group=',self.curgroup)

    def getgroups(self,groupidstart,groupidend):
        return self.groups[groupidstart:groupidend]

    def getitem(self,groupid,itemid):
        if itemid < 0 or groupid < 0 :
            log.warn('groupid = ',groupid,'itemid = ', itemid)
            return None
        group = self.getgroup(groupid)
        return group.items[itemid]

    def walk(self):
        i = 0

        for group in self:
            i = i+1
            log.debug('group',i)
            j=0
            for page in group:
                j = j+1
                log.debug('page ',j)
                for char in page:
                    char.display()
                    #print codecs.encode(char.char,'utf8')
                    #print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin ,char.english

#todo 需要将要背诵的对象分组，用next方法来显示，初始化分组

#unit test
if __name__ == '__main__':
    gs = Groups(2,2)
    gs.open('../data/freq_part.txt')
    '''group = gs.getgroup(1)
    for item in group.items:
        for char in item.items:
            print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin ,char.english

    item1 = gs.getitem(1,5)
    for char in item1.items:
        print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin ,char.english
       '''
    gs.walk()