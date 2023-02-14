from struct import unpack

class Vector4D:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def print(self, name):
        print(f"{name}: ({self.x}, {self.y}, {self.z}, {self.w})")

class ByteReader:
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def read_uint32(self):
        value, = unpack("<I", self.data[self.offset:self.offset+4])
        self.offset += 4
        return value

    def read_float(self):
        value, = unpack("<f", self.data[self.offset:self.offset+4])
        self.offset += 4
        return value

    def read_vector4d(self):
        values = unpack("<ffff", self.data[self.offset:self.offset+16])
        self.offset += 16
        return Vector4D(*values)

    def read_offset(self):
        value = self.read_uint32()
        if value != 0:
            value += self.offset - 4
        return value

    def set_current_offset(self, offset):
        self.offset = offset

class DrawableModel:
    def __init__(self, data):
        self.start_offset = 0
        self.shader_group = None
        self.skeleton = None
        self.shader_group_offset = 0
        self.skeleton_offset = 0
        self.center = None
        self.bounds_min = None
        self.bounds_max = None
        self.model_offsets = []
        self.level_of_detail_count = 0
        self.model_collection = []
        self.absolute_max = None
        self.unk1 = None
        self.neg1 = None
        self.neg2 = None
        self.neg3 = None
        self.unk2 = None
        self.unk3 = None
        self.unk4 = None
        self.unk5 = None
        self.unk6 = None
        self.unk7 = None

        br = ByteReader(data)

        self.start_offset = br.offset

        vtable = br.read_uint32()
        offset = br.read_offset()

        self.shader_group_offset = br.read_offset()
        self.skeleton_offset = br.read_offset()

        self.center = br.read_vector4d()
        self.center.print("Center")
        self.bounds_min = br.read_vector4d()
        self.bounds_min.print("BoundsMin")
        self.bounds_max = br.read_vector4d()
        self.bounds_max.print("BoundsMax")

        #idk what you did here, fix this, below this is a mess and wrong.
        self.level_of_detail_count = 0
        self.model_offsets = [br.read_offset() for i in range(4)]
        for i in range(4):
            self.model_offsets[i] = br.read_offset()
            if self.model_offsets[i] != 0:
                levelOfDetailCount += 1

        AbsoluteMax = br.read_vector_4d()
        AbsoluteMax.print("AbsoluteMax")

        Unk1 = br.read_uint32()

        Neg1 = br.read_uint32()
        Neg2 = br.read_uint32()
        Neg3 = br.read_uint32()

        Unk2 = br.read_float()

        Unk3 = br.read_uint32()
        Unk4 = br.read_uint32()
        Unk5 = br.read_uint32()

        Unk6 = br.read_uint32()
        Unk7 = br.read_uint32()

        if self.shader_group_offset != 0:
            br.set_current_offset(self.shader_group_offset)
            shaderGroup = ShaderGroup(br)

        if self.skeleton_offset != 0:
            br.set_current_offset(self.skeleton_offset)
            skeleton = self.skeleton()

        mModelCollection = [0] * levelOfDetailCount
        for i in range(levelOfDetailCount):
            print("PointerCollectionOffset:", self.model_offsets[i])
            br.set_current_offset(self.model_offsets[i])
            mModelCollection[i] = self.ptr(br, 1)

    def get_data_names(self):
    names = [0] * (17 + levelOfDetailCount)
    i = 0
    names[i] = "shaderGroupOffset"
    i += 1
    names[i] = "skeletonOffset"
    i += 1
    names[i] = "Center"
    i += 1
    names[i] = "BoundsMin"
    i += 1
    names[i] = "BoundsMax"
    i += 1

    names[i] = "levelOfDetailCount"
    i += 1

    for i2 in range(levelOfDetailCount):
        names[i] = "  DetailOffset " + str(i2 + 1)
        i += 1

    names[i] = "AbsoluteMax"
    i += 1

    names[i] = "Unk1"     # either 1 or 9
    i += 1

    names[i] = "Neg1"
    i += 1
    names[i] = "Neg2"
    i += 1
    names[i] = "Neg3"
    i += 1

    names[i] = "Unk2"
    i += 1

    names[i] = "Unk3"
    i += 1
    names[i] = "Unk4"
    i += 1
    names[i] = "Unk5"
    i += 1

    names[i] = "Unk6"  # This should be a CSimpleCollection
    i += 1
    names[i] = "Unk7"

    return names

    def get_data_values(self):
        values = [0] * (17 + levelOfDetailCount)
        i = 0
        values[i] = Utils.get_hex_string(shaderGroupOffset)
        i += 1
        values[i] = Utils.get_hex_string(skeletonOffset)
        i += 1

        values[i] = str(Center)
        i += 1
        values[i] = str(BoundsMin)
        i += 1
        values[i] = str(BoundsMax)
        i += 1

        values[i] = str(levelOfDetailCount)
        i += 1

        for i2 in range(levelOfDetailCount):
            values[i] = Utils.get_hex_string(modelOffsets[i2])
            i += 1

        values[i] = str(AbsoluteMax)
        i += 1

        values[i] = str(Unk1)     # either 1 or 9
        i += 1

        values[i] = str(Neg1)
        i += 1
        values[i] = str(Neg2)
        i += 1
        values[i] = str(Neg3)
        i += 1

        values[i] = str(Unk2)
        i += 1

        values[i] = str(Unk3)
        i += 1
        values[i] = str(Unk4)
        i += 1
        values[i] = str(Unk5)
        i += 1   
        values[i] = str(Unk6)
        i += 1   
        values[i] = str(Unk7)
        i += 1
        return values  