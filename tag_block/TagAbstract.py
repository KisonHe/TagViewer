class TagAbstract:
    register = None
    ui_instance = None
    def updateUi(self):
        raise RuntimeError

    def setupUi(self, parent):
        raise RuntimeError

    def __init__(self) -> None:
        pass

    def onTagChanged(self):
        raise RuntimeError
