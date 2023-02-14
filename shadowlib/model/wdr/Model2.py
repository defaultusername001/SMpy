class Model2:
    def __init__(self):
        self.start_offset = None
        self.VTable = None
        self.Geometries = None
        self.unknown_vector_offsets = None
        self.material_mapping_offset = None
        self.Unknown1 = None
        self.Unknown2 = None
        self.Unknown3 = None
        self.GeoCount = None
        self.UnknownVectors = None
        self.ShaderMappings = None

    def read(self, br):
        self.start_offset = br.get_current_offset()
        self.VTable = br.read_uint32()
        self.Geometries = PtrCollection(br, 2, Geometry)
        self.unknown_vector_offsets = br.read_offset()
        self.material_mapping_offset = br.read_offset()
        self.Unknown1 = br.read_uint16()
        self.Unknown2 = br.read_uint16()
        self.Unknown3 = br.read_uint16()
        self.GeoCount = br.read_uint16()
        br.set_current_offset(self.unknown_vector_offsets)
        self.UnknownVectors = SimpleArray(br, 4, 4, Vector4D)
        br.set_current_offset(self.material_mapping_offset)
        self.ShaderMappings = SimpleArray(br, self.Geometries.count, 3)

    def __str__(self):
        return "Model"

    def get_data_names(self):
        names = [0] * (9 + len(self.UnknownVectors) + len(self.ShaderMappings))
        i = 0
        names[i] = "VTable"
        i += 1
        names[i] = "unknownVectorOffsets"
        i += 1
        names[i] = "materialMappingOffset"
        i += 1
        names[i] = "Unknown1"
        i += 1
        names[i] = "Unknown2"
        i += 1
        names[i] = "Unknown3"
        i += 1
        names[i] = "GeoCount"
        i += 1
        names[i] = "[UnknownVectors]"
        i += 1
        for i2 in range(len(self.UnknownVectors)):
            names[i] = "  Vector " + str(i2 + 1)
            i += 1
        names[i] = "[ShaderMappings]"
        i += 1
        for i2 in range(len(self.ShaderMappings)):
            names[i] = "  ShaderMapping " + str(i2 + 1)
            i += 1
        return names

    def get_data_values(self):
        values = [0] * (9 + len(self.UnknownVectors) + len(self.ShaderMappings))
        i = 0
        values[i] = str(self.VTable)
        i += 1
        values[i] = Utils.get_hex_string(self.unknown_vector_offsets)
        i += 1
        values[i] = Utils.get_hex_string(self.material_mapping_offset)
        i += 1
        values[i] = str(self.Unknown1)
        i += 1
        values[i] = str(self.Unknown2)
        i += 1
        values[i] = str(self.Unknown3)
        i += 1
        values[i] = str(self.GeoCount)
        i += 1
        values[i] = ""
        i += 1
        for i2 in range(len(self.UnknownVectors)):
            values[i] = str(self.UnknownVectors[i2])
            i += 1
        values[i] = ""
        i += 1
        for i2 in range(len(self.ShaderMappings)):
            values[i] = str(self.ShaderMappings[i2])
            i += 1
        return values
