from typing import List, Union

class SimpleCollection:
    def __init__(self, br, type: int):
        self.type = type
        self.Read(br)

    def Read(self, br):
        offset = br.read_offset()
        self.Count = br.read_uint16()
        self.Size = br.read_uint16()

        self.Values = []

        save = br.get_current_offset()
        br.set_current_offset(offset)

        for i in range(self.Count):
            self.Values.append(self.ReadData(br))

        br.set_current_offset(save)

    def ReadData(self, br):
        if self.type == 0:
            data = br.read_uint32()
            return data
        else:
            data2 = br.read_uint32()
            return data2

class SimpleArray:
    def __init__(self, br, count: int, type: int):
        self.Count = count
        self.type = type
        self.read(br)

    def read(self, br):
        self.Values = []

        for i in range(self.Count):
            self.Values.append(self.read_data(br))

    def read_data(self, br):
        if self.type == 0:
            data = br.read_uint32()
            return data
        elif self.type == 1:
            offset = br.read_offset()
            return offset
        elif self.type == 2:
            byte = br.read_byte()
            return byte
        elif self.type == 3:
            short = br.read_uint16()
            return short
        elif self.type == 4:
            vec = br.read_vector_4d()
            return vec
        else:
            data2 = br.read_uint32()
            return data2

class PtrCollection:
    model_collection = 1
    geometry = 2
    shaderfx = 3

    def __init__(self, br, type: int):
        self.type = type
        self.br = br
        self.read()

    def read(self):
        self.start_offset = self.br.get_current_offset()
        self.ptr_list_offset = self.br.read_offset()

        self.Count = self.br.read_uint16()
        self.Size = self.br.read_uint16()

        self._item_offsets = [0] * self.Count
        self._items = []

        save = self.br.get_current_offset()

        self.br.set_current_offset(self.ptr_list_offset)

        for i in range(self.Count):
            self._item_offsets[i] = self.br.read_offset()

        for i in range(self.Count):
            self.br.set_current_offset(self._item_offsets[i])

            item = self.get_type()

            self._items.append(item)

        self
 #does the ptrcollection need to be repeated here? just import it 