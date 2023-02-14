class VertexDeclaration:
    def __init__(self, br):
        self.UsageFlags = 0
        self.Stride = 0
        self.AlterateDecoder = 0
        self.Type = 0
        self.DeclarationTypes = 0
        self.Read(br)

    def Read(self, br):
        self.UsageFlags = br.readUInt32()
        self.Stride = br.readUInt16()
        self.AlterateDecoder = br.readByte()
        self.Type = br.readByte()
        br.readUInt32()
        br.readUInt32()
        # self.DeclarationTypes = br.readUInt64()

    def getDataNames(self):
        name_list = []
        name_list.append("UsageFlags")
        name_list.append("Stride")
        name_list.append("AlterateDecoder")
        name_list.append("Type")

        return name_list

    def getDataValues(self):
        value_list = []
        value_list.append(str(self.UsageFlags))
        value_list.append(str(self.Stride))
        value_list.append(str(self.AlterateDecoder))
        value_list.append(str(self.Type))

        return value_list
