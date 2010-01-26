#!/bin/env python
# -*- coding: utf8 -*-

import wx
import mainui_xrc
import wx.xrc as xrc
#import modules.group as group
import modules.log4py as log4py
import string
import procdict
import cPickle as pk

log = log4py.log4py('[hzdqframe]')
    
    
class hzdqframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):
        
        mainui_xrc.xrcmframe.__init__(self,parent)
       
        self.txtmain = xrc.XRCCTRL(self, "txtmain")
        
        self.txtsearch = xrc.XRCCTRL(self, "txtsearch")
        self.txtsearch.SetValue('中')
        s = self.txtsearch.GetValue().encode('utf8')
        f = file('../../data/hzidx.dat','rb')
        self.hzidx = pk.load(f)
        f.close()
        #self.procdict = procdict.procdict('../../data/unihan.zip','blog.csdn.net/ablo_zhou')
        #self.unihan = self.procdict.dicttxt
           
        self.unihan = file('../../data/unihan.txt','rb')
        #indx = '㐅'

        seek = self.hzidx[s]
        self.unihan.seek(seek)
        line = self.unihan.readline()
        self.txtmain.SetValue(line)

    def __del__(self):
        self.unihan.close()

#        self.gs = group.Groups(2, 20)
#        self.gs.open('../../data/freq_part.txt')
#        self.g = iter(self.gs)
#        self.group = self.g.next()
#        self.p = iter(self.group)  
    def fmtgloss(self,gloss):
        glist = gloss.split(':')
        if glist[0] == 'en_gls':
            return '\n英语解释:\t'+glist[1]
        return ''
    
    def fmtphonetic(self,phonetic):
        plist = phonetic.split(',')
        fmt = ''
        #处理拼音
        for s in plist:
            ph = s.split(':')
            if ph[0] == 'py': #拼音
                fmt += '\n汉语拼音:'+ph[1]
            elif ph[0] == 'Cant':
                fmt += '\n粤语读音:'+ph[1]
            elif ph[0] == 'Hangul':
                fmt += '\n韩语读音:'+ph[1]
            elif ph[0] == 'KoRom':
                fmt += '\n韩语罗马读音:'+ph[1]
            elif ph[0] == 'JKun':
                fmt += '\n日本本土读音:'+ph[1]
            elif ph[0] == 'JOn':
                fmt += '\n日本中国读音:'+ph[1]
            elif ph[0] == 'Viet':
                fmt += '\n越南语读音:'+ph[1]
        return fmt
    
    def fmtunicode(self,unicode):
        return '\nUnicode:'+unicode
           
    def OnButton_btnsave(self, evt):
        f = open('save.txt','a')
        r = self.txtmain.GetValue().encode('utf8')
        f.write(r)
        f.close()
            
    def OnButton_btnsearch(self, evt):
        log.debug('OnButton_btnsearch')
        search = self.txtsearch.GetValue()
        self.txtmain.SetValue(search)
        res = ''
        #p = phonetic.strip();
        space = [' ', '\n', '\t']
        for c in search:
            if c == u'-' or c in space:
                res += c.encode('utf8')
                continue
            if c in string.letters:
                res += c.encode('utf8')+'\n'
                continue
            if c in string.digits:
                res += c.encode('utf8')+'\n'
                continue
           
            try:
                seek = self.hzidx[c.encode('utf8')]
                self.unihan.seek(seek)
                line = self.unihan.readline()
                #self.txtmain.SetValue(line)
                
                
                log.debug(line)
                l = line.split('\t')
                fmt = l[0]+'\n'+'='*30
                #for part in l[1:]:
                fmt += self.fmtunicode(l[1])
                fmt += self.fmtphonetic(l[2])
                fmt += self.fmtgloss(l[3])
                res += fmt +'\n\n'
                res += '='*30
            except AttributeError:
                res += c +'\n'
        self.txtmain.SetValue(res)

    def OnButton_btn_next(self, evt):

        self.p = self.group.next()
        self.txtmain.SetValue(self.p.getstr().encode('utf8'))
