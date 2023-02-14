class Link:
    def __init__(self, rf):
        self.areaID = rf.readShort()
        self.nodeID = rf.readShort()
        self.unknown = rf.readByte()
        self.linkLength = rf.readByte()
        self.flags = rf.readShort()

    def __str__(self):
        return ("-----------Link-------------"
                + f"AreaID: {self.areaID}"
                + f"NodeID: {self.nodeID}"
                + f"unknown: {self.unknown}"
                + f"LinkLength: {self.linkLength}"
                + f"Flags: {self.flags}")
