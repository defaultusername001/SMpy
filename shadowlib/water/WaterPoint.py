class WaterPoint:
    
    def __init__(self, line):
        split = line.split()
        self.coord = Vector3D(float(split[0]), float(split[1]), float(split[2]))
        self.speedX = float(split[3])
        self.speedY = float(split[4])
        self.unknown = float(split[5])
        self.waveHeight = float(split[6])
