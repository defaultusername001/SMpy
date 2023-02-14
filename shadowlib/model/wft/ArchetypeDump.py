class ArchetypeDamp:
    def read(self, br):
        VTable = br.readUInt32()
        print("VTable: " + str(VTable))
