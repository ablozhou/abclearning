#!/bin/env python
#coding=utf8

import wx
import sys

class Panel(wx.Panel):
    
    def __init__(self,parent,id):
        wx.Panel.__init__(self,parent,id,style=wx.BORDER_SUNKEN)
        
class Frame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size = (500,400))
        panel = Panel(self, -1)
        myBox = wx.BoxSizer()
        myBox.Add(panel, -1, wx.EXPAND)
        
        self.SetSizer(myBox)
        self.Show()
        
def main():
    app = wx.App()
    frame = Frame(None,-1,'hello test')
    app.MainLoop()
    
if __name__ == '__main__':
    sys.exit(main())