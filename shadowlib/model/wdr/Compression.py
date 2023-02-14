import zlib

class Compression:
    def __init__(self):
        self.type = None

    def set_codec(self, type):
        self.type = type

    def compress(self, destination, source):
        compressed = zlib.compress(source)
        destination.write(compressed)

    def decompress(self, source, total_size):
        decompressed = zlib.decompress(source)
        return decompressed
