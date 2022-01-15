# -*- coding: UTF-8 -*-

from helpers.GlobalValue import GlobalValue
from level_block.Level import LevelStatus


class FreeDictKey:

    def __init__(self):
        self.key = []

    def addElement(self,element: str):
        self.key.append(element)



class FreeDictValue:

    def __init__(self):
        self.value = []

    def addElement(self,element: str):
        self.value.append(element)

class FreeDict:

    def __init__(self):
        self.keys = []
        self.values = []

    def addKey(self, key :FreeDictKey):
        self.keys.append(key)
        pass

    def addValue(self, value :FreeDictValue):
        self.values.append(value)
        pass




class DataAnalyzer:
    
    def __init__(self):
        self.viewer_data = {}
        pass

    def setViewerData(self, tags, levels):
        # set level
        for key in levels.keys():
            if levels[key] == LevelStatus.ON:
                self.viewer_data[key] = FreeDict()

        for key, value in self.viewer_data:
            self.writeViewerData(tags, int(key), value)

    def writeViewerData(self, tags, level_value, array_dict: FreeDict):
        tags = self.getTagSubset()
        pass

    def getTagSubset(self, tags: dict, level):
        array = []
        if level <= 0:
            return None

        if len(tags.keys()) < level:
            return None

        for tag in tags.keys():
            array.append(tag)



    def getViewerData(self):
        return self.viewer_data


# example:

# viewer_data stores all the data needed for visualization and it's a normal dict
# viewer_data : {levelx : FreeDict , levelx : FreeDict , ...}

# FreeDict is a custom data structure that like normal dict to store the mapping between tags and projects
# FreeDict : {FreeDictKey : FreeDictValue , FreeDictKey : FreeDictValue , ...}

# FreeDictKey is a custom data structure that like string array to store the subset of the set of tag
# FreeDictValue is a custom data structure that like string array to store the subset of the set of project
# FreeDictKey : ["tag1" , "tag2", ...]
# FreeDictValue : ["project1" , "project2", ...]
