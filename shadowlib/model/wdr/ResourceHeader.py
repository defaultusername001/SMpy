class ResourceHeader:
    MagicBigEndian = 0x52534305
    MagicValue = 0x05435352

    def __init__(self):
        self.Magic = None
        self.Type = None
        self.Flags = None
        self.CompressCodec = None

    def get_system_mem_size(self):
        return (self.Flags & 0x7FF) << (((self.Flags >> 11) & 0xF) + 8)

    def get_graphics_mem_size(self):
        return ((self.Flags >> 15) & 0x7FF) << (((self.Flags >> 26) & 0xF) + 8)

    def set_mem_sizes(self, system_mem_size, graphics_mem_size):
        max_a = 0x3F
        sys_a = system_mem_size >> 8
        sys_b = 0

        while sys_a > max_a:
            if (sys_a & 1) != 0:
                sys_a += 2
            sys_a >>= 1
            sys_b += 1

        gfx_a = graphics_mem_size >> 8
        gfx_b = 0

        while gfx_a > max_a:
            if (gfx_a & 1) != 0:
                gfx_a += 2
            gfx_a >>= 1
            gfx_b += 1

        self.Flags = (self.Flags & 0xC0000000) | (sys_a | (sys_b << 11) | (gfx_a << 15) | (gfx_b << 26))

    def read(self, br):
        self.Magic = br.read_uint32()
        type = br.read_uint32()
        self.Type = ResourceType.get(type)
        self.Flags = br.read_uint32()
        self.CompressCodec = CompressionType.get(br.read_uint16())

    def read_2(self, rf):
        self.Magic = rf.read_int()
        type = rf.read_int()
        self.Type = ResourceType.get(type)
        self.Flags = rf.read_int()
        self.CompressCodec = CompressionType.get(rf.read_short())