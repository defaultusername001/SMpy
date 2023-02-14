class PtrCollection:
    modelCollection = 1
    geometry = 2
    shaderfx = 3

    def __init__(self):
        self._itemOffsets = []
        self._items = []
        self.startOffset = 0
        self.ptrListOffset = 0
        self.Count = 0
        self.Size = 0
        self.type = 0
        self.br = None

    def __init__(self, br, type):
        self._itemOffsets = []
        self._items = []
        self.startOffset = 0
        self.ptrListOffset = 0
        self.Count = 0
        self.Size = 0
        self.type = type
        self.br = br
        self.read()

    def read(self):
        self.startOffset = self.br.get_current_offset()
        self.ptrListOffset = self.br.read_offset()
        self.Count = self.br.read_uint16()
        self.Size = self.br.read_uint16()
        self._itemOffsets = [0] * self.Count
        self._items = []
        save = self.br.get_current_offset()
        self.br.set_current_offset(self.ptrListOffset)
        for i in range(self.Count):
            self._itemOffsets[i] = self.br.read_offset()
        for i in range(self.Count):
            self.br.set_current_offset(self._itemOffsets[i])
            item = self.get_type()
            self._items.append(item)
        self.br.set_current_offset(save)

    def get_type(self):
        if self.type == PtrCollection.modelCollection:
            model = Model2()
            model.read(self.br)
            return model
        elif self.type == PtrCollection.geometry:
            geo = Geometry()
            geo.read(self.br)
            return geo
        elif self.type == PtrCollection.shaderfx:
            sf = ShaderFx()
            sf.read(self.br)
            return sf
        else:
            model2 = Model2()
            return model2
    def get_data_names(self):
        names = [0] * (4 + self.Count)
        i = 0
        names[i] = "ptrListOffset"
        i += 1
        names[i] = "Count"
        i += 1
        names[i] = "Size"
        i += 1
        names[i] = "[Start PtrList]"
        i += 1
        for i2 in range(self.Count):
            names[i] = "  Pointer {} {}".format(i2 + 1, self._items)
            i += 1
        return names

    def get_data_values(self):
        values = [0] * (4 + self.Count)
        i = 0
        values[i] = Utils.get_hex_string(self.ptrListOffset)
        i += 1
        values[i] = str(self.Count)
        i += 1
        values[i] = str(self.Size)
        i += 1
        values[i] = ""
        i += 1
        for i2 in range(self.Count):
            values[i] = Utils.get_hex_string(self._itemOffsets[i2])
            i += 1
        return values
