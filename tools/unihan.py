#!/bin/env python
#coding:utf8

import modules.log4py as log4py
import modules.char as char
import codecs
import string
import cPickle as pk
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


log = log4py.log4py('[unihan]')
file_src = '../data/Unihandata.txt'
file_write='../data/unihan.txt'
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
for hz in hzlist:
    i +=1
    if DEBUG == True:
        if i> 5000 : break
    ch = dict[hz]
    py = ch.getphonetics()
    gloss = ch.getgloss()
    hx = hex(ord(ch.char))
    a = ch.char
    line = hz+'\t'+hx+'\t'+py+'\t'+gloss+'\n'

    index[hz.encode('utf8')]=lens #utf8 index
    #
    
    #p = ch.char+'\t'+ hex(ord(ch.char))+ '\t' +  ch.getphonetics()+'\n'
    print line.encode('utf8')
    fw.write(line)
    lens = fw.tell()#fw.write('\n')
    #print lens

fw.close()

#持久性 序列化
fpk = file('../data/hzidx.dat','wb')
pk.dump(index,fpk,True)
fpk.close()
