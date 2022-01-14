# -*- coding: UTF-8 -*-
from viewer_block.ViewerInterface import ViewerInterface
import copy
class WordViewer(ViewerInterface):
    ui_instance = None
    levels = {}
    tags = {}
    def __init__(self):
        pass

    def update(self,tags,levels):
        self.tags = copy.deepcopy(tags)
        self.levels = copy.deepcopy(levels)
        
        self.display({"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","tag2"],["摩托车","飙车"]]]})

    def display(self, data:dict):
        # add your code here
        for level in data: # data {"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","tag2"],["摩托车","飙车"]]]}
            # TODO:Print level here
            for pare in data[level]: # data[level] [[['线下', '刺激'], ['过山车', '飙车']], [['线下', 'tag2'], ['摩托车', '飙车']]]
                # pare[0] ['线下', '刺激']
                # pare[1] ["过山车","飙车"]
                for tag in pare[0]:
                    print(tag,end=" ")
                pass
            print(": ",end="")
        self.ui_instance.setText("")

        # add your code end
        pass
    def setUiInstance(self,ui):
        self.ui_instance = ui

