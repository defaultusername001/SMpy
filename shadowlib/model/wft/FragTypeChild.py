class FragTypeChild:
    def __init__(self, br):
        self.drwblOffset = 0
        VTable = br.readUInt32()
        unkFloat1 = br.readFloat()
        unkFloat2 = br.readFloat()
        unkZero = br.readUInt32()
        for i in range(8):
            unkVec = br.readVector4D()
        self.drwblOffset = br.readOffset()
        unkZero2 = br.readUInt32()
        unkOffset1 = br.readOffset()
        unkOffset2 = br.readOffset()
        unkOffset3 = br.readOffset()
        unkOffset4 = br.readOffset()
        unkZero3 = br.readUInt32()
        unkZero4 = br.readUInt32()
        unkZero5 = br.readUInt32()
        unkZero6 = br.readUInt32()
        unkOffset5 = br.readOffset()
