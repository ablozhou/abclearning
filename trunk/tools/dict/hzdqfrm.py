#!/bin/env python
# -*- coding: UTF-8 -*-

import wx
import mainui_xrc
import wx.xrc as xrc
#import modules.group as group
import modules.log4py as log4py
import string
import procdict

log = log4py.log4py('[hzdqframe]')
    
    
class hzdqframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):
        
        mainui_xrc.xrcmframe.__init__(self,parent)
       
        self.txtmain = xrc.XRCCTRL(self, "txtmain")
        
        self.txtsearch = xrc.XRCCTRL(self, "txtsearch")
        self.txtsearch.SetValue('中')
        procdict.procdict('../../data/unihan.zip','blog.csdn.net/ablo_zhou')
#        self.gs = group.Groups(2, 20)
#        self.gs.open('../../data/freq_part.txt')
#        self.g = iter(self.gs)
#        self.group = self.g.next()
#        self.p = iter(self.group)  
       
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
                res += c.encode('utf8')
                continue
            if c in string.digits:
                res += c.encode('utf8')
                continue
           
            try:
                char = self.gs.getunit(c)
                #char.display()
                p = char.getphonetic()
                log.debug(p)
                res += char.char.encode('utf8') + p + ' '
            except AttributeError:
                res += char.encode('utf8')
        self.txtmain.SetValue(res)

    def OnButton_btn_next(self, evt):

        self.p = self.group.next()
        self.txtmain.SetValue(self.p.getstr().encode('utf8'))
