# -*- coding: UTF-8 -*-

import sys
from PyQt5 import QtWidgets, uic, QtCore
from Ui_MainWindow import Ui_MainWindow
import pandas
from tag_block.UiTag import UiTag
from tag_block.TagRegister import TagRegister
from tag_block.SimpleTagRegister import SimpleTagRegister
from level_block.LevelRegister import LevelRegister
from level_block.SimpleLevelRegister import SimpleLevelRegister
from viewer_block.ViewerRegister import ViewerRegister
from helpers.GlobalValue import GlobalValue
from helpers.helpers import extractTagFromString
# Set True to ignore ! starting Tags
ignoreExclamationMark = True

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

    window.resize(800, 600)
    app.exec()
