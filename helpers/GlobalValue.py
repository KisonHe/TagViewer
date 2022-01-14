# -*- coding: UTF-8 -*-

class GlobalValue:
    g_excel_data = None

    def __init__(self):
        pass

    def setExcelData(excel_data):
        GlobalValue.g_excel_data = excel_data

    def getExcelData(self):
        return self.g_excel_data