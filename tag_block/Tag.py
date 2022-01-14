# -*- coding: UTF-8 -*-
from enum import Enum
from PyQt5 import QtWidgets
from design.UiInstance import PyqtUiInstance
from design.colorDesign import tag_colors


# tag的可能的status
class TagStatus(Enum):
    # Must Start from 0 and add one by one
    # Because func getNext
    NONE = 0
    MAIN_TAG_ONLY = 1
    EXTRA_TAG_ONLY = 2
    BOTH_TAGS = 3

    def getNext(self):
        tmp = (self.value + 1) % len(TagStatus)
        return TagStatus(tmp)

    def getHintString(self):
        return ["Tag未生效", "只算Main", "只算Extra", "两个都算"][self.value]


class Tag:
    register = None
    ui_instance = None
    status = TagStatus.NONE

    # colors = ["#9D849A","#A9B0BC","#90A3B9","#637081"]
    def updateUi(self):
        tmp = "border-radius: 3px;" + "background-color : " + tag_colors[self.status.value]
        self.ui_instance.setStyleSheet(tmp)
        self.ui_instance.setToolTip(self.status.getHintString())

    def setupUi(self, parent):
        # TODO
        parent.addWidget(self.ui_instance)
        self.updateUi()
        pass

    def __init__(self, name, register) -> None:
        # We want to have many choices, here should we use factory?
        # answer by jack: I think no
        self.name = name
        self.ui_instance = QtWidgets.QPushButton(name)
        self.ui_instance.clicked.connect(self.onTagCliecked)
        self.register = register
        self.register.tagChange(self.name, self.status)
        pass

    def onTagCliecked(self):
        self.status = self.status.getNext()
        self.updateUi()
        self.register.tagChange(self.name, self.status)
