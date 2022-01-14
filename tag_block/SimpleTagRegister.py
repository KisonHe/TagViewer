# -*- coding: UTF-8 -*-
import imp
from posixpath import split
from sys import implementation
from tag_block.TagSubjectInterface import TagSubjectInterface
from tag_block.TagObserverInterface import TagObserverInterface
from helpers.helpers import extractTagFromString
from tag_block.UiTag import TagStatus
class SimpleTagRegister(TagSubjectInterface):
    tags = {}
    subscribers = []
    ui_instance = None

    def setupUi(self, parent):
        # TODO
        pass

    def __init__(self) -> None:
        pass
    def setUiInstance(self,ui):
        self.ui_instance = ui

    # Called by tag's click callback, to update info in the register
    # Works like this: "线上:main 刺激：both 释放情绪：extra"
    def onTagChange(self, text:str):
        if not (len(text) > 0):
            return
        if self.ui_instance == None:
            raise "Need to call setUiInstance first"
        status = ["","main","extra","both"]
        self.tags = {}
        hasError = False
        text = text.replace("：",":")
        strlist = text.split()
        for pares in strlist:
            parelist = pares.split(":")
            if len(parelist) != 2:
                hasError = True
                continue
            if (not parelist[1] in status) or (len(parelist[1]) < 1) or (len(parelist[0]) < 1):
                hasError = True
                continue
            self.tags[parelist[0]] = TagStatus(status.index(parelist[1]))
        if hasError:
            self.ui_instance.setStyleSheet("background-color : red")
        else:
            self.ui_instance.setStyleSheet("background-color : white")
            
            
        # self.tags[name] = status
        # tags = extractTagFromString(text,False)
        self.notifyTagObserver()

    def notifyTagObserver(self):
        for o in self.subscribers:
            o.tagUpdate(self.tags)
        pass

    def registerTagObserver(self, o: TagObserverInterface):
        self.subscribers.append(o)
        pass

    def removeTagObserver(self, o: TagObserverInterface):
        self.subscribers.remove(o)
        pass

