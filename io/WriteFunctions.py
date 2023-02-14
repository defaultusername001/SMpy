import struct
# we dont have IOException here, fix, just labeled for clarity sake to change the 1:1 conversion
class WriteFunctions:
    def init(self, name: str):
        self.dataOut = open(name, "wb")

    
    def closeFile(self) -> bool:
        try:
            self.dataOut.close()
        except IOException as ex: 
            logger.log(Level.SEVERE, ex)
            return False
        return True

    def writeByte(self, value: int):
        try:
            self.dataOut.write(value.to_bytes(1, byteorder='little'))
        except IOException as ex:
            pass

    def write(self, value: int):
        try:
            self.dataOut.write(value.to_bytes(4, byteorder='little'))
        except IOException as ex:
            value = -1

    def writeShort(self, value: int):
        try:
            self.dataOut.write(value.to_bytes(2, byteorder='little'))
        except IOException as ex:
            value = -1

    def write(value):
        value = value
        bbuf = bytearray(struct.pack("f", value))
        value = struct.unpack("<f", bbuf)[0]
        try:
            dataOut.write(struct.pack("f", value))
        except Exception as ex:
            print("An error occurred:", ex)

    def writeChar(value):
        letter = b'\x00'
        try:
            dataOut.write(bytes([ord(value)]))
        except Exception as ex:
            # alot of this is not defined in the dataout
            pass
        return letter

    def writeString(value):
        for i in range(len(value)):
            writeChar(value[i])

    def writeNullTerminatedString(value):
        for i in range(len(value)):
            writeChar(value[i])
        dataOut.write(b'\x00')

    def write(vector):
        write(vector.x)
        write(vector.y)
        write(vector.z)

    def write(vector):
        write(vector.x)
        write(vector.y)
        write(vector.z)
        write(vector.w)

    def write(array):
        try:
            dataOut.write(array)
        except Exception as ex:
            print("An error occurred:", ex)

    def seek(pos):
        try:
            dataOut.seek(pos)
        except Exception as ex:
            print("An error occurred:", ex)

    def gotoEnd():
        try:
            dataOut.seek(dataOut.tell(), 2)
        except Exception as ex:
            print("An error occurred:", ex)

    def fileSize():
        try:
            return dataOut.tell()
        except Exception as ex:
            return 0
  