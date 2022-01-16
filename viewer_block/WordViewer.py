# -*- coding: UTF-8 -*-
from viewer_block.ViewerInterface import ViewerInterface
from helpers.DataAnalyzer import *
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
        # test data struct
        analyzer = DataAnalyzer()
        analyzer.setViewerData(tags,levels)
        self.display(analyzer.viewer_data)
        #display({"1":[[["线下"],["过山车","飙车","线下的其他projects"]],[["搞笑"],["摩托车","飙车","搞笑的其他projects"]]],"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","搞笑"],["摩托车","飙车"]]]})

    def display(self, data:dict):
        # add your code here
        text = ""
        for level in data: # data {"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","tag2"],["摩托车","飙车"]]]}
            # TODO:Print level here
            text = text + "lv" + level + ": \n"
            # add by jack
            search_data = data[level].getKeyValue()
            for pare in search_data: # data[level] [[['线下', '刺激'], ['过山车', '飙车']], [['线下', 'tag2'], ['摩托车', '飙车']]]
                # pare[0] ['线下', '刺激']
                # pare[1] ["过山车","飙车"]
                for tag in pare[0]:
                    text = text + tag + ", "
                text = text[:len(text)-2] # remove last ", "
                text = text + " : "
                for project in pare[1]:
                    text = text + project + "、"
                text = text[:len(text)-1] # remove last "、"
                text = text + "\n"
            text = text + "-"*20 + "\n"

            # text = text + "\n"
        self.ui_instance.setText(text)

        # add your code end
        pass
    def setUiInstance(self,ui):
        self.ui_instance = ui

#  {"1":[[["线下"],["过山车","飙车","线下的其他projects"],[["搞笑"],["摩托车","飙车","搞笑的其他projects"]]],"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","搞笑"],["摩托车","飙车"]]]}
#  {"1":[[],[],[[["线下"],["过山车","飙车","线下的其他projects"]]],[["搞笑"],["摩托车","飙车","搞笑的其他projects"]]],"2":[[["线下","刺激"],["过山车","飙车"]],[["线下","搞笑"],["摩托车","飙车"]]]}