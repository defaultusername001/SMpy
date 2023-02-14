class ImgItem:
    def __init__(self, name: str):
        self.name = name
        self.type = 0
        self.offset = 0
        self.size = 0
        self.isResource = False
        self.flags = 0

    @property
    def nameWithoutExtension(self):
        return self.name.split(".")[0]

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if type < 1000:
            self.isResource = True
        self._type = type
