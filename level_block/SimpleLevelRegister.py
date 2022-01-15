# -*- coding: UTF-8 -*-
import copy
from level_block.Level import LevelStatus
from level_block.LevelObserverInterface import LevelObserverInterface
from level_block.LevelSubjectInterface import LevelSubjectInterface
from tag_block.TagObserverInterface import TagObserverInterface
from helpers.GlobalValue import GlobalValue
import logging


log = logging.getLogger('SimpleLevelRegister')
log.setLevel(logging.ERROR)

class SimpleLevelRegister(LevelSubjectInterface,TagObserverInterface):
    

    def __init__(self):
        super().__init__()

        self.tags = {}
        self.levels = {}
        self.subscribers = []
        self.c_config = {"max_level":6,"min_level":1} #should be const

        # self.excel_data = GlobalValue.getExcelData()
        # print(excel_data.iloc[1, 4])
        

    # Called by level button's click callback, to update info in the register
    def levelChange(self, level, status):
        self.levels[str(level)] = status
        self.notifyLevelObserver()
        pass
    def setUiInstance(self, ui):
        self.ui_instance = ui

    def onLevelTextChange(self,text:str):
        on_level_map = []
        levels = {}
        hasError = False
        if not (len(text) > 0):
            # avoid crash when user delete all chars
            return
        if self.ui_instance == None:
            raise "Need to call setUiInstance first"
        strlist = text.split()
        for strlevel in strlist:
            try:
                level = int(strlevel)
                if (level > self.c_config["max_level"]) or (level < self.c_config["min_level"]):
                    hasError = True
                    continue
                # self.levelChange(str(level),LevelStatus.ON)
                on_level_map.append(level)
                levels[strlevel] = LevelStatus.ON
            except:
                hasError = True
                continue
        if hasError:
            self.ui_instance.setStyleSheet("background-color : red")
        else:
            self.ui_instance.setStyleSheet("background-color : white")
        for i in range(self.c_config["min_level"], self.c_config["max_level"] + 1):
            if not i in on_level_map:
                # self.levelChange(str(i),LevelStatus.OFF)
                levels[str(i)] = LevelStatus.OFF
        self.levels = levels
        self.notifyLevelObserver()

    def tagUpdate(self, tags:dict):
        #Simple tag register doesn't care about tag change
        pass

    def notifyLevelObserver(self):
        for o in self.subscribers:
            o.levelUpdate(self.levels)

    def removeLevelObserver(self, o: LevelObserverInterface):
        self.subscribers.remove(o)

    def registerLevelObserver(self, o: LevelObserverInterface):
        self.subscribers.append(o)
