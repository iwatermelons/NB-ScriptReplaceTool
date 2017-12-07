# -*- coding:utf-8 -*-

import wx
import src.events  as events
import src.help as help


class App(wx.App):
     def OnInit(self):
         frame = events.MyFrame2(None)
         frame.Show()
         return True
 
if __name__ == '__main__':
    app = App(False)
    help.HelpText()
    app.MainLoop()
