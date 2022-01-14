# -*- coding: UTF-8 -*-
from TagObserverInterface import TagObserverInterface


class TagSubjectInterface:
    def registerTagObserver(self, o: TagObserverInterface):
        # 虚函数，不应该到这里
        raise RuntimeError

    def removeTagObserver(self, o: TagObserverInterface):
        # 虚函数，不应该到这里
        raise RuntimeError

    def notifyTagObserver(self):
        # 虚函数，不应该到这里
        raise RuntimeError
