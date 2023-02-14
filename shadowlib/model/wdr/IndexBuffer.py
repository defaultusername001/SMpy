class IndexBuffer:
    def __init__(self, br):
        self.start_offset = None
        self.VTable = None
        self.IndexCount = None
        self.DataOffset = None
        self.p1_offset = None
        self.RawData = None
        self.read(br)

    def read(self, br):
        self.start_offset = br.get_current_offset()
        self.VTable = br.read_uint32()
        self.IndexCount = br.read_uint32()
        self.DataOffset = br.read_data_offset()
        self.p1_offset = br.read_offset()
        self.read_data(br)

    def read_data(self, br):
        br.set_system_memory(False)
        br.set_current_offset(self.DataOffset)
        self.RawData = br.to_array(self.IndexCount * 2)
        br.set_system_memory(True)

    def get_data_names(self):
        return [
            "IndexCount",
            "DataOffset",
            "p1Offset",
            "RawData(Length)"
        ]

    def get_data_values(self):
        return [
            str(self.IndexCount),
            hex(self.DataOffset),
            hex(self.p1_offset),
            str(len(self.RawData))
        ]
