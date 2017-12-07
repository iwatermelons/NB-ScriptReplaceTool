# -*- coding: UTF-8 -*-

import os
import time
import xlrd
import shutil
import re
import sys
from os.path import join


class Replace(object):
    
    def __init__(self, path,old_file_name,new_file_name,sheet_old,sheet_new):
        self.path = path
        #输入替换参数execl文件名称
        self.old_file_name = old_file_name
        self.new_file_name = new_file_name
        #sheet 原内容
        self.sheet_old = sheet_old
        #sheet 新内容
        self.sheet_new = sheet_new
    

    def dirirectory(self,path):

        #完善目录
        self.pathInput = join(path, 'input_xml')
        self.pathReplace = join(path,'replace_xml')
        self.pathOutput = join(path,'output_xml')

        #遍历目录是否存在，不存在新建，存在跳过
        for path_t in [self.pathInput,self.pathReplace,self.pathOutput]:

            #检验目录是否存在
            if os.path.exists(path_t) == False:

                os.mkdir(path_t)
                print 'Creation Dirirectory: %s' %path_t
            else:
                print 'Existence Dirirectory: %s' %path_t

        # return pathInput,pathReplace,pathOutput
    
    def index(self,input_file_one_name):
        #正则匹配出索引ID.
        index_id = re.search(r"\d{6}",input_file_one_name).group(0)
        # 返回索引ID
        return index_id
    
    
    def file_execl_show(self,f_path_file,sheet_change):
        # 检查Execl 输入数据是否存在
        if os.path.exists(f_path_file) == False:
            print "Execl 新旧数据，文件不存在"
            # 退出程序
            # sys.exit()
        # 打开execl 新旧数据文件  
        workbook = xlrd.open_workbook(r'%s' %(f_path_file))
        # 打开指定表格
        sheet = workbook.sheet_by_name(sheet_change)
        #统计表中行数
        nrows = sheet.nrows
        #统计表中列数
        global ncols
        ncols = sheet.ncols
        # 有效行数计算
        nrows_1 = nrows -2
        # 打印列表行列情况
        print 'Read sheet name : %s' %sheet_change
        print "行数：%s,  有效数据行数：%s  ，列数：%s" %(nrows,nrows_1, ncols)
    
    
    def coordinate(self,f_path_file, sheet_change, index_id):
        # 打开execl替换文件
        workbook = xlrd.open_workbook(r'%s' %(f_path_file))
    
        # 打开指定表格
        sheet = workbook.sheet_by_name(sheet_change)
        #统计表中行数
        nrows = sheet.nrows
    
        # 读 execl 表中 C列所有数据
        data = sheet.col_values(2)
        n = 0
        for n in range(2, nrows):
            # 替换浮点数类型
            if type(data[n]) == float:
                data[n] = int(data[n])
                data[n] = str(data[n])
            # 查找索引ID，位置值，所在行
            if data[n] == index_id:
                return n    
    
    
    def read_execl(self,f_path_file,sheet_change,row_id):
        #打开execl文件
        workbook = xlrd.open_workbook(r'%s' %(f_path_file))
        # 打开指定表格
        sheet = workbook.sheet_by_name(sheet_change)
        #获得索引所在，整行数据
        data = sheet.row_values(row_id)
        # 迭代出整行，所有值
        for n in range(ncols):
            # 替换浮点数类型
            if type(data[n]) == float:
                data[n] = int(data[n])
                data[n] = str(data[n])
        #返回索引所在，整行有效数据
        return data
    
    
    def replace_xml(self,input_file_one_name, data_old, data_new, replace_number):
    
        #把input目录原文件，复制到替换目录，并从新命名
        shutil.copyfile('%s//%s' %(self.pathInput,input_file_one_name), '%s//replace_0_%s' %(self.pathReplace, input_file_one_name)) 
        #数据位置，替换文件，变量初始值
        i = out_i = 0
        for i in range(ncols):
            #判断输入数据如果为空，跳过循环
            if data_old[i] == '':
                continue
            #如果替换前后数据相同，跳过循环
            if data_old[i] == data_new[i]:
                continue
                # break
            #打开替换目录文件
            template = open('%s//replace_%d_%s' %(self.pathReplace, out_i,input_file_one_name), 'r')
            #读取替换目录文件内容，整行读取
            data_xml = template.readlines()
            #替换文件名变值
            out_i = out_i + 1
            #打开新替换保存文件。
            output = open('%s//replace_%d_%s' %(self.pathReplace,out_i,input_file_one_name), 'w')
            
            #替换统计值， 旧数据在旧文件，新数据在旧文件，新数据在新文件，初始值
            j_old =  j_new_in_old  = j_new = 0
            #迭代每行内容
            for data_xml_line_old in data_xml:
                #统计旧数据在旧文件个数
                if data_old[i] in data_xml_line_old:
                    j_old = j_old + 1
                # 统计新数据在旧文件个数
                if data_new[i] in data_xml_line_old:
                    j_new_in_old = j_new_in_old  + 1
    
                #每行内容替换
                data_xml_line_new = data_xml_line_old.replace(data_old[i],data_new[i])
    
                #新数据在新文件个数
                if data_new[i] in data_xml_line_new:
                    j_new=j_new+1
                
                #写入替换文件保存
                output.write(data_xml_line_new)
            template.close()
            output.close()
    
            #计算替换次数
            j_t = j_new - j_new_in_old
            #设置替换完成情况
            if j_t == j_old:
                str_a = 'OK'
            else:
                str_a = 'ON'
            # 旧数据在就文件中，没有查找到，打印告警
            if j_old == 0:
                str_b = "***   请注意   ***"
                global warning_number
                # 打印告警次数
                warning_number = warning_number + 1
            else:
                str_b = ' '
    
            #打印每项新旧数据替换情况
            print "---------------------------------------------------------------"
            print "Old  data：%s in Old_file_xml, count : %d ;    %s" %(data_old[i], j_old, str_b)
            print 'New data：%s in New_file_xml, Replace : %d;   %s' %( data_new[i], j_t, str_a)
            #print 'New data %s  in Old_file_xml, count : %d ;   New data %s in New_file_xml, count: %d ;   Replace : %d ;    %s' %( data_new[i], j_new_in_old,data_new[i], j_new, j_t, str_a)
    
        #把替换完的文件，保存到output目录
        shutil.copyfile('%s//replace_%d_%s' %(self.pathReplace,out_i,input_file_one_name), '%s//update_%s' %(self.pathOutput, input_file_one_name)) 
    
        #记录替换文件个数
        # global replace_number 
        replace_number = replace_number + 1
        return replace_number