import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def plus(self, v3d):
        self.x += v3d.x
        self.y += v3d.y
        self.z += v3d.z

    def minus(self, v3d):
        self.x -= v3d.x
        self.y -= v3d.y
        self.z -= v3d.z

    def times(self, v3d):
        self.x *= v3d.x
        self.y *= v3d.y
        self.z *= v3d.z

    def toString(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)
