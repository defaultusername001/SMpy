class ImgV3:
    def __init__(self, encryptionKey):
        self.encryptionKey = encryptionKey
        self.decrypter = Decrypter(encryptionKey)
        self.identifier = bytearray(4)

    def load(self, path):
        rf = ReadFunctions(path)

        self.identifier[0] = rf.readByte()
        self.identifier[1] = rf.readByte()
        self.identifier[2] = rf.readByte()
        self.identifier[3] = rf.readByte()

        if (self.identifier[0] == 82 and self.identifier[1] == 42 and self.identifier[2] == 78 and self.identifier[3] == -87):
            img = self.readUnEncryptedImg(path, rf)
        else:
            img = self.readEncryptedImg(path, rf)

        rf.closeFile()
        return img

    def readUnEncryptedImg(self, path, rf):
        items = []

        itemCount = rf.readInt()
        tableSize = rf.readInt()
        sizeOfTableItems = rf.readShort()
        unknown = rf.readShort()

        for curItem in range(itemCount):
            itemSize = rf.readInt()
            itemType = rf.readInt()
            itemOffset = rf.readInt() * 0x800
            usedBlocks = rf.readShort()
            padding = rf.readShort() & 0x7FF
            item = ImgItem("")
            if itemType <= 0x6E:
                item.flags = itemSize
                itemSize = Utils.getTotalMemSize(itemSize)
            item.offset = itemOffset
            item.size = usedBlocks * 0x800 - padding
            item.type = itemType
            items.append(item)

        for curName in range(itemCount):
            items[curName].name = rf.readNullTerminatedString()

        return Img(path = path, items = items, isEncrypted = False)

    def readEncryptedImg(self, path, rf):
        items = []

        data = self.withIdentifier(rf)

        br = ByteReader(data, 0)
        id = br.readUInt32()
        version = br.readUInt32()
        itemCount = br.readUInt32()
        tableSize = br.readUInt32()

        itemSize = rf.readShort()
        unknown = rf.readShort()

        namesSize = tableSize - itemCount * itemSize

        for i in range(itemCount):
            data = self.decrypter.decrypt16byteBlock(rf)
            br = ByteReader(data, 0)
            item = ImgItem("")
            itemSize = br.readUInt32()
            itemType = br.readUInt32()
            itemOffset = br.readUInt32() * 2048
            usedBlocks = br.readUInt16()
            padding = br.readUInt16() & 0x7FF
            if itemType <= 0x6E:
                item.flags = itemSize
                itemSize = Utils.getTotalMemSize(itemSize)
            item.offset = itemOffset
            item.size = usedBlocks * 0x800 - padding
            item.type = itemType
            items.append(item)

        i = 0
        names = bytearray(namesSize)
        while i < namesSize:
            data = self.decrypter.decrypt16byteBlock(rf)
            for j in range(16):
                names[i + j] = data[j]
            i += 16
            if i + 16 > namesSize:
                lastName = rf.readNullTerminatedString()
                lastBytes = lastName.encode()
                for j in range(len(lastBytes)):
                    names[i + j] = lastBytes[j]
                i += 16

        br = ByteReader(names, 0)

        i = 0
        while i < itemCount:
            name = br.readNullTerminatedString()
            items[i].name = name
            br.readByte()
            i += 1

        rf.closeFile()

        return Img(path = path, items = items, isEncrypted = True)

    def withIdentifier(self, rf):
            data = bytearray(16)

            data[0] = self.identifier[0]
            data[1] = self.identifier[1]
            data[2] = self.identifier[2]
            data[3] = self.identifier[3]

            for j in range(4, 16):
                data[j] = rf.readByte()

            return self.decrypter.decrypt(data)

    def saveImg(self, img):
        raise NotImplementedError("Saving is not implemented") #TODO actually implement this with the new script, just fix the encryption on the write
