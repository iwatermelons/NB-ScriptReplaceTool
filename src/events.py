# -*- coding:utf-8 -*-

import pywx
import os
import sys
import time
import wx
import shutil
import pyreadone as pyrm
import pyreplace
import src.help as help



# sys.stdout sys.stderr重定向类
class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out=aWxTextCtrl
 
    def write(self,string):
        self.out.WriteText(string)
        # wx.CallAfter(self.out.WriteText, string)



class MyFrame2 ( pywx.MyFrame1 ):

    def __init__(self, parent):
        pywx.MyFrame1.__init__( self, parent )
        self.local_dir = 'locale_Read_NBs_data'
        self.sheet_locale_input = 'locale_input'

        # redirect text here
        redir=RedirectText(self.m_textCtrl4)
        #输出流重定向
        sys.stdout=redir
        # 错误流重定向
        sys.stderr=redir

  
    # Virtual event handlers, overide them in your derived class
    def OnReadInputDirirectory( self, event ):
        self.path = self.m_dirPicker3.GetPath()
        # print type(path)
        print self.path
        event.Skip()

    def OnHelpClick( self, event ):
        help.HelpText()

        event.Skip()
    
    def OnFileNumber( self, event ):
        # Clear(0)
        event.Skip()
    
    def OnReadXmlOneClick( self, event ):
        print  "######################################################"
        #调用dirirectory函数，操作目录
        pyoo = pyrm.OsOperation(self.path,self.local_dir,self.sheet_locale_input)
        pyoo.dirirectory()
        # path1, path3 = pyr.dirirectory(path, local_dir)
        print '============================='
        #切换输入数据目录
        os.chdir(pyoo.path1)
        print os.getcwd()
        #获得输入数据目录下，所有文件名称
        input_file_all_name =  os.listdir(pyoo.path1)
        #统计文件个数
        file_count = len(input_file_all_name)
        #打印文件名
        print '输入目录共计: %d 个文件。' %file_count

        file_count_str = str(file_count)
        self.m_textCtrl91.SetValue(file_count_str)

        
        #输入目录无文件退出程序
        # if file_count == 0:
            # sys.exit()
        
        # 打印 出所有文件名称
        # print '%d个文件名： %s' %(file_count, input_file_all_name)
    
        excel = pyrm.Excel()
        
        date =  time.strftime("%Y%m%d_%H-%M-%S", time.localtime())
        # 调用函数，新建output基站数据，excel文件。  返回excel文件绝对路径，和文件名称
        path_excel_name, creation_excel_name= excel.creation(pyoo.path3, self.sheet_locale_input, file_count, date)
    
        print '------------------------------------------------'
        # self.m_textCtrl4.AppendText('创建 NB Data excel文件 :' + str(path_excel_name) + '\r')
        print '创建 NB Data excel文件 : %s' %path_excel_name

    
    
        file_number = replace_number = warning_number = execl_locale_row =0
    
        for input_file_one_name in input_file_all_name:
        
            file_number = file_number + 1
            print  "***************************************************************************"
            print  '读取第%s个文件' %file_number
            print  "***************************************************************************"
    
            #打印当前操作文件名
            print "当前读取文件：%s" %input_file_one_name
            pyr = pyrm.Read()
            #获取文件名中的,索引ID.
            index_id = pyr.index(input_file_one_name)
            print "当前文件读取 Index ID: %s"  %index_id
    
            print '======================================='
            data = pyr.read_one_file_xml(pyoo.path1, input_file_one_name)
            print data
    
            #调用函数，把数据写入execl表中
            print path_excel_name
            excel.write(path_excel_name, self.sheet_locale_input, execl_locale_row, data)
            #写入execl表，行控制
            execl_locale_row = execl_locale_row +1
            print '======================================='
            print "读取写入数据： %s  完成" %index_id
        print '======================================='
        print "读取共写入：%d  个数据。" %file_number + '\r'

    
    def OnReadOldExcel( self, event ):
        self.pathOldExcel = self.m_filePicker7.GetPath()
        print self.pathOldExcel

        self.OldSheet = self.m_textCtrl911.GetValue()
        print self.OldSheet + '\r'

        # self.NewSheet
        event.Skip()
    
    def OnOldDataSheetName( self, event ):
        self.OldSheet = self.m_textCtrl911.GetValue()
        print self.OldSheet
        event.Skip()
    
    def OnReadNewExcel( self, event ):
        self.pathNewExcel = self.m_filePicker71.GetPath()
        print self.pathNewExcel

        self.NewSheet = self.m_textCtrl9111.GetValue()
        print self.NewSheet + '\r'

        event.Skip()
    
    def OnNewDataSheetName( self, event ):
        self.NewSheet = self.m_textCtrl9111.GetValue()
        print self.NewSheet
        event.Skip()
    
    def OnPrintData( self, event ):
        event.Skip()
    
    def OnReplaceClick( self, event ):

        print  "######################################################"
        replace = pyreplace.Replace(self.path, self.pathOldExcel, self.pathNewExcel,self.OldSheet, self.NewSheet)

        #调用dirirectory函数，操作目录
        print self.path
        replace.dirirectory(self.path)
        print '======================================='
        #切换输入数据目录
        os.chdir(replace.pathInput)
        # os.chdir(pathInput)
        print os.getcwd()
        #获得输入数据目录下，所有文件名称
        input_file_all_name =  os.listdir(replace.pathInput)
        #统计文件个数
        file_count = len(input_file_all_name)
        #打印文件名
        print '输入目录共计: %d 个文件。' %file_count
        
        # 打印 出所有文件名称
        # print '%d个文件名： %s' %(file_count, input_file_all_name)
        
        #调用函数，打印execl 文件 情况
        replace.file_execl_show(self.pathOldExcel, self.OldSheet,)
        replace.file_execl_show(self.pathNewExcel, self.NewSheet)
        
        file_number = replace_number = warning_number =0
        #遍历循环，获取每个文件，进行操作
        for input_file_one_name in input_file_all_name:
            
            file_number = file_number + 1
            print  "***************************************************************************"
            print  "替换第%s个文件" %file_number
            print  "***************************************************************************"
        
            #打印当前操作文件名
            print "当前替换文件：%s" %input_file_one_name
            #获取文件名中的,索引ID.
            index_id = replace.index(input_file_one_name)
            print "当前文件替换 Index ID: %s"  %index_id
            print '======================================='
        
            #调用坐标函数，读取execl文件，获得索引数据行数。
            old_row_id = replace.coordinate(self.pathOldExcel, self.OldSheet, index_id)
            new_row_id = replace.coordinate(self.pathNewExcel, self.NewSheet, index_id)
        
            #查找不到行数，返回Node值，结束循环
            if old_row_id == None:
                print '------------------------------------------------'
                print "文件索引%s ，Execl sheel %s 无数据。" %(index_id, self.OldSheet)
                continue
            if new_row_id == None:
                print '------------------------------------------------'
                print "文件索引%s ，Execl sheel %s 无数据。" %(index_id, self.NewSheet)   
                continue
        
            #打印索引所在行数
            print "Data index: %s, execl sheel 'Old' 坐标为: C%d" %(index_id, old_row_id)
            print "Data index: %s, execl sheel 'New' 坐标为: C%d" %(index_id, new_row_id)
            print '======================================='
        
            #调入read_execl函数; 读取execl，原sheet内容
            data_old = replace.read_execl(self.pathOldExcel, self.OldSheet, old_row_id)    
            #调入read_execl函数; 读取execl，新sheet内容
            data_new = replace.read_execl(self.pathNewExcel, self.NewSheet, new_row_id)
        
            #打印  旧，新数据值
            print "Old  data: %s" %data_old
            print "New data: %s" %data_new
        
            #判断新旧数据是否相同，相同跳出循环
            if data_old == data_new:
                print "----------------------------"
                print "新旧数据相同，无需替换"
                continue
        
            #调用函数进行xml文件替换
            replace_number = replace.replace_xml(input_file_one_name, data_old,data_new, replace_number)
            
        #删除替换目录
        shutil.rmtree(replace.pathReplace) 
        
        #end
        
        #打印统计值
        print  "#################################################################################################"
        print  "共计： %d 个文件  。  替换 ： %d 个文件 。   告警次数 ： %d" %(file_number, replace_number, warning_number)
        print  "#################################################################################################"  + '\r'
    
        event.Skip()
    

    def OnExitClick( self, event ):
        print "exit"
        self.Close(True)
        event.Skip()