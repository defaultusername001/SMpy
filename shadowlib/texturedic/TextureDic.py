class TextureDic:
    def __init__(self, fileName, br, gameType, compressed, sysSize):
        self.fileName = fileName
        self.br = br
        self.gameType = gameType
        self.compressed = compressed
        self.textureCount = 0
        self.flags = 0
        self.size = 0
        self.textures = []
        self.fileSize = sysSize
        self.loadTextureDic()

    def loadTextureDic(self):
        if self.gameType == GameType.GTA_IV:
            if self.compressed:
                TextureDicIV().loadTextureDic(self, self.compressed, 0)
            else:
                TextureDicIV().loadTextureDic(self, self.compressed, self.fileSize)
        else:
            TextureDic_III_ERA().loadTextureDic(self)

    def addTexture(self, tex):
        self.textures.append(tex)
