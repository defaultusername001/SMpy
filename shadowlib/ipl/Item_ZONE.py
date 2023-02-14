class Item_ZONE:
    def __init__(self, gameType):
        self.gameType = gameType
        self.posLowerLeft = None
        self.posUpperRight = None

    def read(self, line):
        pass
        # print("Message.displayMsgHigh({})".format(line))

    def read(self, rf):
        self.posLowerLeft = [rf.read_vector3d() for i in range(3)]
        self.posUpperRight = [rf.read_vector3d() for i in range(3)]
        # self.display()

    def display(self):
        print("LowerLeft: {}, {}, {}".format(self.posLowerLeft[0], self.posLowerLeft[1], self.posLowerLeft[2]))
        print("UpperRight: {}, {}, {}".format(self.posUpperRight[0], self.posUpperRight[1], self.posUpperRight[2]))

    def read(self, rf, hashTable):
        print("{} not supported yet.".format(self.__class__.__name__))
