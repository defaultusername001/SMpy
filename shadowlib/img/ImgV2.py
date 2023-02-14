class ImgV2:
    def load(self, path):
        items = []

        rf = ReadFunctions(path)

        itemCount = 0

        itemCount = rf.readInt()

        for curItem in range(itemCount):
            itemOffset = rf.readInt() * 2048
            itemSize = rf.readInt() * 2048
            itemName = rf.readNullTerminatedString(24)
            itemType = Utils.getFileType(itemName)
            item = ImgItem(itemName)
            item.offset = itemOffset
            item.size = itemSize
            item.type = itemType
            items.append(item)

        return Img(path = path, items = items)
