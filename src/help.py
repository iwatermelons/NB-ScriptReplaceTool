# -*- coding:utf-8 -*-

class HelpText(object):
    def __init__(self):
        self.help='''Replace Tool v1.0
        使用说明：
            1. 请选择，数据操作目录。
            2. 自动创建Input目录，请复制需要替换的txt，xml文件进入目录。
            3. 读取Input目录文件信息，需要的数据创建excel保存在locale_Read_NBs_data目录。
            4. 选择替换旧(新)数据excel文件，及对应旧(新)sheet.
            5. 替换数据。
        功能流程：
            1. 只读取：  1 ->2 -> 3
            2. 只替换：  1 ->2 -> 4 ->5
            3. 读取+替换：  1 ->2 ->3 -> 4 ->5
        '''
        print self. help