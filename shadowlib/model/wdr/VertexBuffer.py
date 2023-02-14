class VertexBuffer:
    def __init__(self):
        self.startOffset = None
        self.VTable = None
        self.VertexCount = None
        self.Unknown1 = None
        self.DataOffset = None
        self.StrideSize = None
        self.vertexDeclOffset = None
        self.Unknown2 = None
        self.DataOffset2 = None
        self.p2Offset = None
        self.RawData = None
        self.VertexDeclaration = None

    def __init__(self, br):
        self.startOffset = None
        self.VTable = None
        self.VertexCount = None
        self.Unknown1 = None
        self.DataOffset = None
        self.StrideSize = None
        self.vertexDeclOffset = None
        self.Unknown2 = None
        self.DataOffset2 = None
        self.p2Offset = None
        self.RawData = None
        self.VertexDeclaration = None
        self.Read(br)

    def ReadData(self, br):
        br.set_system_memory(False)
        br.set_current_offset(self.DataOffset)
        self.RawData = br.to_array(self.VertexCount * self.StrideSize)
        br.set_system_memory(True)

    def Read(self, br):
        self.startOffset = br.get_current_offset()
        self.VTable = br.read_uint32()
        self.VertexCount = br.read_uint16()
        self.Unknown1 = br.read_uint16()
        self.DataOffset = br.read_data_offset()
        self.StrideSize = br.read_uint32()
        self.vertexDeclOffset = br.read_offset()
        self.Unknown2 = br.read_uint32()
        self.DataOffset2 = br.read_data_offset()
        self.p2Offset = br.read_offset()
        self.ReadData(br)
        br.set_current_offset(self.vertexDeclOffset)
        self.VertexDeclaration = VertexDeclaration(br)

    def get_data_names(self):
        return ["VTable", "VertexCount", "Unknown1", "DataOffset", "StrideSize", "vertexDeclOffset", "Unknown2", "DataOffset2", "p2Offset", "RawData(Length)"]

    def get_data_values(self):
        return [str(self.v_table), str(self.vertex_count), str(self.unknown_1), hex(self.data_offset), str(self.stride_size), hex(self.vertex_decl_offset), str(self.unknown_2), hex(self.data_offset_2), hex(self.p2_offset), str(len(self.raw_data))]