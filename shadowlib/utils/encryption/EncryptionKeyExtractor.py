### going to use hashlib here instead of the java stuff, havent tested it though
import hashlib
import configparser

class EncryptionKeyExtractor:
    def __init__(self):
        self.versionData = self.loadVersionData()

    def loadVersionData(self):
        try:
            config = configparser.ConfigParser()
            with open("versions.ini", "r") as f:
                config.read_file(f)
                return [
                    self.Version(
                        name = sectionName,
                        offset = int(config[sectionName]['offset'], 0)
                    )
                    for sectionName in config.sections()
                    if 'name' in config[sectionName] and 'offset' in config[sectionName]
                ]
        except Exception as ex:
            return []

    def getKey(self, gameDir):
        with open(gameDir + "GTAIV.exe", "rb") as f:
            key = bytearray(f.read(32))

        for version in self.versionData:
            with open(gameDir + version.name, "rb") as f:
                f.seek(version.offset)
                if hashlib.sha1(f.read(32)).hexdigest().upper() == 'DEA375EF1E6EF2223A1221C2C575C47BF17EFA5E':
                    return key

        return None

    class Version:
        def __init__(self, name, offset):
            self.name = name
            self.offset = offset
