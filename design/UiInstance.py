
class UiInstanceAbstract:
    def setupUi(self):
        pass
    def changeBackGroundColor(self):
        pass
    def updateUi(self):
        pass
    def __init__(self) -> None:
        pass

class PyqtUiInstance(UiInstanceAbstract):
    instance = None
    def setupUi():
        pass
    def changeBackGroundColor(self, color:str):
        tmp = "background-color : " + color
        self.instance.setStyleSheet(tmp)
        pass
    def __init__(self) -> None:
        super().__init__()
        