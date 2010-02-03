#!/bin/env python
#coding:utf8

import modules.log4py as log4py
import modules.char as char
import codecs
import string

dict={}
spaces=['',' ','\t','\n']
hzlist=[]

log = log4py.log4py('[unihan1]')
file_src = '../data/unihan2.txt'
file_write='../data/wubi.txt'
splitline = []

f=codecs.open(file_src, 'r','utf8')
fw = codecs.open(file_write, 'w+','utf8')
if not f: 
    log.debug('error ,cannot open file %s' % file_src)
    exit(-1) 

lines = f.read().split('\n')
f.close()
i=0
item=[]

WUBI=1
CANGJIE=2
FOURCORNER=3
ZHENGMA=4




for line in lines:
    i +=1
    #if i>1000 :break
    if len(line) <2:break
    print line.encode('utf8')
    item = line.split(' ')
    ch = char.Char(item[0])
    ch.stroknum=item[4]
    ch.consult[WUBI]=item[2]
    ch.consult[ZHENGMA]=item[3]
    ch.radical = item[5]
    ch.strokes = item[6]
    fw.write(ch.char+ch.stroknum+ch.consult[WUBI]+ch.consult[ZHENGMA]+ch.radical+ch.strokes)
    
    #fw.write(line)
    fw.write('\n')
    
fw.close()