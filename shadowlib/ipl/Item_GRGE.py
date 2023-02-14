class Item_GRGE:
    def init(self, gameType):
        self.lowLeftPos = None
        self.lineX = 0
        self.lineY = 0
        self.topRightPos = None
        self.doorType = 0
        self.garageType = 0
        self.hash = 0
        self.name = None
        self.unknown = 0

    def read(self, line):
        pass

    def read(self, rf):
        pass

    def read(self, rf, hashTable):
        self.lowLeftPos = rf.readVector3D()
        self.lineX = rf.readFloat()
        self.lineY = rf.readFloat()
        self.topRightPos = rf.readVector3D()
        self.doorType = rf.readInt()
        self.garageType = rf.readInt()
        tempHash = rf.readUnsignedInt()
        self.name = str(tempHash)
        self.hash = int(tempHash)
        self.name = hashTable[tempHash]
        self.unknown = rf.readInt()

    def display(self):
        print("LowLeftPos: " + str(self.lowLeftPos.x) + ", " + str(self.lowLeftPos.y) + ", " + str(self.lowLeftPos.z))
        print("Line x: " + str(self.lineX) + " y: " + str(self.lineY))
        print("TopRightPos: " + str(self.topRightPos.x) + ", " + str(self.topRightPos.y) + ", " + str(self.topRightPos.z))
        print("Doortype: " + str(self.doorType))
        print("Garagetype: " + str(self.garageType))
        print("Hash: " + str(self.hash) + " name: " + str(self.name))
        print("Unknown: " + str(self.unknown))

    def write(self, wf):
        wf.write(self.lowLeftPos)
        wf.write(self.lineX)
        wf.write(self.lineY)
        wf.write(self.topRightPos)
        wf.write(self.doorType)
        wf.write(self.garageType)
        wf.write(self.hash)
        wf.write(self.unknown)
        self.display()