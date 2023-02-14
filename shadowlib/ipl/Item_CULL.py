class Item_CULL:
    def init(self, gameType):
        self.gameType = gameType
        self.posLowerLeft = None
        self.posUpperRight = None
        self.unk1 = 0
        self.unk2 = 0
        self.unk3 = 0
        self.unk4 = 0
        self.hash = 0
        self.name = None

    def read(self, line):
        pass

    def read(self, rf):
        self.posLowerLeft = rf.readVector3D()
        self.posUpperRight = rf.readVector3D()
        self.unk1 = rf.readInt()
        self.unk2 = rf.readInt()
        self.unk3 = rf.readInt()
        self.unk4 = rf.readInt()
        self.hash = rf.readInt()

    def display(self):
        print("Position: " + self.posLowerLeft.x + ", " + self.posLowerLeft.y + ", " + self.posLowerLeft.z)
        print("Rotation: " + self.posUpperRight.x + ", " + self.posUpperRight.y + ", " + self.posUpperRight.z)
        print("Hash: " + str(self.hash))
        print("Unknown1: " + str(self.unk1))
        print("Unknown2: " + str(self.unk2))
        print("Unknown3: " + str(self.unk3))
        print("Unknown4: " + str(self.unk4))
        print("Name: " + str(self.name))

    def read(self, rf, hashTable):
        self.posLowerLeft = rf.readVector3D()
        self.posUpperRight = rf.readVector3D()
        self.unk1 = rf.readInt()
        self.unk2 = rf.readInt()
        self.unk3 = rf.readInt()
        self.unk4 = rf.readInt()
        tempHash = rf.readUnsignedInt()
        self.name = str(tempHash)
        self.hash = int(tempHash)
        self.name = hashTable[tempHash]
        self.display()
