# -*- coding: UTF-8 -*-
import copy
from level_block.LevelObserverInterface import LevelObserverInterface
from tag_block.TagObserverInterface import TagObserverInterface

class StatisticsPanel(LevelObserverInterface,TagObserverInterface):
    tags = {}
    levels = {}

    def __init__(self):
        pass

    def tagUpdate(self, tags:dict):
        self.tags = copy.deepcopy(tags)
        display()

    def levelUpdate(self, levels):
        self.levels = copy.deepcopy(levels)
        dispaly()


    def display(self):
        pass