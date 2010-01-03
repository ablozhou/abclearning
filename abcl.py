#!/bin/dev python
# coding=utf8
import os
import sys
#import hanzi
import codecs
import time

#from  modules import *
import modules.group
#todo group 要作成迭代器
def getnext(page):
    page.display()
#unit test
#todo 接受输入参数，获取输入，得到下一组汉字或需记忆的词组
#todo 给一个汉字，查询读音，释义，例句
if __name__ == '__main__':
    gs = modules.group.Groups(2,20)
    gs.open('./data/freq_part.txt')  
    g = iter(gs) 
    group = g.next()
    p = iter(group) 
    while True:
        cmd = raw_input('>> ')
        #print cmd
        if cmd=='n':
            try:
                p = group.next()
                p.display()
            except StopIteration:
                try:
                    group = g.next()
                    p = iter(group)
                    p = group.next()
                    p.display()            
                except StopIteration:
                    print 'finished pages'
        if cmd == 'q':
            print 'exit!'
            exit()
        if cmd == 'b':
            print 'from begining ...'
            g = iter(gs) 
            group = g.next()
            p = iter(group) 
            
        
