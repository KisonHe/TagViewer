# -*- coding: UTF-8 -*-
from viewer_block.ViewerSimpleFactory import ViewerSimpleFactory

class ViewerRegister:
    viewer_simple_factory = None

    def __init__(self):
        self.viewer_simple_factory = ViewerSimpleFactory()

    def createViewer(self,type):
        viewer = self.viewer_simple_factory(type)
        return viewer