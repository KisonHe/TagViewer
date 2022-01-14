# -*- coding: UTF-8 -*-

import sys
from types import prepare_class
from PyQt5 import QtWidgets, uic
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt
import pandas
from tag import tag
import xlrd

# Set True to ignore ! starting Tags
ignoreExclamationMark = True

def extractTagFromString(string:str,ifIgnoreExclamationMark:bool)->list:
    ret = []
    if isinstance(string, str):
        # 去掉空格
        string = string.replace(" ","")
        ret = string.split("#")
        # 处理!开头的Tag
        for index in range(len(ret)): 
            if (ret[index].startswith("!")):
                if (ignoreExclamationMark):
                    # 忽略!，把整个string变成"",在下面删掉
                    ret[index] = ""
                else:
                    ret[index] = ret[index].replace("!","")
        # 去掉 ''
        ret = list(filter(None, ret))
    else: 
        raise ValueError
    return ret

def readExcelData():
    excelData = pandas.read_excel('./data.xls',engine='xlrd')
    # 提取Tags
    Tags = {}
    # TODO:这里词典的排序，是考虑ExtraTag,还是不考虑，还是都留着？以{"TAG":[tagNum,extraTagNum]}的方式存着？
    for string in list(excelData["TAG"]) + list(excelData["ExtraTag"]):
        if isinstance(string, str):
            tmp_list = extractTagFromString(string,ignoreExclamationMark)
            for item in tmp_list:
                if (item in Tags.keys()):
                    Tags[str(item)] = Tags[str(item)] + 1
                else:
                    Tags[str(item)] = 1
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setWindowTitle("My Awesome App")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setCentralWidget(self.centralwidget)


# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, *args, obj=None, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setupUi(self)


if (__name__ == "__main__"):
    readExcelData()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    tag_list = []
    for i in range(4):
        mainTag = tag("Tag",None)
        mainTag.setupUi(window.horizontalLayout)
        tag_list.append(mainTag)
        pass
    window.resize(800,600)
    app.exec()
