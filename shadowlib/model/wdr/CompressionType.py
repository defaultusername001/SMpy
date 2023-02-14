from enum import Enum

class CompressionType(Enum):
    LZX = 0xF505
    Deflate = 0xDA78
#idk what this language means in the comment lol, its trivial compression
    @classmethod
    def get(cls, type):
        if type == 0xF505:
            return cls.LZX
        elif type == 0xDA78:
            return cls.Deflate
        else:
            return cls.LZX
