class WaterPlane:
    
    def __init__(self, line):
        self.points = [None, None, None, None]
        self.param = 0
        self.unknown = 0.0
        self.selected = False
        self.u = 0.0
        self.v = 1.0

        split = line.split("   ")
        for i in range(len(split)):
            self.points[i] = WaterPoint(split[i])
        
        sub_split = split[3].split(" ")
        self.param = int(sub_split[7])
        self.unknown = float(sub_split[8])
        
        self.v = self.points[0].coord.x - self.points[1].coord.x
        if self.v < 0:
            self.v *= -1
        self.v /= 10
