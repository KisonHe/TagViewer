# -*- coding: UTF-8 -*-
from enum import Enum
from PyQt5 import QtWidgets

class LevelStatus(Enum):
    # Must Start from 0 and add one by one
    # Because func getNext
    OFF = 0
    ON = 1

    def getNext(self):
        tmp = (self.value + 1) % len(LevelStatus)
        return LevelStatus(tmp)

    def getHintString(self):
        return ["不显示", "显示"][self.value]
