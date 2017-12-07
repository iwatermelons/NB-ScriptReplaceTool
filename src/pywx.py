# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NB-Script Replace Tool", pos = wx.DefaultPosition, size = wx.Size( 734,540 ), style = wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.Size( 500,500 ), wx.DefaultSize )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"选择操作目录", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer12.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_dirPicker3 = wx.DirPickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer12.Add( self.m_dirPicker3, 1, wx.ALL, 5 )
        
        self.m_button4 = wx.Button( self.m_panel2, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.Size( 45,-1 ), 0 )
        bSizer12.Add( self.m_button4, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer12, 0, wx.EXPAND, 5 )
        
        self.m_staticline2 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        
        gSizer5 = wx.GridSizer( 0, 3, 0, 0 )
        
        self.m_staticText111 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Input目录中文件数量", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText111.Wrap( -1 )
        gSizer5.Add( self.m_staticText111, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl91 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        gSizer5.Add( self.m_textCtrl91, 0, wx.ALL, 5 )
        
        self.m_button261 = wx.Button( self.m_panel2, wx.ID_ANY, u"读取文件", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        gSizer5.Add( self.m_button261, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( gSizer5, 0, wx.EXPAND, 5 )
        
        self.m_staticline8 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText31 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Old data EXCEL ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        bSizer17.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_filePicker7 = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer17.Add( self.m_filePicker7, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText1111 = wx.StaticText( self.m_panel2, wx.ID_ANY, u" Old Data Sheet", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1111.Wrap( -1 )
        bSizer17.Add( self.m_staticText1111, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl911 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"locale_input", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_textCtrl911, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer17, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText311 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"New data EXCEL", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText311.Wrap( -1 )
        bSizer171.Add( self.m_staticText311, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_filePicker71 = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer171.Add( self.m_filePicker71, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText11111 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"New Data Sheet", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11111.Wrap( -1 )
        bSizer171.Add( self.m_staticText11111, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_textCtrl9111 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"NewData", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer171.Add( self.m_textCtrl9111, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer171, 0, wx.EXPAND, 5 )
        
        gSizer52 = wx.GridSizer( 0, 4, 0, 0 )
        
        
        bSizer5.Add( gSizer52, 0, 0, 5 )
        
        self.m_staticline21 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
        bSizer11.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )
        
        self.m_staticline16 = wx.StaticLine( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer5.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button15 = wx.Button( self.m_panel2, wx.ID_ANY, u"&Replace", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_button16 = wx.Button( self.m_panel2, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button16, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer4, 0, wx.ALIGN_RIGHT, 5 )
        
        
        self.m_panel2.SetSizer( bSizer5 )
        self.m_panel2.Layout()
        bSizer5.Fit( self.m_panel2 )
        bSizer3.Add( self.m_panel2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer3 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_dirPicker3.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnReadInputDirirectory )
        self.m_button4.Bind( wx.EVT_BUTTON, self.OnHelpClick )
        self.m_textCtrl91.Bind( wx.EVT_TEXT, self.OnFileNumber )
        self.m_button261.Bind( wx.EVT_BUTTON, self.OnReadXmlOneClick )
        self.m_filePicker7.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnReadOldExcel )
        self.m_textCtrl911.Bind( wx.EVT_TEXT, self.OnOldDataSheetName )
        self.m_filePicker71.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnReadNewExcel )
        self.m_textCtrl9111.Bind( wx.EVT_TEXT, self.OnNewDataSheetName )
        self.m_textCtrl4.Bind( wx.EVT_TEXT, self.OnPrintData )
        self.m_button15.Bind( wx.EVT_BUTTON, self.OnReplaceClick )
        self.m_button16.Bind( wx.EVT_BUTTON, self.OnExitClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnReadInputDirirectory( self, event ):
        event.Skip()
    
    def OnHelpClick( self, event ):
        event.Skip()
    
    def OnFileNumber( self, event ):
        event.Skip()
    
    def OnReadXmlOneClick( self, event ):
        event.Skip()
    
    def OnReadOldExcel( self, event ):
        event.Skip()
    
    def OnOldDataSheetName( self, event ):
        event.Skip()
    
    def OnReadNewExcel( self, event ):
        event.Skip()
    
    def OnNewDataSheetName( self, event ):
        event.Skip()
    
    def OnPrintData( self, event ):
        event.Skip()
    
    def OnReplaceClick( self, event ):
        event.Skip()
    
    def OnExitClick( self, event ):
        event.Skip()
    