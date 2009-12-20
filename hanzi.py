#!/bin/dev python

class Hanzi:
    def __init__(self, Hanzi):
        self.char=char
        self.freq=1
        self.pinyin=''
        self.bihua=1
        
    def setfreq(self, freq):
        self.freq = freq
    
    def setpinyin(self, pinyin):
        self.pinyin = pinyin
        
    def setbihua(self, bihua):
        self.bihua

class Char(Hanzi):
    def __init__(self,Char):
        Hanzi.__init__(Char)
        
class MyDict:
    
    def __init__(self):
        self.dict={}
        pass
        
    def addchar(self, char):
        self.dict[char.char] = char
