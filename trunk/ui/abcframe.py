#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import os
import mainui_xrc
import wx.xrc as xrc
import modules.group as group
import modules.log4py as log4py
import string
import codecs
import tools.encdet as encdet

log = log4py.log4py('[abcframe]')

class abcframe(mainui_xrc.xrcmframe):
    def __init__(self,parent):

        mainui_xrc.xrcmframe.__init__(self,parent)

        self.txtmain = xrc.XRCCTRL(self, "txtmain")
        self.tree = xrc.XRCCTRL(self, "tree")
        il = wx.ImageList(16,16)
        self.fldridx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FOLDER,
                    wx.ART_OTHER, (16,16)))
        self.fldropenidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN,
                    wx.ART_OTHER, (16,16)))
        self.fileidx = il.Add(
            wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE,
                    wx.ART_OTHER, (16,16)))

        self.tree.AssignImageList(il)
        self.root = self.tree.AddRoot('root')
        filename = '../data/唐诗三百首/唐诗三百首之.卷一、五言古诗.txt'
        #self.AddTreeNodes(filename)
    def OnTool_new(self, evt):
        #self.tree.DeleteAllItems()
        self.tree.DeleteChildren(self.root)

    def OnTool_open(self, event):
        self.filewildchar=['*.txt','*.*']
        dlg = wx.FileDialog(self, "File List", '../data/唐诗三百首/', "", '|'.join(self.filewildchar), wx.OPEN|wx.MULTIPLE)

        #for i, v in enumerate(self.filewildchar):
        #    s = v.split('|')[0]
            #if s.startswith(w):

        dlg.SetFilterIndex(0)
        if dlg.ShowModal() == wx.ID_OK:
            encoding = 'utf8'
            for filename in dlg.GetPaths():
                self.AddTreeNodes(filename)
            dlg.Destroy()

    def AddTreeNodes(self,filename):

        #filename = '../data/唐诗三百首.txt'
        #filename = '../data/唐诗三百首/唐诗三百首之.卷八、五言绝句.txt'
        #filename = '../data/唐诗三百首/唐诗三百首之.卷二、五言乐府.txt'
        #获取文件名作为总节点
        #(path,rootfile) = os.path.split(filename)
        #(rootm,roote) = os.path.splitext(rootfile)


        #text=''
        #encoding = None
        #self.tree.DeleteAllItems()
        encoding,begin = encdet.detect(filename)
        data = open(filename,'rU').read().decode(encoding)
        items = data.split('=============================')
        titles = items[0].splitlines()
        rootm = titles[-2]
        log.debug('root'+rootm)

        root = self.tree.AppendItem(self.root,rootm)
        self.tree.SetItemImage(root, self.fldridx,
                               wx.TreeItemIcon_Normal)
        self.tree.SetItemImage(root, self.fldropenidx,
                               wx.TreeItemIcon_Expanded)

        #log.debug(*items)
        for item  in items[1:]:
            #log.debug(item)
            line = item.splitlines()
            log.debug(line[1])
            it = self.tree.AppendItem(root,line[1].encode('utf8'))
            self.tree.SetItemPyData(it,item)
            self.tree.SetItemImage(it, self.fileidx,
                                   wx.TreeItemIcon_Normal)

        #self.tree.Expand(root)
    def OnTree_sel_changed_tree(self, evt):
        item = evt.GetItem()
        data = self.tree.GetItemPyData(item)
        points = self.txtmain.GetFont().GetPointSize()
        f = wx.Font(points + 10, wx.ROMAN, wx.NORMAL, wx.BOLD, False)

        self.txtmain.SetValue(data)
        pos = data.find('\n\n')
        self.txtmain.SetStyle(0, pos, wx.TextAttr("blue", wx.NullColour, f))

    def open(self,filename):
        self.data = file(filename,'rb').read()
        #self.txtmain.SetValue(t)
#        self.gs = group.Groups(2, 20)
#        self.gs.open('../data/freq_part.txt')
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

        #self.p = self.group.next()
        #self.txtmain.SetValue(self.p.getstr().encode('utf8'))
        #self.tree.
        pass
