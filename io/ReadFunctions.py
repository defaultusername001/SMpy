class ReadFunctions:
    def __init__(self, name):
        self.data_in = open(name, "rb")

    def closeFile(self):
        try:
            self.data_in.close()
            return True
        except Exception as e:
            print("Unable to close file")
            return False

    def readByte(self):
        try:
            return int.from_bytes(self.data_in.read(1), byteorder='little')
        except Exception as e:
            return -1

    def readBytes(self, num_bytes):
        try:
            return self.data_in.read(num_bytes)
        except Exception as e:
            raise Exception("Error reading bytes: ", e)

    def readInt(self):
        try:
            return int.from_bytes(self.data_in.read(4), byteorder='little')
        except Exception as e:
            return -1

    def readShort(self):
        try:
            return int.from_bytes(self.data_in.read(2), byteorder='little')
        except Exception as e:
            return -1

    def readFloat(self):
            try:
                return struct.unpack("<f", self.data_in.read(4))[0]
            except Exception as e:
                return -1.0

    def readString(self, size):
        try:
            return self.data_in.read(size).decode("utf-8")
        except Exception as e:
            return ""

    def readNullTerminatedString(self, size=None):
        result = bytearray()
        if size is None:
            b = self.data_in.read(1)
            while b != b'\x00':
                result += b
                b = self.data_in.read(1)
        else:
            for i in range(size):
                b = self.data_in.read(1)
                if b == b'\x00':
                    break
                result += b
        return result.decode("utf-8")

    def readChar(self):
        try:
            return chr(self.readByte())
        except Exception as e:
            return '\x00'

    def swapInt(self, v):
        return (v >> 24 & 0xff) + (v >> 8 & 0xff00) + (v << 8 & 0xff0000) + (v << 24 & 0xff000000)

    def swapShort(self, i):
        return (i >> 8 & 0xff) + (i << 8 & 0xff00)

    def swapFloat(self, f):
        int_value = struct.unpack("<I", struct.pack("<f", f))[0]
        int_value = self.swapInt(int_value)
        return struct.unpack("<f", struct.pack("<I", int_value))[0]

    def readVector3D(self):
        x = self.readFloat()
        y = self.readFloat()
        z = self.readFloat()
        return (x, y, z)

    def readVector4D(self):
        x = self.readFloat()
        y = self.readFloat()
        z = self.readFloat()
        w = self.readFloat()
        return (x, y, z, w)

    def moreToRead(self):
        try:
            return self.data_in.seek(0, 2) - self.data_in.tell()
        except Exception as e:
            return 0

class ByteReader:
    def __init__(self, stream, index):
        self.stream = stream
        self.index = index

class ReadFunctions:
    def __init__(self, data_in):
        self.dataIn = data_in

    @property
    def byteReader(self):
        try:
            stream = bytearray(dataIn.length().to_bytes(4, byteorder='big'))
            dataIn.readinto(stream)
            return ByteReader(stream, 0)
        except IOError:
            return None

    def getByteReader(self, size):
        stream = bytearray(size)
        dataIn.readinto(stream)
        return ByteReader(stream, 0)

    def seek(self, offset):
        try:
            self.dataIn.seek(offset)
        except IOError as ex:
            logging.error(ex)

    def readUnsignedInt(self):
        i = self.readInt()
        return i & 0xffffffff

    def readArray(self, size):
        array = bytearray(size)
        try:
            self.dataIn.readinto(array)
        except IOError as ex:
            print("logging.error(ex)")
        return array
