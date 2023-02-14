class Texture:
    def __init__(self, diffuseTexName, dxtCompressionType, width, height, data):
        self.diffuseTexName = diffuseTexName
        self.dxtCompressionType = dxtCompressionType
        self.width = width
        self.height = height
        self.data = data
        self.compression = 0
        self.offset = 0
        self.conversionOffset = 0
        self.dataSize = 0
        self.alphaTexName = None
