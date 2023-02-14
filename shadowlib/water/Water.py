import logging

class Water:
    
    def __init__(self, file_name, game_type):
        self.file_name = file_name
        self.game_type = game_type
        self.planes = []
        self.read()

    def read(self):
        with open(self.file_name) as input_file:
            for line in input_file:
                print(line.strip())
                wp = WaterPlane(line.strip())
                self.planes.append(wp)

    def get_planes(self):
        return self.planes

class WaterPlane:
    
    def __init__(self, data):
        pass
