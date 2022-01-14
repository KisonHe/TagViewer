# -*- coding: UTF-8 -*-
from tag_block.Tag import Status
from tag_block.TagSubjectInterface import TagSubjectInterface
from tag_block.TagObserverInterface import TagObserverInterface


class TagRegister(TagSubjectInterface):
    tags = {}
    subscribers = []

    def setupUi(self, parent):
        # TODO
        pass

    def __init__(self) -> None:
        pass

    # Called by tag's click callback, to update info in the register
    def tagChange(self, name, status):
        self.tags[name] = status
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
