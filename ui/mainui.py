#!/bin/env python
# -*- coding: UTF-8 -*-

import wx
import mainui_xrc
import abcframe
       

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = abcframe.abcframe(parent = None)
    frame.Show()
    app.MainLoop()