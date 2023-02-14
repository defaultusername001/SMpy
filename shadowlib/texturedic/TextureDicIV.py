class TextureDicIV:
    def __init__(self):
        self.textures = []
        self.sysSize = 0

    def loadTextureDic(self, wtd, compressed, sysSize):
        self.sysSize = sysSize
        if compressed:
            br = None
            if wtd.br == None:
                rf = ReadFunctions(wtd.fileName)
                print("WTD Opened")
                br = rf.byteReader
            else:
                br = wtd.br

            stream = bytearray()
            res = ResourceFile()
            stream = res.read(br, wtd.fileSize)
            self.sysSize = res.systemSize
            br2 = ByteReader(stream, 0)
            self.read(br2)
        else:
            self.read(wtd.br)
        wtd.textures = self.textures

    def read(br):
        VTable = br.readUInt32()
        blockMapOffset = br.readOffset()
        parentDictionary = br.readUInt32()
        usageCount = br.readUInt32()

        # SimpleCollection
        hashTableOffset = br.readOffset()
        texCount = br.readUInt16()
        texSize = br.readUInt16()

        if texCount > 0:
            save = br.getCurrentOffset()
            br.setCurrentOffset(hashTableOffset)
            for i in range(texCount):
                # Message.displayMsgHigh("Hash: " + br.readUInt32());
                pass
            br.setCurrentOffset(save)

            # PointerCollection
            textureListOffset = br.readOffset()
            textureCount = br.readUInt16()
            pTexSize = br.readUInt16()
            save = br.getCurrentOffset()
            br.setCurrentOffset(textureListOffset)
            for i in range(textureCount):
                texOffset = br.readOffset()
                save = br.getCurrentOffset()
                br.setCurrentOffset(texOffset)
                TexVTable = br.readUInt32()
                unknown1 = br.readUInt32()
                unknown2 = br.readUInt32()
                unknown3 = br.readUInt32()
                unknown4 = br.readUInt32()
                texNameOffset = br.readOffset()
                save2 = br.getCurrentOffset()
                br.setCurrentOffset(texNameOffset)
                packName = br.readNullTerminatedString()
                # Message.displayMsgHigh("PackName: " + packName);
                name = packName.replace("pack:/", "").replace(".dds", "")
                br.setCurrentOffset(save2)
                unknown5 = br.readUInt32()
                width = br.readUInt16()
                height = br.readUInt16()
                compression = br.readString(4)
                strideSize = br.readUInt16()
                type = br.readByte()
                levels = br.readByte()
                unk1 = br.readFloat()
                unk2 = br.readFloat()
                unk3 = br.readFloat()
                unk1 = br.readFloat()
                unk2 = br.readFloat()
                unk3 = br.readFloat()
                nextTexOffset = br.readOffset()
                unknown6 = br.readUInt32()
                dataOffset = br.readDataOffset()
                unknown7 = br.readUInt32()

                # load the texture
                br.setCurrentOffset(dataOffset + sysSize)

                if compression == "DXT1":
                    dataSize = width * height // 2
                elif compression == "DXT3" or compression == "DXT5":
                    dataSize = width * height
                else:
                    raise ValueError("Unknown compression type")

                texture = Texture(
                    diffuseTexName=name,
                    dxtCompressionType=compression,
                    width=width,
                    height=height,
                    data=br.readBytes(dataSize),
                )

                textures.append(texture)
                br.setCurrentOffset(save)
