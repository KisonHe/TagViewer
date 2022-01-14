# -*- coding: UTF-8 -*-
from viewer_block import *

class ViewerSimpleFactory:

    def __init__(self) -> None:
        pass

    def createViewer(self, type):
        if type == "word":
            print("Create viewer: word viewer!")
            return WordViewer()
        elif type == "graph":
            print("Create viewer: graph viewer!")
            return GraphViewer()
        else:
            print("Create viewer: illegal type!")
            return WordViewer()