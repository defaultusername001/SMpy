class Item_LCUL:
    def __init__(self, gameType: str):
        self.gameType = gameType
        self.posLowerLeft = None
        self.posUpperRight = None
        self.unk1 = 0
        self.hash1 = 0
        self.hash2 = 0
        self.hash3 = 0
        self.hash4 = 0
        self.hash5 = 0
        self.hash6 = 0
        self.hash7 = 0
        self.hash8 = 0
        self.hash9 = 0
        self.hash10 = 0
        self.name1 = None
        self.name2 = None
        self.name3 = None
        self.name4 = None
        self.name5 = None
        self.name6 = None
        self.name7 = None
        self.name8 = None
        self.name9 = None
        self.name10 = None

    def read(self, rf: object, hashTable: dict = None):
        self.posLowerLeft = rf.readVector3D()
        self.posUpperRight = rf.readVector3D()
        self.unk1 = rf.readInt()
        self.hash1 = rf.readUnsignedInt()
        self.hash2 = rf.readUnsignedInt()
        self.hash3 = rf.readUnsignedInt()
        self.hash4 = rf.readUnsignedInt()
        self.hash5 = rf.readUnsignedInt()
        self.hash6 = rf.readUnsignedInt()
        self.hash7 = rf.readUnsignedInt()
        self.hash8 = rf.readUnsignedInt()
        self.hash9 = rf.readUnsignedInt()
        self.hash10 = rf.readUnsignedInt()
        self.name1 = rf.readString(32)
        self.name2 = rf.readString(32)
        self.name3 = rf.readString(32)
        self.name4 = rf.readString(32)
        self.name5 = rf.readString(32)
        self.name6 = rf.readString(32)
        self.name7 = rf.readString(32)
        self.name8 = rf.readString(32)
        self.name9 = rf.readString(32)
        self.name10 = rf.readString(32)

    def display(self):
        print("LowerLeft: {}, {}, {}".format(self.posLowerLeft[0], self.posLowerLeft[1], self.posLowerLeft[2]))
        print("UpperRight: {}, {}, {}".format(self.posUpperRight[0], self.posUpperRight[1], self.posUpperRight[2]))
        print("Hash1: {} name: {}".format(self.hash1, self.name1))
        print("Hash2: {} name: {}".format(self.hash2, self.name2))
        print("Hash3: {} name: {}".format(self.hash3, self.name3))
        print("Hash4: {} name: {}".format(self.hash4, self.name4))
        print("Hash5: {} name: {}".format(self.hash5, self.name5))
        print("Hash6: {} name: {}".format(self.hash6, self.name6))
        print("Hash7: {} name: {}".format(self.hash7, self.name7))
        print("Hash8: {} name: {}".format(self.hash8, self.name8))
        print("Hash9: {} name: {}".format(self.hash9, self.name9))
        print("Hash10: {} name: {}".format(self.hash10, self.name10))

    def read(self, rf, hashTable):
        self.posLowerLeft = [rf.read_vector3d() for i in range(3)]
        self.posUpperRight = [rf.read_vector3d() for i in range(3)]
        self.unk1 = rf.read_int()
        self.hash1 = rf.read_unsigned_int()
        self.hash2 = rf.read_unsigned_int()
        self.hash3 = rf.read_unsigned_int()
        self.hash4 = rf.read_unsigned_int()
        self.hash5 = rf.read_unsigned_int()
        self.hash6 = rf.read_unsigned_int()
        self.hash7 = rf.read_unsigned_int()
        self.hash8 = rf.read_unsigned_int()
        self.hash9 = rf.read_unsigned_int()
        self.hash10 = rf.read_unsigned_int()
        self.name1 = rf.read_string(32)
        self.name2 = rf.read_string(32)
        self.name3 = rf.read_string(32)
        self.name4 = rf.read_string(32)
        self.name5 = rf.read_string(32)
        self.name6 = rf.read_string(32)
        self.name7 = rf.read_string(32)
        self.name8 = rf.read_string(32)
        self.name9 = rf.read_string(32)
        self.name10 = rf.read_string(32)
        # self.display()    
