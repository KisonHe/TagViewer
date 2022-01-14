# -*- coding: UTF-8 -*-
from Tag import Status
class TagRegister:
    tags = {}
    def setupUi(self, parent):
        # TODO
        pass
    def __init__(self) -> None:
        pass

    def tagUpdate(self, name, status):
        self.tags[name] = status
