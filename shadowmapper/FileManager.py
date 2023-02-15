from threading import Thread

class FileManager(Thread):
    def __init__(self):
        super().__init__() #should super be used here?, never used it before but I think the application is right for a file manager.
        self.hashTable = HashTable(OneAtATimeHasher())
        self.statusCallbacks = None
        self.gtaDat = None
        self.ipls = []
        self.ides = []
        self.imgs = []
        self.waters = []
        self.modelIPL = DefaultListModel()
        self.modelIDE = DefaultListModel()
        self.modelIPLItems = DefaultListModel()
        self.modelIDEItems = DefaultListModel()
        self.modelVehicles = DefaultComboBoxModel()
        self.selType = -1
        self.selParam1 = -1
        self.selParam2 = -1
        self.key = None
        self.gameDir = None
        self.gameType = None

    @property
    def gamePath(self):
        return Path(self.gameDir)

    def startLoading(self, statusCallbacks, install, key):
        self.statusCallbacks = statusCallbacks
        self.gameDir = install.path
        self.gameType = install.gameType
        self.key = key
        self.start()

    def setInstall(self, install):
        self.gameDir = install.path
        self.gameType = install.gameType

    imgWPLCount = sum(map(lambda img: img.getItemOfTypeCount(".wpl"), imgs))

    if self.statusCallbacks is not None:
        self.statusCallbacks.onStartLoadingWpl(imgWPLCount)

    for img in imgs:
        rf = ReadFunctions(img.path)
        for wplEntry in img.getItemsOfType(".wpl"):
            rf.seek(wplEntry.offset)
            ipl = Ipl(rf, self.hashTable, self.gameType!!, True, img, wplEntry, wplEntry.name)
            ipl.fileName = wplEntry.name
            self.ipls.append(ipl)

            if self.statusCallbacks is not None:
                self.statusCallbacks.onLoadingStatusChanged("<WPL> {}".format(wplEntry.name))
                self.modelIPL.addElement(wplEntry.name)
                self.statusCallbacks.onLoadingValueIncreased()

        rf.closeFile()

    if self.statusCallbacks is not None:
        self.statusCallbacks.onLoadingFinished()


    def addHashes(self, ide):
        for item in ide.itemObjs:
            self.hashTable.add(item.modelName)
        for item in ide.itemTobj:
            self.hashTable.add(item.modelName)
        for item in ide.itemCars:
            self.hashTable.add(item.modelName)
        for item in ide.itemAnim:
            self.hashTable.add(item.modelName)
        for item in ide.item2dfx:
            self.hashTable.add(item.name)
        for item in ide.itemTAnm:
            self.hashTable.add(item.modelName)


    def loadHashesFromIni(self):
        hashesIni = IniEditor()
        try:
            hashesIni.load("hashes.ini")
            for hash, value in hashesIni.getSectionMap("cars").items():
                self.hashTable.add(int(hash), value)
            for hash, value in hashesIni.getSectionMap("hashes").items():
                self.hashTable.add(int(hash), value)
        except Exception as e:
            raise RuntimeError(e)


    def save(self):
        if self.gtaDat is not None and self.gtaDat.changed:
            print("Saving gta.dat")
            self.gtaDat.save()
        for ide in self.ides:
            if ide.isSaveRequired:
                ide.save()
                ide.setSaveRequired(False)
                print(f"Saving ide {ide.fileName}")
        for ipl in self.ipls:
            if ipl.changed:
                ipl.save(self.hashTable)
                ipl.changed = False
                print(f"Saving ipl {ipl.fileName}")
        for img in self.imgs:
            if img.isSaveRequired:
                img.save()
                img.setSaveRequired(False)


    def getSaveModel(self):
        saveModel = DefaultListModel()
        if self.gtaDat is not None and self.gtaDat.changed:
            saveModel.addElement("gta.dat")
        for ide in self.ides:
            if ide.isSaveRequired:
                saveModel.addElement(ide.fileName)
        for ipl in self.ipls:
            if ipl.changed:
                saveModel.addElement(ipl.fileName)
        for img in self.imgs:
            if img.isSaveRequired:
                saveModel.addElement(img.fileName)
        return saveModel


    def addIPLItem(self, name, iplID, pos):
        iplItem = Item_INST(self.gameType)
        iplItem.name = name
        iplItem.interior = 0
        iplItem.lod = -1
        iplItem.position.x = pos.x
        iplItem.position.y = 0 - pos.z
        iplItem.position.z = pos.y
        self.ipls[iplID].itemsInst.append(iplItem)
        self.ipls[iplID].changed = True
        self.modelIPLItems.addElement(name)

    def addIDEItem(tmp, ideID):
        ides[ideID].itemObjs.append(tmp)
        ides[ideID].setSaveRequired()
        modelIDEItems.addElement(tmp.modelName)
        return len(ides[ideID].itemObjs) - 1


    def updateIDEItemList(ideID, type):
        modelIDEItems.clear()
        if type == 0:
            for item in ides[ideID].itemObjs:
                modelIDEItems.addElement(item.modelName)


    def updateIPLItemList(iplID, type):
        modelIPLItems.clear()
        if type == 0:
            for item in ipls[iplID].itemsInst:
                modelIPLItems.addElement(item.name)
        elif type == 1:
            for item in ipls[iplID].itemsGrge:
                modelIPLItems.addElement(item.name)
        elif type == 2:
            for item in ipls[iplID].itemsCars:
                if item.name != "":
                    modelIPLItems.addElement(item.name)
                else:
                    modelIPLItems.addElement("Random")
        elif type == 3:
            for item in ipls[iplID].itemsCull:
                modelIPLItems.addElement(item.name)
        elif type == 4:
            for item in ipls[iplID].itemsStrBig:
                modelIPLItems.addElement(item.modelName)
        elif type == 5:
            for item in ipls[iplID].itemsLCul:
                modelIPLItems.addElement(item.name1)
        elif type == 6:
            for item in ipls[iplID].itemsZone:
                modelIPLItems.addElement(str(item))
        elif type == 7:
            for item in ipls[iplID].itemsBlok:
                modelIPLItems.addElement(str(item))
    
    def addNewIDE(file):
        if file is not None:
            if file.exists():
                JOptionPane.showMessageDialog(None, "File already exists")
            else:
                ide = IDE(file.absolutePath, gameType, True)
                ide.setSaveRequired()
                ides.append(ide)
                modelIDE.addElement(file.name)

    def addNewIPL(file):
        if file is not None:
            if file.exists():
                JOptionPane.showMessageDialog(None, "File already exists")
            else:
                ipl = Ipl(file.absolutePath, hashTable, gameType, False)
                ipl.changed = True
                ipls.append(ipl)

                modelIPL.addElement(file.name)
                fixedIplPath = file.path.lower().replace(gameDir.lower(), "")
                gtaDat.ipl.append(fixedIplPath)
                gtaDat.changed = True

    def setSelection(selType, selParam1, selParam2):
        if self.selType != -1:
            if self.selType == PickingType.map:
                ipls[self.selParam1].itemsInst[self.selParam2].selected = False
            elif self.selType == PickingType.water:
                waters[0].planes[self.selParam1].selected = False
            elif self.selType == PickingType.car:
                ipls[self.selParam1].itemsCars[self.selParam2].selected = False
            else:
                print("--Something went wrong--")
                print(f"SelType: {selType}")
                print(f"SelParam1: {selParam1}")
                print(f"SelParam2: {selParam2}")
        self.selType = selType
        self.selParam1 = selParam1
        self.selParam2 = selParam2
        if self.selType != -1:
            if selType == PickingType.map:
                ipls[selParam1].itemsInst[selParam2].selected = True
            elif selType == PickingType.water:
                waters[0].planes[selParam1].selected = True
            elif selType == PickingType.car:
                ipls[selParam1].itemsCars[selParam2].selected = True
            else:
                print("--Something went wrong--")
                print(f"SelType: {selType}")
                print(f"SelParam1: {selParam1}")
                print(f"SelParam2: {selParam2}")
    def loadWaterTexture() -> TextureDic:
    # TODO: Fix this
    # return TextureDic(f"{gameDir}/pc/textures/water.wtd", None, GameType.GTA_IV, 23655)
        pass

    def addNewImg(path: Path) -> CommandResult:
        if not path.startswith(gamePath):
            return CommandResult.Failed("IMG should be inside the games folder")

        imgs.add(Img.createNewImg(path))

        return CommandResult.Success

    class LoadingStatusCallbacks:
        def onStartLoadingWpl(self, wplCount: int):
            pass
        def onStartLoading(self, fileCount: int):
            pass
        def onLoadingStatusChanged(self, status: str):
            pass
        def onLoadingValueIncreased(self):
            pass
        def onLoadingFinished(self):
            pass

    def run():
        startLoading()
