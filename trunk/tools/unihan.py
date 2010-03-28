#!/bin/env python
#coding:utf8

import modules.log4py as log4py
import modules.char as char
import codecs
import string
import cPickle as pk
import sys
import traceback

log = log4py.log4py('[unihan]')
file_src = '../data/Unihandata.txt'
file_write='../data/unihan3.txt'
'''
0x4E00-0x9FFF       CJK 统一字型               常用字          共 20992个（实际只定义到0x9FC3)
0x3400-0x4DFF       CJK 统一字型扩展表A     少用字   共 6656个
0x20000-0x2A6DF   CJK 统一字型扩展表B  少用字，历史上使用  共42720个
0x2A700-0x2B73F   CJK 统一字型扩展表C    共4160个汉字，全部定义
0xF900-0xFAFF       CJK 兼容字型        重复字，可统一变体，共同字  共512个
0x2F800-0x2FA1F   CJK 兼容字型补遗    可统一变体 共544个
'''
WUBI=1
CANGJIE=2
FOURCORNER=3
ZHENGMA=4

dict={}
spaces=['',' ','\t','\n']
hzlist=[]

#unicode hanzi
DEBUG = False
COUNT = 5000
if DEBUG != True:
    for hz in xrange(0x4E00,0xA000):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x3400,0x4E00):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x2A700,0x2B740):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))

    for hz in xrange(0x20000,0x2A6E0):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0xF900,0xFB00):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))
    for hz in xrange(0x2F800,0x2FA20):
        hz = unichr(hz)
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)
    print hex(ord(hz))



splitline = []

f=codecs.open(file_src, 'r','utf8')
fw = codecs.open(file_write, 'w+','utf8')
if not f:
    log.debug('error ,cannot open file %s' % file_src)
    exit(-1)

lines = f.read().split('\n')
i=0

for line in lines:
    if line in spaces:
        continue
    if line[0] == '#':
        continue

    i+=1
    if DEBUG == True:
        if i >COUNT: break
    splitline = line.split('\t',5)
    print line.encode('utf8')
    splitline[0] = splitline[0].replace('U+','0x',2)
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
    phonetic = splitline[2].lower()
    #print 'line '+str(i)+splitline[2].encode('utf8')
    if key == 'kDefinition':
        english = splitline[2]
        le = char.Language(char.English)
        le.addgloss(english)
        ch.addlang(le)

    elif key == 'kMandarin':
        langch = ch.getlang(char.Chinese)
        if langch == None:
            langch = char.Language(char.Chinese)
            ch.addlang(langch)

        t = phonetic.split(' ')
        print t
        ch.addphonetic('py:'+'/'.join(t))

    elif key == 'kHanyuPinyin':
        langch = ch.getlang(char.Chinese)
        if langch == None:
            langch = char.Language(char.Chinese)
            ch.addlang(langch)
        z = phonetic.split(' ')
        t=[]
        for p in z:
            s = p.split(':')
            t += s[1].split(',')
        ch.addphonetic('py:'+'/'.join(t))

    elif key == 'kXHC1983':
        langch = ch.getlang(char.Chinese)
        if langch == None:
            langch = char.Language(char.Chinese)
            ch.addlang(langch)

        p = phonetic.split(' ')
        t=[]
        for p1 in p:
            c = p1.split(':')
            t.append(c[1])
        ch.addphonetic('py:'+'/'.join(t))

    elif key == 'kCantonese':
        #广东话
        langch = ch.getlang(char.Chinese)
        if langch == None:
            langch = char.Language(char.Chinese)
            ch.addlang(langch)
        t = phonetic.split(' ')
        ch.addphonetic('Cant:'.decode('utf8')+'/'.join(t),char.Cantonese,char.Chinese)

    elif key == 'kHangul':
        langKorean = ch.getlang(char.Korean)
        if langKorean == None:
            langKorean = char.Language(char.Korean)
            ch.addlang(langKorean)
        ch.addphonetic('Hangul:'.decode('utf8')+phonetic,char.Hangul,char.Korean)

    elif key == 'kKorean':
        #韩语
        langKorean = ch.getlang(char.Korean)
        if langKorean == None:
            langKorean = char.Language(char.Korean)
            ch.addlang(langKorean)
        ch.addphonetic('KoRom:'.decode('utf8')+phonetic,char.Korean_roman,char.Korean)

    elif key == 'kJapaneseKun':
        #日语
        langjp = ch.getlang(char.Japanese)
        if langjp == None:
            langjp = char.Language(char.Japanese)
            ch.addlang(langjp)

        ch.addphonetic('JKun:'.decode('utf8')+phonetic,char.JapaneseKun,char.Japanese)

    elif key == 'kJapaneseOn':
        #日语
        langjp = ch.getlang(char.Japanese)
        if langjp == None:
            langjp = char.Language(char.Japanese)
            ch.addlang(langjp)

        ch.addphonetic('JOn:'.decode('utf8')+phonetic,char.JapaneseOn,char.Japanese)

    elif key == 'kVietnamese':
        #越南语
        langviet = ch.getlang(char.Vietnamese)
        if langviet == None:
            langviet = char.Language(char.Vietnamese)
            ch.addlang(langviet)

        ch.addphonetic('Viet:'.decode('utf8')+phonetic,char.Vietnamese,char.Vietnamese)

#=============cangjie
filedic_src = '../data/Unihan_DictionaryLikeData.txt'
#file_write='../data/unihan2.txt'
splitline = []

fcangjie=codecs.open(file_src, 'r', 'utf8')
#fw = codecs.open(file_write, 'w+', 'utf8')
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
#filewb_write='../data/wubiout.txt'


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
    ch.strokes = item[6][:-1] #去掉换行


#==============

index={}
lens = 0
i=0
for hz in hzlist:
    i +=1
    cons = False
    if DEBUG == True:
        if i> COUNT : break
    ch = dict[hz]
    py = ''
    gloss = ''
    py = ch.getphonetics()
    gloss = ch.getgloss()
    hx = hex(ord(ch.char))
    #a = ch.char
    linew = hz+'\t'+hx + '\t'
    if len(py) > 2:

        linew += py
        cons = True
############################3
#处理五笔，仓颉，郑码，笔画
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

    # try:
    #linew = hz+'\t'+hx+'\t'
    if len(cj) != 0: #仓颉码
        if cons == True:
            linew += ','
        cons = True
        linew += 'cj:'+cj
    if len(fc) != 0: #四角号码
        if cons == True:
            linew += ','
        linew +='4c:'+fc
        cons = True
    if len(wb) != 0: #五笔
        if cons == True:
            linew += ','
        linew +='wb:'+wb
        cons = True

    if len(zm) != 0: #郑码
        if cons == True:
           linew += ','
        linew +='zm:'+zm
        cons = True

    if ch.strokenum != -1: #笔画数
        if cons == True:
           linew += ','
        linew +='sn:'+str(ch.strokenum)
        cons = True

    if ch.freq != -1: #频率等级 1-5，1最高
        if cons == True:
           linew += ','
        linew +='fq:'+str(ch.freq)
        cons = True

    if len(ch.radical) != 0: #偏旁部首
        if cons == True:
           linew += ','
        linew +='rd:'+ch.radical
        cons = True

    if len(ch.strokes) != 0: #笔顺 横竖撇捺弯 1,2,3,4,5
        if cons == True:
           linew += ','
        linew +='st:'+ch.strokes
        cons = True

    linew += '\t'+gloss
    linew += '\n'

    index[hz.encode('utf8')]=lens #utf8 index
    #

    #p = ch.char+'\t'+ hex(ord(ch.char))+ '\t' +  ch.getphonetics()+'\n'
    print linew.encode('utf8')
    fw.write(linew)
    lens = fw.tell()#fw.write('\n')
    #print lens

fw.close()

#持久性 序列化
fpk = file('../data/hzidx.dat','wb')
pk.dump(index,fpk,True)
fpk.close()
