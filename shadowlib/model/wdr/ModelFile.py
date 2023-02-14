def add_vertices(mdl, stream, vert_offset, poly_offset, vert_size, poly_size, stride_size, mat_index):
    def arr2float(mini_arr):
        return struct.unpack('f', bytes(mini_arr))[0]

    for i in range(vert_size):
        mini_arr = [0, 0, 0, 0]
        mini_arr[0] = stream[vert_offset + (i * stride_size)]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 1]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 2]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 3]
        x = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 4]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 5]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 6]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 7]
        y = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 8]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 9]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 10]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 11]
        z = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 12]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 13]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 14]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 15]
        normx = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 16]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 17]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 18]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 19]
        normy = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 20]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 21]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 22]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 23]
        normz = arr2float(mini_arr)
        unk1 = stream[vert_offset + (i * stride_size) + 24]
        unk2 = stream[vert_offset + (i * stride_size) + 25]
        unk3 = stream[vert_offset + (i * stride_size) + 26]
        unk4 = stream[vert_offset + (i * stride_size) + 27]
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 28]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 29]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 30]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 31]
        u = arr2float(mini_arr)
        mini_arr[0] = stream[vert_offset + (i * stride_size) + 32]
        mini_arr[1] = stream[vert_offset + (i * stride_size) + 33]
        mini_arr[2] = stream[vert_offset + (i * stride_size) + 34]
        mini_arr[3] = stream[vert_offset + (i * stride_size) + 35]
        v = arr2float(mini_arr)

        mdl.add_vertex_to_strip(x, y, z, u, v, mat_index)
        mdl.create_model_vertex(i, x, y, z, u, v)

def add_polygons(mdl, stream, vert_offset, poly_offset, vert_size, poly_size, stride_size, mat_index):
    for i in range(poly_size):
        mini_arr = bytearray(2)
        mini_arr[0] = stream[poly_offset + (i * 6)]
        mini_arr[1] = stream[poly_offset + (i * 6) + 1]
        a = arr2int(mini_arr)
        mini_arr[0] = stream[poly_offset + (i * 6) + 2]
        mini_arr[1] = stream[poly_offset + (i * 6) + 3]
        b = arr2int(mini_arr)
        mini_arr[0] = stream[poly_offset + (i * 6) + 4]
        mini_arr[1] = stream[poly_offset + (i * 6) + 5]
        c = arr2int(mini_arr)

        mdl.create_model_poly(a, b, c, mat_index, False)


def arr2float(arr):
    accum = 0
    for i, shift_by in enumerate(range(0, 32, 8)):
        accum |= (arr[i] & 0xff) << shift_by
    return struct.unpack('f', struct.pack('i', accum))[0]


def arr2int(arr):
    low = arr[0] & 0xff
    high = arr[1] & 0xff
    return high << 8 | low


def float2arr(f):
    n = struct.unpack('i', struct.pack('f', f))[0]
    return struct.pack('i', n)


def short2arr(i):
    s = i & 0xffff
    return struct.pack('h', s)
