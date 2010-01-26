#!/bin/env python
# -*- coding: utf8 -*-
#	Author:	ablozhou
#	E-mail:		ablozhou@gmail.com
#
#	Copyright 2010 ablozhou
#
#	Distributed under the terms of the GPL (GNU Public License)
#
#   abcl is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   modify history
#   date          author    notes
#   2010.1.26    ablozhou   release 0.5 
#

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
    