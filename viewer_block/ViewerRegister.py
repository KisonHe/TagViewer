# -*- coding: UTF-8 -*-
from viewer_block.ViewerSimpleFactory import ViewerSimpleFactory
from level_block.LevelObserverInterface import LevelObserverInterface
from tag_block.TagObserverInterface import TagObserverInterface
import copy
class ViewerRegister(LevelObserverInterface,TagObserverInterface):
    viewers = []
    level = {}
    tags = {}
    viewer_simple_factory = None

    def __init__(self):
        self.viewer_simple_factory = ViewerSimpleFactory()

    def levelUpdate(self, levels):
        #TODO:
        self.level = copy.deepcopy(levels)
        pass

    def tagUpdate(self, data: dict):
        #TODO:
        self.tags = copy.deepcopy(data)
        pass

    def createViewer(self,type):
        viewer = self.viewer_simple_factory(type)
        return viewer
        