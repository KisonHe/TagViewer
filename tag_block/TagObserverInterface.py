# -*- coding: UTF-8 -*-
class TagObserverInterface:
    def __init__(self):
        pass

    def tagUpdate(self, tags:dict):
        # 虚函数，不应该到这里
        raise RuntimeError
