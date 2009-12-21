#!/bin/dev python
# coding=utf8
import os
import sys
import hanzi
import codecs
import time

import modules 

f=codecs.open('char1.txt', 'r','utf8')
dict = hanzi.MyDict() 
for line in f.readlines():
    print line
    for  char in line:
        print char
        dict.addchar(hanzi.Char(char))
    
f.close()

#todo group 要作成迭代器
def getnext(Char):
    Char.display()
#unit test
#todo 接受输入参数，获取输入，得到下一组汉字或需记忆的词组
if __name__ == '__main__':
    getnext(
    while True:
        cmd = input '输入命令'
        if cmd=='n':
            getnext
    
        
