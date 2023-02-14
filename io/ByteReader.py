import struct

class Vector4D:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class ByteReader:
    def __init__(self, stream, current_offset):
        self.stream = stream
        self.current_offset = current_offset
        self.system = True
        self.sys_size = 0

    def readUInt32(self):
        i = 0
        len = 4
        cnt = 0
        tmp = bytearray(len)
        i = self.current_offset
        while i < self.current_offset + len:
            tmp[cnt] = self.stream[i]
            cnt += 1
            i += 1
        accum = 0
        i = 0
        shift_by = 0
        while shift_by < 32:
            accum = accum | ((tmp[i] & 0xff) << shift_by)
            i += 1
            shift_by += 8
        self.current_offset += 4
        return accum

    def read_offset(self):
        value = 0
        offset = self.readUInt32()
        if offset == 0:
            value = 0
        else:
            if offset >> 28 != 5:
                raise Exception("Expected an offset")
            else:
                value = offset & 0x0fffffff
        return value


    def __init__(self, stream, current_offset):
        self.stream = stream
        self.current_offset = current_offset
        self.system = True
        self.sys_size = 0

    def readVector4D(self):
        x = self.readFloat()
        y = self.readFloat()
        z = self.readFloat()
        w = self.readFloat()
        return Vector4D(x, y, z, w)

    def readFloat(self):
        accum = 0
        i = 0
        shift_by = 0
        while shift_by < 32:
            accum = accum | ((self.stream[self.current_offset + i] & 0xff) << shift_by)
            i += 1
            shift_by += 8
        self.current_offset += 4
        return struct.unpack("!f", struct.pack("!I", accum))[0]

    def readUInt16(self):
        low = self.stream[self.current_offset] & 0xff
        high = self.stream[self.current_offset + 1] & 0xff
        self.current_offset += 2
        return (high << 8) | low

    def readInt16(self):
        ret = (self.stream[self.current_offset + 1].to_bytes(2, byteorder='big') << 8) | (self.stream[self.current_offset].to_bytes(2, byteorder='big') & 0xff)
        self.current_offset += 2
        return ret

    def readDataOffset(self):
        value = 0
        offset = self.readUInt32()
        if offset == 0:
            value = 0
        else:
            if offset >> 28 != 6:
                pass
            value = offset & 0x0fffffff
        return value


    def readByte(self):
        b = self.stream[self.current_offset]
        self.current_offset += 1
        return b

    def readNullTerminatedString(self, size):
        woord = ""
        got_null = False
        for i in range(size):
            b = self.readByte()
            if not got_null:
                if b != 0:
                    woord += chr(b)
                else:
                    got_null = True
        return woord

    def readNullTerminatedString(self):
        sb = ""
        c = chr(self.stream[self.current_offset])
        while ord(c) != 0:
            sb += c
            self.current_offset += 1
            c = chr(self.stream[self.current_offset])
        return sb

    def readString(self, length):
        sb = ""
        for i in range(length):
            c = chr(self.stream[self.current_offset])
            sb += c
            self.current_offset += 1
        return sb

    def toArray(self, bytes):
        arr = bytearray(bytes)
        for i in range(bytes):
            arr[i] = self.stream[self.current_offset]
            self.current_offset += 1
        return arr

    def toArray(self):
        return self.stream


    def toArray(self, start, end):
        ret_size = end - start
        ret_stream = bytearray(ret_size)
        self.setCurrentOffset(start)
        for i in range(ret_size):
            ret_stream[i] = self.stream[self.current_offset]
            self.current_offset += 1
        return ret_stream

    def readByte(self):
        self.current_offset += 1
        return self.stream[self.current_offset - 1]

    def getCurrentOffset(self):
        return self.current_offset

    def setCurrentOffset(self, offset):
        self.current_offset = offset
        if not self.system:
            self.current_offset += self.sys_size

    def setSysSize(self, size):
        self.sys_size = size

    def setSystemMemory(self, system):
        self.system = system

    def getByteBuffer(self, size):
        buffer = bytearray(size)
        for i in range(size):
            buffer[i] = self.readByte()
        return buffer

    def readBytes(self, p_count):
        buffer = bytearray(p_count)
        for i in range(p_count):
            buffer[i] = self.readByte()
        return buffer

    @property
    def inputStream(self):
        return self.stream[self.current_offset:]

    def skipBytes(self, bytes):
        self.current_offset += bytes

    def __init__(self, stream, current_offset):
        self.stream = stream
        self.current_offset = current_offset
        self.system = True
        self.sys_size = 0

    def hasFlag(self, flags, flag):
        return (flags & flag) == flag

    def moreToRead(self):
        return len(self.stream) - self.current_offset

    def unsignedInt(self):
        i = self.readUInt32()
        return i & 0xffffffff
