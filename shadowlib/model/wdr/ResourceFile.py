class ResourceFile:
    def __init__(self):
        self._header = None
        self._codec = None

    def read(self, br, file_size):
        self._header = ResourceHeader()
        self._header.read(br)

        if self._header.Magic != ResourceHeader.MagicValue:
            raise Exception("Invalid resource file")

        self._codec = Compression()

        if self._header.CompressCodec == LZX:
            self._codec.set_codec(self._header.CompressCodec)
        elif self._header.CompressCodec == Deflate:
            self._codec.set_codec(self._header.CompressCodec)
        else:
            pass

        total_mem_size = self._header.get_system_mem_size() + self._header.get_graphics_mem_size()

        if file_size == -1:
            file_size = br.more_to_read()

        stream = self._codec.decompress(br.to_array(br.get_current_offset(), br.more_to_read()), total_mem_size)
        return stream

    def get_graphic_size(self):
        return self._header.get_graphics_mem_size()

    def get_system_size(self):
        return self._header.get_system_mem_size()


#you dont need to redefine LZX and Deflate here, its in the compression.py