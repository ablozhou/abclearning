#!/bin/env python
#coding:utf8

import modules.log4py as log4py
import modules.char as char
import codecs
import string
import cPickle as pk
import traceback
import sys
WUBI=1
CANGJIE=2
FOURCORNER=3
ZHENGMA=4

'''
0x4E00-0x9FFF       CJK 统一字型               常用字          共 20992个（实际只定义到0x9FC3)
0x3400-0x4DFF       CJK 统一字型扩展表A     少用字   共 6656个
0x20000-0x2A6DF   CJK 统一字型扩展表B  少用字，历史上使用  共42720个
0xF900-0xFAFF       CJK 兼容字型        重复字，可统一变体，共同字  共512个
0x2F800-0x2FA1F   CJK 兼容字型补遗    可统一变体 共544个
'''
dict={}
spaces=['', ' ', '\t', '\n']
hzlist=[]

#unicode hanzi
DEBUG = False
COUNT = 5000
if DEBUG != True:
    for hz in xrange(0x4E00, 0xA000):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x3400, 0x4E00):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x20000, 0x2A6E0):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0xF900, 0xFB00):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x2F800, 0x2FA20):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))



log = log4py.log4py('[unihan2]')
filedic_src = '../data/Unihan_DictionaryLikeData.txt'
file_write='../data/unihan2.txt'
splitline = []

fcangjie=codecs.open(file_src, 'r', 'utf8')
fw = codecs.open(file_write, 'w+', 'utf8')
if not fcangjie:
    log.debug('error ,cannot open file %s' % file_src)
    exit(-1)
#if DEBUG:
#    f.seek(5000)
linescj = fcangjie.read().split('\n')
fcangjie.close()
if DEBUG:
    linescj = linescj[10000:]
i=0

for line in linescj:
    if line in spaces:
        continue
    if line[0] == '#':
        continue
    i+=1
    if DEBUG == True:
        if i > COUNT:
            break
    splitline = line.split('\t', 5)
    print line.encode('utf8')
    splitline[0] = splitline[0].replace('U+', '0x', 2)
    value = eval(splitline[0])
    hz = unichr(value)
    #print hz.encode('utf8')
    try:
        ch = dict[hz]
    except KeyError:
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)

    key = splitline[1]
    #print 'splitline[2]:' + splitline[2].lower().encode('utf8')
    data = splitline[2].lower()
    #print 'line '+str(i)+splitline[2].encode('utf8')
    if key == 'kCangjie':
        ch.consult[CANGJIE]=data

    elif key == 'kFourCornerCode':
        ch.consult[FOURCORNER]=data
    elif key == 'kTotalStrokes':
        ch.strokenum = int(data)
    elif key == 'kFrequency':
        ch.freq=int(data)
    elif key == 'kTotalStrokes':
        ch.strokenum=int(data)

i=0

###################################
#处理五笔码等
filewb_src = '../data/wubi.txt'
filewb_write='../data/wubiout.txt'


fwb=codecs.open(filewb_src, 'r', 'utf8')
#fwwb = codecs.open(file_write, 'w+','utf8')
if not fwb:
    log.debug('error ,cannot open file %s' % filewb_src)
    exit(-1)

lineswb = fwb.read().split('\n')
fwb.close()
i=0
item=[]

for line in lineswb:
    i +=1
    if DEBUG == True:
        if i > COUNT:
            break
    if len(line) < 2:
        log.warn('line len <2')
        break

    if line[0] == '#':
        continue

    print line.encode('utf8')
    item = line.split(' ')
    hz = item[0]
    if len(hz) == 0:
        log.debug('empty line of '+filewb_src)
        continue

    try:
        ch = dict[hz]
    except KeyError:
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    #ch = char.Char(item[0])
    ch.strokenum=item[4]
    ch.consult[WUBI]=item[2].lower()
    ch.consult[ZHENGMA]=item[3].lower()
    ch.radical = item[5]
    ch.strokes = item[6]


####################################
#write to file
i=0
lens = 0
for hz in hzlist:

    i +=1
    if DEBUG == True:
        if i > COUNT:
            break
    ch = dict[hz]
    if ch in (' ', '\n', '\t'):
        continue
    cj=''
    fc=''
    wb=''
    zm=''

    try:
        cj = ch.consult[CANGJIE]
    except KeyError:
        message = traceback.format_exception(*sys.exc_info())
        print ''.join(message)

    try:
        fc= ch.consult[FOURCORNER]
    except KeyError:
        message = traceback.format_exception(*sys.exc_info())
        print ''.join(message)
    try:
        wb= ch.consult[WUBI]
    except KeyError:
        message = traceback.format_exception(*sys.exc_info())
        print ''.join(message)
    try:
        zm= ch.consult[ZHENGMA]
    except KeyError:
        message = traceback.format_exception(*sys.exc_info())
        print ''.join(message)

    hx = hex(ord(ch.char))

    cons = False
   # try:
    line = hz+'\t'+hx+'\t'
    if len(cj) != 0:
        cons = True
        line += 'cj:'+cj
    if len(fc) != 0:
        if cons == True:
            line += ','
        line +='4c:'+fc
        cons = True

    if len(wb) != 0:
        if cons == True:
            line += ','
        line +='wb:'+wb
        cons = True

    if len(zm) != 0:
        if cons == True:
           line += ','
        line +='zm:'+zm
        cons = True

    if ch.strokenum != -1:
        if cons == True:
           line += ','
        line +='sn:'+str(ch.strokenum)
        cons = True

    if ch.freq != -1:
        if cons == True:
           line += ','
        line +='fq:'+str(ch.freq)
        cons = True

    if len(ch.radical) != 0:
        if cons == True:
           line += ','
        line +='rd:'+ch.radical
        cons = True

    if len(ch.strokes) != 0:
        if cons == True:
           line += ','
        line +='st:'+ch.strokes
        cons = True

    line += '\n'

    index[hz.encode('utf8')]=lens #utf8 index


    print line.encode('utf8')
    fw.write(line)
    lens = fw.tell()#fw.write('\n')


fw.close()

#持久性 序列化
fpk = file('../data/hzidxcj.dat', 'wb')
pk.dump(index, fpk, True)
fpk.close()
