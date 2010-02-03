#!/bin/env python
#coding:utf8

import modules.log4py as log4py
import modules.char as char
import codecs
import string
import cPickle as pk

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
spaces=['',' ','\t','\n']
hzlist=[]

#unicode hanzi
DEBUG = False

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



log = log4py.log4py('[unihan2]')
file_src = '../data/Unihan_DictionaryLikeData.txt'
file_write='../data/unihan2.txt'
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
        if i >5000: break
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
    data = splitline[2].lower()
    #print 'line '+str(i)+splitline[2].encode('utf8')
    if key == 'kCangjie':
        ch.consult[CANGJIE]=data
               
    elif key == 'kFourCornerCode':
        ch.consult[FOURCORNER]=data
        
    elif key == 'kFrequency':
        ch.freq=int(data)
    elif key == 'kTotalStrokes':
        ch.strokenum=int(data)
    


#持久性 序列化
#fpk = file('../data/hz.dat','wb')
#pk.dump(hzlist,fpk,True)
#pk.dump(dict,fpk,True)    
#fpk.close()
#
#fpk1 = file('../data/hz.dat','rb')
#hzlist1 = pk.load(fpk1)
#dict1=pk.load(fpk1)
#fpk1.close()



index={}
lens = 0
i=0


###################################
#处理五笔码等
filewb_src = '../data/wubi.txt'
filewb_write='../data/wubiout.txt'


fwb=codecs.open(file_src, 'r','utf8')
#fwwb = codecs.open(file_write, 'w+','utf8')
if not fwb: 
    log.debug('error ,cannot open file %s' % filewb_src)
    exit(-1) 

lineswb = fwb.read().split('\n')
fwb.close()
i=0
item=[]

for line in lines:
    i +=1
    #if i>1000 :break
    if len(line) <2:break
    print line.encode('utf8')
    item = line.split(' ')
    hz = item[0].decode('utf8')
    try:
        ch = dict[hz]
    except KeyError:
        ch = char.Char(hz)
        dict[hz]=ch
        hzlist.append(hz)    
    #ch = char.Char(item[0])
    ch.stroknum=item[4]
    ch.consult[WUBI]=item[2]
    ch.consult[ZHENGMA]=item[3]
    ch.radical = item[5]
    ch.strokes = item[6]
    #fw.write(ch.char+ch.stroknum+ch.consult[WUBI]+ch.consult[ZHENGMA]+ch.radical+ch.strokes)
    
    #fw.write(line)
    #fw.write('\n')
    


####################################
#write to file
for hz in hzlist:
    
    i +=1
    if DEBUG == True:
        if i> 5000 : break
    ch = dict[hz]
    if ch in (' ','\n','\t'):
        continue
    cj=''
    fc=''
    wb=''
    zm=''
    try:
        cj = ch.consult[CANGJIE]
    except KeyError:
        pass
    try:        
        fc= ch.consult[FOURCORNER]
    except KeyError:
        pass
    try:        
        wb= ch.consult[WUBI]
    except KeyError:
        pass
    try:        
        zm= ch.consult[ZHENGMA]
    except KeyError:
        pass

    hx = hex(ord(ch.char))
    
    #a = ch.char
    try:
        line = hz+'\t'+hx+'\t'+'cj:'+cj+','+'fc:'+fc+',wb:'+wb
        line +=',zm:'+zm+'\trd:'+ch.radical+'\tsn:'+str(ch.strokenum)
        line +='\tfq:'+str(ch.freq)+'\tst:'+ch.strokes+'\n'
    except AttributeError:
        print 'AttributeError'+hx
        continue
    index[hz.encode('utf8')]=lens #utf8 index
    #
    
    #p = ch.char+'\t'+ hex(ord(ch.char))+ '\t' +  ch.getphonetics()+'\n'
    print line.encode('utf8')
    fw.write(line)
    lens = fw.tell()#fw.write('\n')
    #print lens

fw.close()

#持久性 序列化
fpk = file('../data/hzidxcj.dat','wb')
pk.dump(index,fpk,True)
fpk.close()
