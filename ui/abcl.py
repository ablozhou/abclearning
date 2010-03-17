#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx
import sys
import abcxrc
import abclfrm

class AbclApp(wx.App):
    def OnInit(self):

        self.mainfrm = abclfrm.abclfrm(parent = None)

        self.SetTopWindow(self.mainfrm)
        self.mainfrm.Show()
        return True

    def Exit(self):
        pass



#指定一个文件的另一个执行文件
def main():
    app = AbclApp(0)

    app.MainLoop()


if __name__ == '__main__':
    sys.exit(main())
