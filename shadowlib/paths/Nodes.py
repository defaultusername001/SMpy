class Nodes:
    def __init__(self):
        self.nodeCount = 0
        self.carNodeCount = 0
        self.intersectionNodeCount = 0
        self.linkCount = 0

        rf = ReadFunctions("E:/Nodes/nodes29.nod")
        self.readHeader(rf)
        for i in range(self.nodeCount):
            node = Node(rf)
        for i in range(self.linkCount):
            link = Link(rf)

    def readHeader(self, rf):
        self.nodeCount = rf.readInt()
        self.carNodeCount = rf.readInt()
        self.intersectionNodeCount = rf.readInt()
        self.linkCount = rf.readInt()
        print(f"Node Count: {self.nodeCount}")
        print(f"Car Node Count: {self.carNodeCount}")
        print(f"intersectionNode Count: {self.intersectionNodeCount}")
        print(f"Link Count: {self.linkCount}")
