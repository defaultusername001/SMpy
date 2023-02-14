class Item_STRBIG(IplItem):
    def __init__(self, gameType):
        self.gameType = gameType

    def read(self, line):
        pass
        # print("Message.displayMsgHigh({})".format(line))

    def read(self, rf):
        self.modelName = rf.read_string(24)
        self.unk1 = rf.read_int()
        self.unk2 = rf.read_int()
        self.unk3 = rf.read_int()
        self.pos = [rf.read_vector3d() for i in range(3)]
        self.rot = [rf.read_vector4d() for i in range(4)]
        # self.display()

    def display(self):
        print("ModelName: {}".format(self.modelName))
        print("Unk1: {}".format(self.unk1))
        print("Unk2: {}".format(self.unk2))
        print("Unk3: {}".format(self.unk3))
        print("Position: {}, {}, {}".format(self.pos[0], self.pos[1], self.pos[2]))
        print("Rotation: {}, {}, {}, {}".format(self.rot[0], self.rot[1], self.rot[2], self.rot[3]))

    def read(self, rf, hashTable):
        raise NotImplementedError("Not supported yet.")
