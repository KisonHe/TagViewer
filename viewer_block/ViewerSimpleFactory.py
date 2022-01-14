# -*- coding: UTF-8 -*-
from viewer_block.WordViewer import WordViewer

class ViewerSimpleFactory:

    def __init__(self) -> None:
        pass

    def createViewer(self, type):
        if type == "word":
            return WordViewer()
        elif typr == "graph":
            return GraphViewer()
        else:
            return WordViewer()