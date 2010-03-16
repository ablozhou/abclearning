#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import mainui_xrc
import abcframe

class AbclApp(wx.App):
    def OnInit(self):

        self.mainfrm = abcframe.abcframe(parent = None)

        self.SetTopWindow(self.mainfrm)
        self.mainfrm.Show()
        return True

    def Exit(self):
        pass



#指定一个文件的另一个执行文件
if __name__ == '__main__':
    app = AbclApp(0)

    app.MainLoop()