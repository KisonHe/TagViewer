# -*- coding: UTF-8 -*-
from level_block.LevelObserverInterface import LevelObserverInterface

class LevelSubjectInterface:
    def __init__(self):
        pass

    def registerLevelObserver(self, o: LevelObserverInterface):
        # 虚函数，不应该到这里
        raise RuntimeError

    def removeLevelObserver(self, o: LevelObserverInterface):
        # 虚函数，不应该到这里
        raise RuntimeError

    def notifyLevelObserver(self):
        # 虚函数，不应该到这里
        raise RuntimeError
