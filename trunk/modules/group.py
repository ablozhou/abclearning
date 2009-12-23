#!/bin/dev python
# coding=utf8
from log4py import *
from hanzi import *
import memory
import codecs
log = log4py('group')
class Group(memory.Memory):
    def __init__(self,pagesize = 10, parent = None):
        Memory.__init__(self)
        self.curpoint = 0
        self.sources = []
        self.parent = parent
        self.pagesize = pagesize
        self._count = 0
        
    def addsource(self,source):
        
        if self._count < self.pagesize:
            self.sources.append(source)
            self._count += 1
            #if self.parent != None:
            return 1    
        else:
            return -1 

class Page(Group):
    def __init__(self):
        Group.__init__(self)
        
class Groups():
    def __init__(self,groupsize=50,pagesize=10):
        self.groupsize = groupsize
        self.pagesize = pagesize
        self.curgroup = 0
        self.curpage = 0
        self.maxgroups = 0
        self.sources=[] #
        self._countpage = 0
        self._countgroup = 0
        self._group = None
        self._page = None
        
    def addsource(self,source):
        log.debug('countpage = ',self._countpage,'countgroup = ',self._countgroup)
        if self._countpage >= self.pagesize:
            
            self._countpage = 0
            self._countgroup += 1
            if self._countgroup >= self.groupsize:
                self._group = None
            
        if self._countpage == 0:
            self._page = Page()
            
            if self._group == None:
                self._group = Group()
                self.sources.append(self._group)
                
            self._group.addsource(self._page)
            
            
        self._page.addsource(source)
        self._countpage += 1        
        
    def open(self,file):
        splitline = []
        f=codecs.open(file, 'r','utf8')
        if not f: 
            log4py.debug('error ,cannot open file %s' % file)
            return False

        for line in f.readlines():
            
            splitline = line.split('\t',5)
            #log.debug(splitline)
            char = Char(splitline[1])
            char.setfreq(int(splitline[2]))
            char.setpinyin(splitline[4])
            char.english=splitline[5]
            
            self.addsource(char)
        
        f.close()        
        return True
    
    def getgroup(self,groupid):
        return self.sources[groupid]
    
    def getgroups(self,groupidstart,groupidend):
        return self.sources[groupidstart:groupidend]
    
    def getpage(self,groupid,pageid):
        if pageid < 0 or groupid < 0 :
            log.warn('groupid = ',groupid,'pageid = ', pageid)
            return None
        group = getgroup(groupid)
        return group.sources[pageid]
        
            
#todo 需要将要背诵的对象分组，用next方法来显示，初始化分组    

#unit test
if __name__ == '__main__':
    gs = Groups(6,3)
    gs.open('../data/freq_part.txt')
    group = gs.getgroup(0)
    for page in group.sources:
        for char in page.sources:
            print codecs.encode(char.hanzi,'utf8'),char.freq,char.pinyin,char.english
            #print 
            