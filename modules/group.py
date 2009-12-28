#!/bin/dev python
# coding=utf8
from log4py import *
from hanzi import *
import memory
import codecs
log = log4py('group')
class Group(memory.Memory):
    def __init__(self,groupsize = 10, pagesize = 10, parent = None):
        Memory.__init__(self)
        self.curpoint = 0
        self.items = []
        self.parent = parent
        self.groupsize = groupsize
        self.pagesize = pagesize
        self._countpage = 0
        #self._countpage = 0
    
    def getlastitem(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]
    
    def isfill(self):
        lens = len(self.items)
        if lens < groupsize:
            return False
        else:
            if len(self.getlastitem()) == self.pagesize:
                return True
            return False
            
        
    def getemptyitem(self):
        item = self.getlastitem()
        if item == None or len(item.items) == self.pagesize :
            if len(self.items) == self.groupsize:
                return None
            item = Page()
            self.items.append(item)
        
        return item
            
    def additem(self,item):
        
        if self._countpage <= self.groupsize:
            self.items.append(item)
            self._countpage += 1
            #if self.parent != None:
            return 1    
        else:
            return -1 

class Page(Group):
    #def additem(self,item):
    #    self.additem(item)
    pass    
class Groups():
    def __init__(self,groupsize=10,pagesize=10):
        ''' groupsize 组内包含多少item
        groupsize 页内包含多少对象
        '''
        self.groupsize = groupsize
        self.pagesize = pagesize
        self.curgroup = 0
        self.curitem = 0
        self.maxgroups = 0
        self.groups=[] #
        self._countgroup = 0
        self._countitem = 0
        self._group = None
        self._item = None
        
    def getlastgroup(self):
        if len(self.groups) == 0:
            return None
        return self.groups[len(self.groups)-1]
    
    def getemptygroup(self):
        group = self.getlastgroup()
        if group == None:
            group = Group()
            self.groups.append(group)
        # 如果组内页数等于最大值，判断最后一个页是否填满
        # 如果填满，新建group，如果没满，继续填    
        if len(group.items) == self.groupsize:
            if group.isfull():
                group = Group()
                self.groups.append(group)
        
        return group
            
            
    def additem(self,item):
        ''' 如果group为空，创建group,加入groups;
        如果group 满了，则将group 置空
        如果item 为空，创建item，并加入group
        如果item 满了，则将item置空
        item 是基本单位
        '''
        group =  self.getemptygroup()
        page = group.getemptyitem()
        
        page.additem(item)
        log.debug('countitem = ',self._countitem,'countitem = ',self._countitem)
        
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
            char.setfreq(int(splitline[2]))
            char.setpinyin(splitline[4])
            char.english=splitline[5]
            
            self.additem(char)
        
        f.close()        
        return True
    
    def getgroup(self,groupid):
        if len(self.groups) == 0:
            return None
        return self.groups[groupid]
    
    def getgroups(self,groupidstart,groupidend):
        return self.groups[groupidstart:groupidend]
    
    def getitem(self,groupid,itemid):
        if itemid < 0 or groupid < 0 :
            log.warn('groupid = ',groupid,'itemid = ', itemid)
            return None
        group = self.getgroup(groupid)
        return group.items[itemid]
        
            
#todo 需要将要背诵的对象分组，用next方法来显示，初始化分组    

#unit test
if __name__ == '__main__':
    gs = Groups(11,4)
    gs.open('../data/freq_part.txt')
    group = gs.getgroup(1)
    for item in group.items:
        for char in item.items:
            print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin ,char.english
             
    item1 = gs.getitem(1,5)
    for char in item1.items:
        print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin ,char.english
             