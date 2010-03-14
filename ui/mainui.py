#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import mainui_xrc
import abcframe

#TODO 设置多行文本控件字体
#指定一个文件的另一个执行文件
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = abcframe.abcframe(parent = None)
    frame.Show()
    app.MainLoop()