#!/bin/env python
#coding:utf8
import sys
print sys.path
import zipfile
import modules.char as char

space=[' ','\t','\n']
class procdict:
    def __init__(self,zipfile,passwd):
        self.zipfile = zipfile
        self.passwd = passwd
        self.dict = {}
        self.readzipfile(zipfile,passwd)#'../../data/hz1.zip','http://blog.csdn.net/ablo_zhou')
        
    def getdict(self):
        return self.dict
        
    
    def readzipfile(self,filename,passwd):
        f = zipfile.ZipFile(filename,'r',zipfile.ZIP_DEFLATED)
        f.setpassword(passwd)
        self.dicttxt = f.read('unihan.txt')
        f.close()
        
        #self.builddict(dicttxt)
        
    def builddict(self,hzdict):
        hzlist = hzdict.split('\n')
        
        for line in hzlist:
            print line
            
            if line in space:
                continue
            
            part = line.split('\t')
            if len(part) < 2:
                continue
            c = char.Char(part[0])
            self.dict[c.char]=c
            #处理拼音
            for s in part[2].split(','):
                ph = s.split(':')
                if ph[0] == 'py':
                    l = char.Language(char.Chinese)
                    l.addphonetic(ph[1])
                    c.addlang(l)
                elif ph[0] == 'Cant':
                    l = char.Language(char.Chinese)
                    l.addphonetic(ph[1],char.Cantonese,char.Chinese)
                    c.addlang(l)
                elif ph[0] == 'Hangul':
                    l = char.Language(char.Korean)
                    l.addphonetic(ph[1],char.Hangul,char.Korean)
                    c.addlang(l)
    
                elif ph[0] == 'KoRom':
                    l = char.Language(char.Korean)
                    l.addphonetic(ph[1],char.Korean_roman,char.Korean)
                    c.addlang(l)
                    
                elif ph[0] == 'JKun':
                    l = char.Language(char.Japanese)
                    l.addphonetic(ph[1],char.JapaneseKun,char.Japanese)
                    c.addlang(l)
                    
                elif ph[0] == 'JOn':
                    l = char.Language(char.Japanese)
                    l.addphonetic(ph[1],char.JapaneseOn,char.Japanese)
                    c.addlang(l)
                
                elif ph[0] == 'Viet':
                    l = char.Language(char.Vietnamese)
                    l.addphonetic(ph[1],char.Vietnamese,char.Vietnamese)
                    c.addlang(l)
                
            #处理注释
            g = part[3]
            if g != '':
                l = char.Language(char.English)
                l.addgloss(g)
                c.addlang(l)

    def getchar(self,char):
        lines = self.dicttxt.split('\n')
        
        #ch = self.dict[char]
        #print str(i)+ch.char.encode('utf8')
        py = ch.getphonetics()
        #print py.encode('utf8')
        gloss = ch.getgloss()
        hx = hex(ord(ch.char.decode('utf8')))
        #print hx
        
        p = char+hx+py+gloss
        #p = ch.char+'\t'+ hex(ord(ch.char))+ '\t' +  ch.getphonetics()+'\n'
        print p

if __name__ == '__main__':
    d = procdict('../../data/unihan.zip','blog.csdn.net/ablo_zhou')
    d.getchar('一')
    d.getchar('绿')
    d.getchar('掠')
    