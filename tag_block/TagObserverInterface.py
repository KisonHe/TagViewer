# -*- coding: UTF-8 -*-
class TagObserverInterface:
    def __init__(self):
        pass

    def tagUpdate(self):
        # 虚函数，不应该到这里
        raise RuntimeError