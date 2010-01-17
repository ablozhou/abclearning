#!/bin/env python
# -*- coding: UTF-8 -*-

import wx
import mainui_xrc
import wx.xrc as xrc
import modules.group as group
import modules.log4py as log4py

log = log4py.log4py('[abcframe]')

class abcframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):
        
        mainui_xrc.xrcmframe.__init__(self,parent)
       
        self.txtmain = xrc.XRCCTRL(self, "txtmain")
        
        self.txtsearch = xrc.XRCCTRL(self, "txtsearch")
        self.txtsearch.SetValue('中')
        
        self.gs = group.Groups(2, 20)
        self.gs.open('../data/freq_part.txt')
        self.g = iter(self.gs)
        self.group = self.g.next()
        self.p = iter(self.group)        
        
    def OnButton_btnsearch(self, evt):
        log.debug('OnButton_btnsearch')
        search = self.txtsearch.GetValue()
        self.txtmain.SetValue(search)
        char = self.gs.getunit(search)
        char.display()
        p = char.getphonetic()
        log.debug(p)
        res = char.char.encode('utf8') + p
        self.txtmain.SetValue(res)

    def OnButton_btn_next(self, evt):

        self.p = self.group.next()
        self.txtmain.SetValue(self.p.getstr().encode('utf8'))
