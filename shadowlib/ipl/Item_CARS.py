class Item_CARS:
    def __init__(self, gameType):
        self.gameType = gameType
        self.selected = False
        self.position = Vector3D()
        self.rotation = Vector3D()
        self.hash = 0
        self.name = None
        self.unknown1 = 0
        self.unknown2 = 0
        self.unknown3 = 0
        self.unknown4 = 0
        self.unknown5 = 0
        self.unknown6 = 0
        self.unknown7 = 0
        self.type = 0
        
    def read(self, line):
        pass
        
    def read(self, rf):
        raise NotImplementedError("Not supported yet.")
        
    def read(self, rf, hashTable):
        self.position = rf.readVector3D()
        self.rotation = rf.readVector3D()
        temp_hash = rf.readUnsignedInt()
        self.name = str(temp_hash)
        self.hash = int(temp_hash)
        self.unknown1 = rf.readInt()
        self.unknown2 = rf.readInt()
        self.unknown3 = rf.readInt()
        self.unknown4 = rf.readInt()
        self.unknown5 = rf.readInt()
        self.unknown6 = rf.readInt()
        self.unknown7 = rf.readInt()
        
    def display(self):
        print("--CAR--")
        print("Position: {}, {}, {}".format(self.position.x, self.position.y, self.position.z))
        print("Rotation: {}, {}, {}".format(self.rotation.x, self.rotation.y, self.rotation.z))
        print("Hash: {} name: {}".format(self.hash, self.name))
        print("Unknown1: {}".format(self.unknown1))
        print("Unknown2: {}".format(self.unknown2))
        print("Unknown3: {}".format(self.unknown3))
        print("Unknown4: {}".format(self.unknown4))
        print("Unknown5: {}".format(self.unknown5))
        print("Unknown6: {}".format(self.unknown6))
        print("Unknown7: {}".format(self.unknown7))
        
    def write(self, wf):
        wf.write(self.position)
        wf.write(self.rotation)
        wf.write(self.hash)
        wf.write(self.unknown1)
        wf.write(self.unknown2)
        wf.write(self.unknown3)
        wf.write(self.unknown4)
        wf.write(self.unknown5)
        wf.write(self.unknown6)
        wf.write(self.unknown7)