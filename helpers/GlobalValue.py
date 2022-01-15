# -*- coding: UTF-8 -*-

class GlobalValue:
    # python class var is a different thing
    g_excel_data = None

    def __init__(self):
        pass

    @staticmethod
    def setExcelData(excel_data):
        GlobalValue.g_excel_data = excel_data

    @staticmethod
    def getExcelData():
        return GlobalValue.g_excel_data