# -*- coding: UTF-8 -*-

class GlobalValue:
    # python class var is a different thing
    g_excel_data = None
    g_ignore_exclamation_mark = False
    g_main_tag = "TAG"
    g_extra_tag = "ExtraTag"
    g_project_list = "娱乐项目"

    def __init__(self):
        pass

    @staticmethod
    def setExcelData(excel_data):
        GlobalValue.g_excel_data = excel_data

    @staticmethod
    def getExcelData():
        return GlobalValue.g_excel_data
