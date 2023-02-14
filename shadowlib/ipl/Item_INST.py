class Item_INST:
    def init(self, gameType):
        self.gameType = gameType
        self.id = 0
        self.name = None
        self.hash = 0
        self.interior = 0
        self.position = [0.0, 0.0, 0.0]
        self.scale = [0.0, 0.0, 0.0]
        self.rotation = [0.0, 0.0, 0.0, 1.0]
        self.lod = 0
        self.unknown1 = 0
        self.unknown2 = 0
        self.unknown3 = 0.0
        self.drawDistance = 300.0
        self.axisAngle = [0.0, 0.0, 0.0, 0.0]
        self.hidden = False
        self.selected = False
        self.glListID = 0

    def read(self, line):
        line = line.replace(" ", "")
        split = line.split(",")

        if self.gameType == "GTA_SA":
            self.id = int(split[0])
            self.name = split[1]
            self.interior = int(split[2])
            self.position = [float(split[3]), float(split[4]), float(split[5])]
            self.rotation = [float(split[6]), float(split[7]), float(split[8]), float(split[9])]
            self.lod = int(split[10])
        elif self.gameType == "GTA_VC":
            self.id = int(split[0])
            self.name = split[1]
            self.interior = int(split[2])
            self.position = [float(split[3]), float(split[4]), float(split[5])]
            self.scale = [float(split[6]), float(split[7]), float(split[8])]
            self.rotation = [float(split[9]), float(split[10]), float(split[11]), float(split[12])]
        elif self.gameType == "GTA_III":
            self.id = int(split[0])
            self.name = split[1]
            self.position = [float(split[2]), float(split[3]), float(split[4])]
            self.scale = [float(split[5]), float(split[6]), float(split[7])]
            self.rotation = [float(split[8]), float(split[9]), float(split[10]), float(split[11])]
        else:
            raise ValueError("Unsupported GameType {}".format(self.gameType))

        self.axisAngle = self.rotation.axisAngle
        self.display()

    def read(self, rf, hashTable):
        self.position = rf.readVector3D()
        self.rotation = rf.readVector4D()
        temp_hash = rf.readUnsignedInt()
        self.name = str(temp_hash)
        self.hash = int(temp_hash)
        self.name = hashTable.get(temp_hash, None)
        if self.name is None:
            self.name = "HASH({})".format(temp_hash)
            print("ERROR Hash does not exist '{}'".format(temp_hash))

        self.unknown1 = rf.readInt()
        self.lod = rf.readInt()
        self.unknown2 = rf.readInt()
        self.unknown3 = rf.readFloat()
        self.display()

    def display(self):
        if self.gameType != "GTA_IV":
            print("Name: {}".format(self.name))
        if self.gameType in ["GTA_VC", "GTA_SA"]:
            print("Position: {}, {}, {}".format(self.position[0], self.position[1], self.position[2]))
        if self.gameType in ["GTA_III", "GTA_VC"]:
            print("Rotation: {}, {}, {}, {}".format(self.rotation[0], self.rotation[1], self.rotation[2], self.rotation[3]))
        print("Lod: {}".format(self.lod))

    def write(self, wf):
        wf.write(self.position)
        wf.write(self.rotation)
        if self.hash == 0:
            self.hash = int(getHashKey(self.name))
        wf.write(self.hash)
        wf.write(self.unknown1)
        wf.write(self.lod)
        wf.write(self.unknown2)
        wf.write(self.unknown3)
        self.display()
