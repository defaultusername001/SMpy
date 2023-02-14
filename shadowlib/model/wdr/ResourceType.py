from enum import Enum

class ResourceType(Enum):
    TextureXBOX = 0x7
    ModelXBOX = 0x6D
    Generic = 0x01
    Bounds = 0x20
    Particles = 0x24
    Particles2 = 0x1B
    Texture = 0x8
    Model = 0x6E
    ModelFrag = 0x70

    @classmethod
    def get(cls, type):
        return cls.Model
