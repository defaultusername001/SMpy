import numpy as np
from OpenGL.GL import *

def to_gl(texture_dic, gl):
    texture_ids = np.zeros(len(texture_dic.textures), dtype=np.int32)
    glGenTextures(len(texture_dic.textures), texture_ids)

    for i, texture in enumerate(texture_dic.textures):
        texture.to_gl_texture(gl, texture_ids[i])
    
    return texture_ids

def to_gl_texture(texture, gl, texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)

    if texture.dxt_compression_type == "DXT1":
        compression_type = GL_COMPRESSED_RGB_S3TC_DXT1_EXT
    elif texture.dxt_compression_type == "DXT3":
        compression_type = GL_COMPRESSED_RGBA_S3TC_DXT3_EXT
    elif texture.dxt_compression_type == "DXT5":
        compression_type = GL_COMPRESSED_RGBA_S3TC_DXT5_EXT
    else:
        raise Exception("Unknown compression type")
    
    glCompressedTexImage2D(
        GL_TEXTURE_2D, 0, compression_type, texture.width, texture.height,
        0, len(texture.data), np.array(texture.data, np.uint8)
    )

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
