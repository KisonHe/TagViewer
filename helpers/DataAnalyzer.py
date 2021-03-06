# -*- coding: UTF-8 -*-

from helpers.GlobalValue import GlobalValue
from level_block.Level import LevelStatus
from tag_block.UiTag import TagStatus
from helpers.helpers import extractTagFromString
import logging


class FreeDictKey:

    def __init__(self):
        self.key = {}

    def addElement(self,element: str):
        self.key.append(element)

    def __getitem__(self, index):
        pass

    def  __setitem__(self, key, value):
        pass



class FreeDictValue:

    def __init__(self):
        self.value = []

    def addElement(self,element: str):
        self.value.append(element)

class FreeDict:

    def __init__(self):
        self.keys = []
        self.values = []
        self.key_value = []

    def getKeyValue(self):
        for i in range(0,len(self.keys)):
            key = self.keys[i]
            projects = self.values[i]
            tags = []
            for tag in key.keys():
                tags.append(tag)
            element = []
            element.append(tags)
            element.append(projects)
            self.key_value.append(element)
        return self.key_value

    def addKey(self, tags, subset):
        for set in subset:
            free_dict_key = {}
            for element in set:
                free_dict_key[element] = tags[element]
            self.keys.append(free_dict_key)
            self.values.append([])

    def setValue(self):
        excel_data = GlobalValue.g_excel_data
        projects = excel_data[GlobalValue.g_project_list]
        line = 0
        for project in projects:
            for i in range(0,len(self.keys)):
                free_dict_key = self.keys[i]
                condition = False
                for key,value in free_dict_key.items():
                    judge_tags = []
                    if value == TagStatus.MAIN_TAG_ONLY:
                       judge_tags = judge_tags + extractTagFromString(excel_data.loc[line,GlobalValue.g_main_tag],GlobalValue.g_ignore_exclamation_mark)
                    if value == TagStatus.EXTRA_TAG_ONLY:
                        judge_tags = judge_tags + extractTagFromString(excel_data.loc[line, GlobalValue.g_extra_tag],GlobalValue.g_ignore_exclamation_mark)
                    if value == TagStatus.BOTH_TAGS:
                        judge_tags = judge_tags + extractTagFromString(excel_data.loc[line, GlobalValue.g_main_tag],
                                                                       GlobalValue.g_ignore_exclamation_mark)
                        judge_tags = judge_tags + extractTagFromString(excel_data.loc[line, GlobalValue.g_extra_tag],
                                                                       GlobalValue.g_ignore_exclamation_mark)
                    for tag in judge_tags:
                        if tag == key:
                            condition = True
                        else:
                            condition = False
                if condition == True:
                    self.values[i].append(project)
                    condition = False
            line += 1


class DataAnalyzer:
    
    def __init__(self):
        self.viewer_data = {}
        pass

    def setViewerData(self, tags, levels):
        # set level
        for key in levels.keys():
            if levels[key] == LevelStatus.ON:
                self.viewer_data[key] = FreeDict()

        for key, value in self.viewer_data.items():
            value.addKey(tags,self.writeViewerData(tags, int(key)))
            value.setValue()

    def writeViewerData(self, tags, level_value):
        tag_array = []
        for tag in tags.keys():
            tag_array.append(tag)
        subset = self.getTagSubset(tag_array,level_value)
        return subset



    def getTagSubset(self, tags, level):
        result = []
        if level <= 0:
            return result

        if len(tags) < level:
            return result

        for i in range(0,len(tags)-level+1):
            a = [tags[i]]
            returns = self.getTagSubset(tags[i+1:] ,level-1)
            if len(returns) == 0:
                result.append(a)
            else:
                for array in returns:
                    b = a + array
                    result.append(b)
        return result


    def getViewerData(self):
        return self.viewer_data


# example:

# viewer_data stores all the data needed for visualization and it's a normal dict
# viewer_data : {levelx : FreeDict , levelx : FreeDict , ...}

# FreeDict is a custom data structure that like normal dict to store the mapping between tags and projects
# FreeDict : {FreeDictKey : FreeDictValue , FreeDictKey : FreeDictValue , ...}

# FreeDictKey is a custom data structure that like string array to store the subset of the set of tag
# FreeDictValue is a custom data structure that like string array to store the subset of the set of project
# FreeDictKey : {"tag1" : status ,"tag2" : status ,...}
# FreeDictValue : ["project1" , "project2", ...]
