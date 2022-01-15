# -*- coding: UTF-8 -*-

import sys
from PyQt5 import QtWidgets, uic, QtCore
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtCore import Qt
import pandas
from tag_block.UiTag import UiTag
import xlrd
from tag_block.TagRegister import TagRegister
from tag_block.SimpleTagRegister import SimpleTagRegister
from level_block.LevelRegister import LevelRegister
from level_block.SimpleLevelRegister import SimpleLevelRegister
from viewer_block.ViewerRegister import ViewerRegister
from helpers.GlobalValue import GlobalValue
# Set True to ignore ! starting Tags
ignoreExclamationMark = True


def extractTagFromString(string: str, ifIgnoreExclamationMark: bool) -> list:
    ret = []
    if isinstance(string, str):
        # 去掉空格
        string = string.replace(" ", "")
        ret = string.split("#")
        # 处理!开头的Tag
        for index in range(len(ret)):
            if (ret[index].startswith("!")):
                if (ifIgnoreExclamationMark):
                    # 忽略!，把整个string变成"",在下面删掉
                    ret[index] = ""
                else:
                    ret[index] = ret[index].replace("!", "")
        # 去掉 ''
        ret = list(filter(None, ret))
    else:
        raise ValueError
    return ret


def readExcelData():
    ## This works
    # GlobalValue.setExcelData(pandas.read_excel('./data.xls', engine='xlrd'))
    # excel_data = GlobalValue.getExcelData()

    # This too
    GlobalValue.g_excel_data = pandas.read_excel('./data.xls', engine='xlrd')
    excel_data = GlobalValue.g_excel_data

    # 提取Tags
    Tags = {}
    # TODO:这里词典的排序，是考虑ExtraTag,还是不考虑，还是都留着？以{"TAG":[tagNum,extraTagNum]}的方式存着？
    for string in list(excel_data["TAG"]) + list(excel_data["ExtraTag"]):
        if isinstance(string, str):
            tmp_list = extractTagFromString(string, ignoreExclamationMark)
            for item in tmp_list:
                if (item in Tags.keys()):
                    Tags[str(item)] = Tags[str(item)] + 1
                else:
                    Tags[str(item)] = 1
    pass

# class MainWindow(QtWidgets.QMainWindow):

#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setObjectName("MainWindow")
#         self.resize(800, 600)
#         self.setWindowTitle("My Awesome App")
#         self.centralwidget = QtWidgets.QWidget(self)
#         self.centralwidget.setObjectName("centralwidget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.setCentralWidget(self.centralwidget)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


if (__name__ == "__main__"):
    readExcelData()
    level_register = SimpleLevelRegister()

    # main_tag_register = TagRegister()
    # main_tag_register.registerTagObserver(level_register)

    main_tag_register = SimpleTagRegister()
    main_tag_register.registerTagObserver(level_register)
    

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    viewer_register = ViewerRegister()
    word_viewer = viewer_register.createViewer("word")
    word_viewer.setUiInstance(window.textBrowser)

    level_register.setUiInstance(window.levelLineEdit)
    level_register.registerLevelObserver(viewer_register)
    main_tag_register.registerTagObserver(viewer_register)

    main_tag_register.setUiInstance(window.tagLineEdit)
    window.tagLineEdit.textChanged.connect(main_tag_register.onTagChange)
    window.levelLineEdit.textChanged.connect(level_register.onLevelTextChange)

    tag_list = []
    # for i in range(4):
    #     mainTag = Tag("Tag",main_tag_register)
    #     mainTag.setupUi(window.horizontalLayout)
    #     tag_list.append(mainTag)
    #     pass

    # mainTag = uiTag("Tag", main_tag_register)
    # mainTag.setupUi(window.horizontalLayout)

    # secondTag = uiTag("secondTag", main_tag_register)
    # secondTag.setupUi(window.horizontalLayout)

    # thirdTag = uiTag("thirdTag", main_tag_register)
    # thirdTag.setupUi(window.horizontalLayout)

    # output = QtWidgets.QTextBrowser()
    # window.horizontalLayout.addWidget(output)

    # output.setText("we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n"
    #                "we are world \n")

    window.resize(800, 600)
    app.exec()
