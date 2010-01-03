#!/bin/dev python
# coding=utf8

from memory import *
import codecs

class Char: #字，词
    def __init__(self,char):
        self.mem = Memory()
        self.char=char
        self.freq=1
        self.phonetic='' #拼音 phonetic symbols
        self.stroknum=1 #笔画 number of strokes
        
       
    def display(self):
        #print self.char,phonetic
        if self.mem :
            self.mem.addfamiliar(1)
            self.mem.setlasttime()
        print codecs.encode(self.char,'utf8'),self.freq,codecs.encode(self.phonetic,'utf8'),self.english


        
class CharDict:
    
    def __init__(self):
        self.dict={}
        pass
        
    def addchar(self, char):
        self.dict[char.char] = char
