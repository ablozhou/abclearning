#!/bin/dev python
# coding=utf8

import modules 

class Hanzi:
    def __init__(self,hanzi):
        self.mem=None
        self.hanzi=hanzi
        self.freq=1
        self.pinyin=''
        self.bihua=1
        self.english=''
        
    def setfreq(self, freq):
        self.freq = freq
    
    def setpinyin(self, pinyin):
        self.pinyin = pinyin
        
    def setbihua(self, bihua):
        self.bihua
        
    def display(self):
        print self.hanzi,pinyin
        if self.mem :
            self.mem.addfamiliar(1)
            self.mem.setlasttime()

class Char(Hanzi):
    def __init__(self,char):
        Hanzi.__init__(char)
        self.mem = modules.Memory()
        
class MyDict:
    
    def __init__(self):
        self.dict={}
        pass
        
    def addchar(self, char):
        self.dict[char.char] = char
