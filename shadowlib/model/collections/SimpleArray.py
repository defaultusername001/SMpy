from typing import List

class SimpleArray:
    def __init__(self, br, count, type):
        self.Values: List[T] = []
        self.Count = count
        self.type = type
        self.read(br)

    def read(self, br):
        for i in range(self.Count):
            self.Values.append(self.read_data(br))

    def read_data(self, br):
        if self.type == SimpleArray.ReadUInt32:
            data = br.read_uint32()
            return data
        elif self.type == SimpleArray.ReadOffset:
            offset = br.read_offset()
            return offset
        elif self.type == SimpleArray.ReadByte:
            Byte = br.read_byte()
            return Byte
        elif self.type == SimpleArray.ReadShort:
            Short = br.read_uint16()
            return Short
        elif self.type == SimpleArray.ReadVector4:
            vec = br.read_vector4d()
            vec.print("SimpleArray")
            return vec
        else:
            data2 = br.read_uint32()
            return data2

SimpleArray.ReadUInt32 = 0
SimpleArray.ReadOffset = 1
SimpleArray.ReadByte = 2
SimpleArray.ReadShort = 3
SimpleArray.ReadVector4 = 4
