# -*- coding: UTF-8 -*-
from viewer_block.ViewerInterface import ViewerInterface

class WordViewer(ViewerInterface):
    levels = {}
    tags = {}
    def __init__(self):
        pass

    def update(self,tags,levels):
        self.tags = copy.deepcopy(tags)
        self.levels = copy.deepcopy(levels)
        self.display()

    def display(self):
        # add your code here

        # add your code end
        pass


