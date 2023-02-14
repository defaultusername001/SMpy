class Geometry:
    def __init__(self):
        self.start_offset = 0
        self.v_table = 0
        self.unknown1 = 0
        self.unknown2 = 0
        self.vertex_buffers_offset = 0
        self.unknown3 = 0
        self.unknown4 = 0
        self.unknown5 = 0
        self.index_buffers_offset = 0
        self.unknown6 = 0
        self.unknown7 = 0
        self.unknown8 = 0
        self.index_count = 0
        self.face_count = 0
        self.vertex_count = 0
        self.primitive_type = 0
        self.unknown9 = 0
        self.vertex_stride = 0
        self.unknown10 = 0
        self.unknown11 = 0
        self.unknown12 = 0
        self.unknown13 = 0
        self.vertex_buffer = None
        self.index_buffer = None

    def read(self, br):
        self.start_offset = br.get_current_offset()
        self.v_table = br.read_uint32()
        self.unknown1 = br.read_uint32()
        self.unknown2 = br.read_uint32()
        self.vertex_buffers_offset = br.read_offset()
        self.unknown3 = br.read_uint32()
        self.unknown4 = br.read_uint32()
        self.unknown5 = br.read_uint32()
        self.index_buffers_offset = br.read_offset()
        self.unknown6 = br.read_uint32()
        self.unknown7 = br.read_uint32()
        self.unknown8 = br.read_uint32()
        self.index_count = br.read_uint32()
        self.face_count = br.read_uint32()
        self.vertex_count = br.read_uint16()
        self.primitive_type = br.read_uint16()
        self.unknown9 = br.read_uint32()
        self.vertex_stride = br.read_uint16()
        self.unknown10 = br.read_uint16()
        self.unknown11 = br.read_uint32()
        self.unknown12 = br.read_uint32()
        self.unknown13 = br.read_uint32()
        br.set_current_offset(self.vertex_buffers_offset)
        self.vertex_buffer = VertexBuffer(br)
        br.set_current_offset(self.index_buffers_offset)
        self.index_buffer = IndexBuffer(br)

    def get_data_names(self):
        return [
            "Unknown1",
            "Unknown2",
            "vertexBuffersOffset",
            "Unknown3",
            "Unknown4",
            "Unknown5",
            "indexBuffersOffset",
            "Unknown6",
            "Unknown7",
            "Unknown8",
            "IndexCount",
            "FaceCount",
            "VertexCount",
            "PrimitiveType",
            "Unknown9",
            "VertexStride",
            "Unknown10",
            "Unknown11",
            "Unknown12",
            "Unknown13"
        ]

    def get_data_values(self):
        return [
            str(self.Unknown1),
            str(self.Unknown2),
            hex(self.vertexBuffersOffset),
            str(self.Unknown3),
            str(self.Unknown4),
            str(self.Unknown5),
            hex(self.indexBuffersOffset),
            str(self.Unknown6),
            str(self.Unknown7),
            str(self.Unknown8),
            str(self.IndexCount),
            str(self.FaceCount),
            str(self.VertexCount),
            str(self.PrimitiveType),
            str(self.Unknown9),
            str(self.VertexStride),
            str(self.Unknown10),
            str(self.Unknown11),
            str(self.Unknown12),
            str(self.Unknown13)
        ]
    
    def __str__(self):
        return "Geometry"
