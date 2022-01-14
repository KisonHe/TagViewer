# -*- coding: UTF-8 -*-
from viewer_block.WordViewer import WordViewer
from viewer_block.GraphViewer import GraphViewer
import logging

log = logging.getLogger('ViewerSimpleFactory')
log.setLevel(logging.INFO)
class ViewerSimpleFactory:

    def __init__(self) -> None:
        pass

    def createViewer(self, type):
        if type == "word":
            log.info("Create viewer: word viewer!")
            return WordViewer()
        elif type == "graph":
            log.info("Create viewer: graph viewer!")
            return GraphViewer()
        else:
            log.info("Create viewer: illegal type!")
            return WordViewer()