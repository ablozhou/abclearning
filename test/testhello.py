#!/bin/env python
#-*- coding=utf8 -*-

import wx
import hello_xrc

app = wx.PySimpleApp()
frame = hello_xrc.xrczframe(parent = None)
frame.Show()
app.MainLoop()