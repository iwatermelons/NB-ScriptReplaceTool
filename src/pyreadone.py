# -*- coding:utf-8 -*-

import os
import sys
import time
import re
import xlrd
import xlwt
from os.path import join
from xlutils.copy import copy
from lxml import etree


reload(sys)
sys.setdefaultencoding('utf8')

class OsOperation(object):

    def __init__(self,path,local_dir,sheet_locale_input):

        print os.getcwd()
        #输入替换参数目录
        self.path = path
        #读取完成，输出excel的目录
        self.local_dir = local_dir
        #sheet 新内容
        self.sheet_locale_input = sheet_locale_input

    def dirirectory(self):
    
        #完善目录
        # self.path1 = '%s//input_xml' %self.path
        self.path1 = join(self.path,'input_xml')
        self.path3 = join(self.path,self.local_dir)
        
        #检验目录是否存在
        for path_t in [self.path1,self.path3]:
            if os.path.exists(path_t) == False:
                os.mkdir(path_t)
                print 'Creation Dirirectory: %s' %path_t
            else:
                print 'Existence Dirirectory: %s' %path_t
        # return path1, path3
    


class Excel(object):

    def creation(self,path3, sheet_locale_input,file_count,date):
        # 设置excel文件名称
        creation_excel_name = '%s_Read_%d-NB_xml.xls' %(date,file_count)
        # 设置新建excel文件绝对路径
        path_excel_name = join(path3,creation_excel_name)
        # 新建excel文件
        workbook = xlwt.Workbook(path_excel_name)
        # 设置新建execl文件，sheet名称
        sheet = workbook.add_sheet(u'%s' %sheet_locale_input, cell_overwrite_ok = True)
        #定义表标题
        data = ['RNC ID', '3G ID', '$sbtsid', '$MMEipAddrPrim',  '$MMEipAddrSec', '$MMEipAddrThird', '$MMEipAddrFourth',  '$LTEcpupvlanid',  '$Wcpupvlanid',    '$LTECPUPIPaddress',   '$WCPUPIPaddress', '$omvlanid',   '$OMIPaddress',    '$gateway1',   '$gateway2',   '$gateway3',   '$destIpAddr3',    '$destIpAddr4',    '$destIpAddr5',    '$destIpAddr6',    '$destIpAddr7',   '$ICSUIPaddress',  '$ntpServers', '$sctpPortMin', 'NB_version']
        row = 2
        n = 0
        #循环写入首行，表标题
        for n in range(len(data)):
            sheet.write(1,n,u'%s' %data[n])
            n = n+1
        # 保存 文件
        workbook.save(path_excel_name)
        # 返回新建excel表绝对路径，和excel名称
        return path_excel_name,creation_excel_name
      



    def write(self,path_excel_name, sheet_locale_input , row, data):
        
        #打开 execl 表文件
        workbook = xlrd.open_workbook(path_excel_name)
    
        #use xlutils.copy to copy the xlrd.Book object into an xlwt.Workbook object:
        workbooknew = copy(workbook)
    
        #获取所有Sheet名称
        sheet_names = workbook.sheet_names()
        #获得操作表的 sheet ID
        sheet_number = sheet_names.index(sheet_locale_input)
        #通过 sheet ID 打开 写入sheet
        sheet = workbooknew.get_sheet(sheet_number)
        #留出表头
        row = row + 2
        #写入数据
        n = 0
        for n in range(len(data)):
            sheet.write(row,n,u'%s' %data[n])
        
        #保存文件
        workbooknew.save(path_excel_name)
        #workbooknew.save('%s//%s' %(path,f_name))
        

class Read(object):
    def index(self, input_file_one_name):
        #正则匹配出索引ID.
        self.index_id = re.search(r"\d{6}",input_file_one_name).group(0)
        # 返回索引ID
        return self.index_id
    
    
    def read_one_file_xml(self, path1,input_file_one_name):
        xml = open('%s//%s' %(path1, input_file_one_name), 'r')
        data_xml = xml.read()
        
        html = etree.HTML(data_xml)
    
        data = range(24)
       
    
        # RNCID = html.xpath('//*[class="BTSSCW"]/*[@name="identifier"]/text()')
        RNC_ID = html.xpath('//*[@name="identifier"]/text()')
        print RNC_ID
        if RNC_ID == []:
            data[0] = ''
        else:
            data[0] = RNC_ID[1]
        #3G ID空
        data[1] = ''
    
        NB_ID = html.xpath('//@distName')
        print NB_ID
        # global index_id
        data[2] = self.index_id
    
        MME_IP = html.xpath('//*[@name="ipAddrPrim"]/text()')
        print MME_IP
    
        data[3] = MME_IP[0]
        data[4] = MME_IP[1]
        data[5] = MME_IP[2]
        #MME 4 IP,空值
        data[6] = ''
    
        VLAN_ID = html.xpath('//*[@name="vlanId"]/text()')
        print VLAN_ID
    
        data[7] = VLAN_ID[0]
        data[11] = VLAN_ID[1]
        if  len(VLAN_ID) == 2 :
            data[8] = ''
        else:
            data[8] = VLAN_ID[2]
    
        LTE_W_3_IP = html.xpath('//*[@name="localIpAddr"]/text()')
        print LTE_W_3_IP
    
        data[9] = LTE_W_3_IP[0]
        data[12] = LTE_W_3_IP[1]
        if  len(LTE_W_3_IP) == 2 :
            data[10] = ''
        else:
            data[10] = LTE_W_3_IP[2]
    
        GW_3_IP = html.xpath('//*[@name="gateway"]/text()')
        print GW_3_IP
    
        data[13] = GW_3_IP[0]
        data[14] = GW_3_IP[1]
        if  len(GW_3_IP) == 2 :
            data[15] = ''
        else:
            data[15] = GW_3_IP[2]
    
        Route_3_IP = html.xpath('//*[@name="destIpAddr"]/text()')
        print Route_3_IP
    
        if  len(Route_3_IP) == 2 :
            data[16] = ''
        else:
            data[16] = Route_3_IP[2]
    
        #无值，暂设为空
        data[17] = data[18] = data[19] = data[20] = '' 
    
        RNC_sctp_ip = html.xpath('//*[@name="sctpFarEndSubnetIpAddress"]/text()')
        print RNC_sctp_ip
    
        if RNC_sctp_ip == []:
            data[21] = ''
        else:
            data[21] = RNC_sctp_ip[0]
        
        NTP_IP = html.xpath('//*[@name="ntpServerIp"]/text()')
        print NTP_IP
    
        data[22] = NTP_IP[0]
    
        RNC_sctp_port = html.xpath('//*[@name="sctpPortMin"]/text()')
        print RNC_sctp_port
    
        if RNC_sctp_port == []:
            data[23] = ''
        else:
            data[23] = RNC_sctp_port [0]
    
        # ID = html.xpath('//*[@class="IPRT" and @distName')
        # IP = html.xpath('//*[@class="IPRT"]/list/item[1]/p[3]/text()')
        return data