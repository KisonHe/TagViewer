# -*- coding: UTF-8 -*-

class ViewerInterface:
    def display(self):
        # 虚函数，不应该到这里
        raise RuntimeError