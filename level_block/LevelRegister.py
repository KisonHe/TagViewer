# -*- coding: UTF-8 -*-
import copy
from level_block.LevelObserverInterface import LevelObserverInterface
from level_block.LevelSubjectInterface import LevelSubjectInterface
from tag_block.TagObserverInterface import TagObserverInterface
from helpers.GlobalValue import GlobalValue
import logging


log = logging.getLogger('LevelRegister')
log.setLevel(logging.ERROR)

class LevelRegister(LevelSubjectInterface,TagObserverInterface):
    tags = {}
    subscribers = []

    def __init__(self):
        super().__init__()

    # Called by level button's click callback, to update info in the register
    def levelChange(self):
        #TODO:
        self.notifyLevelObserver()
        pass

    def tagUpdate(self, tags:dict):
        self.tags = copy.deepcopy(tags)
        # TODO:Replace to real Update
        log.info("Got info of" + str(tags))

    def notifyLevelObserver(self):
        for o in self.subscribers:
            o.levelUpdate(None)
            # TODO:Replace None to Levels

    def removeLevelObserver(self, o: LevelObserverInterface):
        self.subscribers.remove(o)

    def registerLevelObserver(self, o: LevelObserverInterface):
        self.subscribers.append(o)
