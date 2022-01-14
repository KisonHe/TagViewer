# -*- coding: UTF-8 -*-

class ViewerInterface:
    def updateInfo(self):
        pass

    def display(self, data:dict):
        # 虚函数，不应该到这里
        raise RuntimeError