# -*- coding: UTF-8 -*-

from helpers.GlobalValue import GlobalValue

class DataAnalyzer:
    viewer_data = {}

    def __init__(self):
        pass

    def setViewerData(self,tags,levels):
        # set level
        for key in levels:
            self.viewer_data[key] = None


    def getViewerData(self):
        return self.viewer_data