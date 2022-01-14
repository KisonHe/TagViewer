# -*- coding: UTF-8 -*-
from Tag import Status
from TagSubjectInterface import TagSubjectInterface
from TagObserverInterface import TagObserverInterface

class TagRegister(TagSubjectInterface):
    tags = {}

    def setupUi(self, parent):
        # TODO
        pass

    def __init__(self) -> None:
        pass

    # Called by tag's click callback, to update info in the register
    def tagChange(self, name, status):
        self.tags[name] = status

    def notifyTagObserver(self):
        pass

    def registerTagObserver(self, o: TagObserverInterface):
        pass

    def removeTagObserver(self, o: TagObserverInterface):
        pass