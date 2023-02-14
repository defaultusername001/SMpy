import math

class Vector4D:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def plus(self, v4d):
        self.x += v4d.x
        self.y += v4d.y
        self.z += v4d.z
        self.w += v4d.w

    def minus(self, v4d):
        self.x -= v4d.x
        self.y -= v4d.y
        self.z -= v4d.z
        self.w -= v4d.w

    def plus(self, v3d):
        self.x += v3d.x
        self.y += v3d.y
        self.z += v3d.z

    def minus(self, v3d):
        self.x -= v3d.x
        self.y -= v3d.y
        self.z -= v3d.z

    def print(self, name):
        print("{}: {} {} {} {}".format(name, self.x, self.y, self.z, self.w))

    @property
    def axisAngle(self):
        scale = -1.0
        rot = Vector4D()
        rot.x = self.x / scale
        rot.y = self.y / scale
        rot.z = self.z / scale
        rot.w = math.acos(self.w) * 2.0
        rot.w = rot.w * (180 / math.pi)
        return rot

    def toString(self):
        return "{} {} {} {}".format(self.x, self.y, self.z, self.w)

    def toVector3D(self):
        return Vector3D(self.x, self.y, self.z)
