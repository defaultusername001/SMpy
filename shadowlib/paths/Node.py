class Node:
    def __init__(self, rf):
        self.memAdress = rf.readInt()
        self.zero = rf.readInt()
        self.areaID = rf.readShort()
        self.nodeID = rf.readShort()
        self.unknown = rf.readInt()
        self.always7FFE = rf.readShort()
        self.linkID = rf.readShort()
        self.posX = rf.readShort()
        self.posY = rf.readShort()
        self.posZ = rf.readShort()
        self.pathWidth = rf.readByte()
        self.pathType = rf.readByte()
        self.flags = rf.readInt()

    def __str__(self):
        return ("--------------Node---------------"
                + f"Mem Adress: {self.memAdress}"
                + f"Zero: {self.zero}"
                + f"AreaID: {self.areaID}"
                + f"NodeID: {self.nodeID}"
                + f"unknown: {self.unknown}"
                + f"Always7FFE: {self.always7FFE}"
                + f"LinkID: {self.linkID}"
                + f"PosX: {self.posX/8.0}" #precision values
                + f"PosY: {self.posY/8.0}" #precision values
                + f"PosZ: {self.posZ/128.0}" #precision values
                + f"PathWidth: {self.pathWidth}"
                + f"PathType: {self.pathType}"
                + f"Flags: {self.flags}")
