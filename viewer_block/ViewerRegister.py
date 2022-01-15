# -*- coding: UTF-8 -*-
from viewer_block.ViewerSimpleFactory import ViewerSimpleFactory
from level_block.LevelObserverInterface import LevelObserverInterface
from tag_block.TagObserverInterface import TagObserverInterface
import copy
class ViewerRegister(LevelObserverInterface,TagObserverInterface):
    viewers = []
    levels = {}
    tags = {}
    viewer_simple_factory = None

    def __init__(self):
        self.viewer_simple_factory = ViewerSimpleFactory()

    def levelUpdate(self, levels):
        #TODO:
        self.levels = copy.deepcopy(levels)
        print(levels)
        self.notifyViewers()
        pass

    def tagUpdate(self, tags: dict):
        #TODO:
        self.tags = copy.deepcopy(tags)
        self.notifyViewers()
        pass

    def notifyViewers(self):
        for viewer in self.viewers:
            viewer.update(self.tags, self.levels)
            pass

    def createViewer(self,type):
        viewer = self.viewer_simple_factory.createViewer(type)
        self.viewers.append(viewer)
        return viewer
        