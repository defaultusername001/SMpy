class WriteBuffer:
    def __init__(self):
        self.byteBuffer = []

    def writeByte(self, waarde):
        self.byteBuffer.append(waarde.to_bytes(1, byteorder='little'))
        return 1

    def writeInt(self, waarde):
        bytes = waarde.to_bytes(4, byteorder='little')
        for i in range(len(bytes)):
            self.writeByte(bytes[i])
        return 4

    def writeVector(self, x, y, z, w):
        self.writeFloat(x)
        self.writeFloat(y)
        self.writeFloat(z)
        if w != -1.0:
            self.writeFloat(w)
        else:
            self.writeInt(2139095041)
        return 16

    def writeVector(self, vec):
        self.writeFloat(vec.x)
        self.writeFloat(vec.y)
        self.writeFloat(vec.z)
        self.writeInt(2139095041)
        return 16

    def writeOffset(self, waarde):
        sWaarde = waarde.to_bytes(2, byteorder='big')
        sWaarde = int.from_bytes(sWaarde, byteorder='little')
        self.writeShort(waarde)
        self.writeShort(20480)
        return 4

    def writeDataOffset(self, waarde):
        bbuf = waarde.to_bytes(4, byteorder='big')
        test1 = bbuf[0]
        test2 = bbuf[1]
        test3 = bbuf[2]
        self.writeByte(test1)
        self.writeByte(test3)
        self.writeByte(test2)
        self.writeByte(0x60)
        return 4

    def writeShort(self, waarde):
            sWaarde = waarde.to_bytes(2, byteorder='big')
            sWaarde = int.from_bytes(sWaarde, byteorder='little')
            bytes = sWaarde.to_bytes(2, byteorder='little')
            for i in range(len(bytes)):
                self.writeByte(bytes[i])
            return 2
        
    def writeFloat(self, waarde):
        bytes = struct.pack('<f', waarde)
        for i in range(len(bytes)):
            self.writeByte(bytes[i])
        return 4
    
    def writeChar(self, waarde):
        self.writeByte(ord(waarde))
        return 1

    def writeString(self, waarde):
        length = 0
        for i in range(len(waarde)):
            length += self.writeChar(waarde[i])
        length += self.writeByte(0)
        return length

    def writeArray(self, array):
        for i in range(len(array)):
            self.writeByte(array[i])
        return len(array)

    def replaceOffset(self, offsetOffset, newOffset):
        bbuf = newOffset.to_bytes(4, byteorder='big')
        self.byteBuffer[offsetOffset] = bbuf[3]
        self.byteBuffer[offsetOffset + 1] = bbuf[2]
        self.byteBuffer[offsetOffset + 2] = bbuf[1]

    def replaceDataOffset(self, offsetOffset, newOffset):
        bbuf = newOffset.to_bytes(4, byteorder='big')
        self.byteBuffer[offsetOffset] = bbuf[3]
        self.byteBuffer[offsetOffset + 1] = bbuf[2]
        self.byteBuffer[offsetOffset + 2] = bbuf[1]

    @property
    def array(self):
        dataBuffer = bytearray(len(self.byteBuffer))
        for i in range(len(dataBuffer)):
            dataBuffer[i] = self.byteBuffer[i]
        return dataBuffer

    @staticmethod
    def float2arr(f):
        n = struct.pack('<f', f)
        return n

    @staticmethod
    def short2arr(i):
        s = i.to_bytes(2, byteorder='little', signed=True)
        return s

    @staticmethod
    def int2arr(value):
        b = value.to_bytes(4, byteorder='little', signed=True)
        return b      
