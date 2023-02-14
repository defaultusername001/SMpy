class Ipl:
    def __init__(self, fileName=None, hashTable=None, gameType=None, autoLoad=False):
        self.rf = None
        self.fileName = fileName
        self.gameType = gameType
        self.changed = False
        self.loaded = False
        self.selected = False
        self.itemsLoaded = False
        self.isStream = False
        self.img = None
        self.imgItem = None
        self.lodWPL = -1
        self.itemsAuzo = []
        self.itemsCars = []
        self.itemsCull = []
        self.itemsEnex = []
        self.itemsGrge = []
        self.itemsInst = []
        self.itemsJump = []
        self.itemsMult = []
        self.itemsOccl = []
        self.itemsPath = []
        self.itemsPick = []
        self.itemsTCyc = []
        self.itemsStrBig = []
        self.itemsLCul = []
        self.itemsZone = []
        self.itemsBlok = []
        self.printName = None
        print("Started loading: " + self.fileName)
        if autoLoad:
            self.loadPlacement(hashTable)

    def __init__(self, rf=None, hashTable=None, gameType=None, autoLoad=False, img=None, imgItem=None, printName=None):
        self.rf = rf
        self.gameType = gameType
        self.img = img
        self.imgItem = imgItem
        self.printName = printName
        if autoLoad:
            self.loadPlacement(hashTable)

    def loadPlacement(self, hashTable):
        if self.gameType == GameType.GTA_IV:
            if "common" in self.fileName:
                IplIII().loadPlacement(self)
            else:
                IplIV(hashTable).loadPlacement(self, self.printName)
        else:
            IplIII().loadPlacement(self)

    def save(self, hashTable):
        if self.gameType == GameType.GTA_IV:
            if "common" in self.fileName:
                IplIII().save(self)
            else:
                IplIV(hashTable).save(self)
        else:
            IplIII().save(self)
