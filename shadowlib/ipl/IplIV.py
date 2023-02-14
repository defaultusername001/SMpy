class IplIV:
    def __init__(self, hash_table):
        self.hashTable = hash_table

    def loadPlacement(self, wpl, printName):
        print("Loading.. bin wpl", printName)
        if wpl.rf is None:
            rf = ReadFunctions(wpl.fileName)
        else:
            wpl.isStream = True
            rf = wpl.rf

        version = rf.readInt() # always 3
        instanceCount = rf.readInt() # Number of instances
        unused1 = rf.readInt() # unused
        garageCount = rf.readInt() # number of garages
        carCount = rf.readInt() # number of cars
        cullCount = rf.readInt() # number of culls
        unused2 = rf.readInt() # unused
        unused3 = rf.readInt() # unused
        unused4 = rf.readInt() # unused
        strBigCount = rf.readInt() # number of strbig
        lodCullCount = rf.readInt() # number of lod cull
        zoneCount = rf.readInt() # number of zones
        unused5 = rf.readInt() # unused
        unused6 = rf.readInt() # unused
        unused7 = rf.readInt() # unused
        unused8 = rf.readInt() # unused
        blokCount = rf.readInt() # number of bloks

        for i in range(instanceCount):
            item = Item_INST(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsInst.append(item)
        for i in range(garageCount):
            item = Item_GRGE(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsGrge.append(item)
        for i in range(carCount):
            item = Item_CARS(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsCars.append(item)
        for i in range(cullCount):
            item = Item_CULL(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsCull.append(item)
        for i in range(strBigCount):
            item = Item_STRBIG(wpl.gameType)
            item.read(rf)
            wpl.itemsStrBig.append(item)
        for i in range(lodCullCount):
            item = Item_LCUL(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsLCul.append(item)
        for i in range(zoneCount):
            item = Item_ZONE(wpl.gameType)
            item.read(rf, self.hashTable)
            wpl.itemsZone.append(item)
        for i in range(blokCount):
            item = Item_BLOK(wpl.gameType)
            item.read(rf, hashTable)
            wpl.itemsBlok.append(item)
        if wpl.rf is None:
            rf.closeFile()
        wpl.loaded = True


def writeHeader(wf, wpl):
    wf.write(3)
    wf.write(len(wpl.itemsInst))
    wf.write(0)
    wf.write(len(wpl.itemsGrge))
    wf.write(len(wpl.itemsCars))
    wf.write(len(wpl.itemsCull))
    wf.write(0)
    wf.write(0)
    wf.write(0)
    wf.write(len(wpl.itemsStrBig))
    wf.write(len(wpl.itemsLCul))
    wf.write(len(wpl.itemsZone))
    wf.write(0)
    wf.write(0)
    wf.write(0)
    wf.write(0)
    wf.write(len(wpl.itemsBlok))

def save(self, wpl):
    if wpl.isStream:
        fileName = wpl.img.fileName
    else:
        fileName = wpl.fileName
    wf = WriteFunctions(fileName)
    if wpl.isStream:
        print("Saving Stream WPL")
        wf.gotoEnd()
        wpl.imgItem.offset = wf.fileSize
    writeHeader(wf, wpl)
    for item in wpl.itemsInst:
        item.write(wf)
    for item in wpl.itemsGrge:
        item.write(wf)
    for item in wpl.itemsCars:
        item.write(wf)
    if wpl.isStream:
        wpl.imgItem.size = wf.fileSize - wpl.imgItem.offset
        wpl.img.setSaveRequired()
    wf.closeFile()
