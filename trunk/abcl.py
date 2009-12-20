#!/bin/dev python
# coding=utf8
import os
import sys
import hanzi
import codecs
import time

f=codecs.open('char1.txt', 'r','utf8')
dict = hanzi.MyDict() 
for line in f.readlines():
    print line
    for  char in line:
        print char
        dict.addchar(hanzi.Char(char))
    
f.close()

#记忆曲线
class Memory():
    def __init__(self,remember=0, lastdate = time.time()):
        self.remember=remember
        self.lastdate=lastdate
        pass
        
    # -5,...,5 共11 等级 
    def addmem(self,count):
        if self.remember < 5 && self.remember > -5: 
            self.remember += count
        return self.remember
    
    
        
