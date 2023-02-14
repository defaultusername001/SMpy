from enum import Enum

class GameType(Enum):
    GTA_III = ("III", "GTA III", "gta3.exe")
    GTA_VC = ("VC", "GTA VC", "gta-vc.exe")
    GTA_SA = ("SA", "GTA SA", "gta-sa.exe")
    GTA_IV = ("IV", "GTA IV", "GTAIV.exe")
    GTA_V = ("V", "GTA V", "GTA5.exe")

    def __init__(self, id, gameName, executableName):
        self.id = id
        self.gameName = gameName
        self.executableName = executableName

    @staticmethod
    def byId(id):
        if id == "III":
            return GameType.GTA_III
        elif id == "VC":
            return GameType.GTA_VC
        elif id == "SA":
            return GameType.GTA_SA
        elif id == "IV":
            return GameType.GTA_IV
        elif id == "V":
            return GameType.GTA_V
        else:
            return None
