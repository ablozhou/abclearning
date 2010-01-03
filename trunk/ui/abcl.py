#!/bin/env python
#coding=utf8

import wx
import sys
sys.path.append('/home/zhouhh/abclearning')
import modules.group
#import modules.char

class MainPanel(wx.Panel):
    
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id,style=wx.BORDER_SUNKEN)
        leftbox = wx.BoxSizer(wx.VERTICAL)
        self.medit = wx.TextCtrl(self,-1,name='medit',style=wx.TE_MULTILINE)
        self.medit.SetEditable(True)
        self.inputtxt = wx.TextCtrl(self,-1,name='input',style=wx.TE_MULTILINE)
        leftbox.Add(self.inputtxt,1,wx.EXPAND|wx.TOP|wx.LEFT,5)
        leftbox.Add(self.medit,4,wx.EXPAND|wx.TOP|wx.LEFT,5)

        self.SetSizer(leftbox)
        
class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size = (500,400))
        panel = MainPanel(self, -1)
        myBox = wx.BoxSizer()
        myBox.Add(panel, -1, wx.EXPAND)
        
        self.SetSizer(myBox)
        self.Show()
        
def main():
    app = wx.App()
    frame = Frame(None,-1,'学认汉字')
    app.MainLoop()
    
if __name__ == '__main__':
    sys.exit(main())
