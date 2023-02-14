from collections import LinkedList

class FragTypeModel:
    def __init__(self):
        self.VTable = 0
        self.blockMapAdress = 0
        self.offset1 = 0
        self.offset2 = 0
        self.drawables = LinkedList()

    def read(self, br):
        print("--------------------\nHeader\n--------------------")
        self.VTable = br.readUInt32()
        print("VTable: " + str(self.VTable))
        self.blockMapAdress = br.readOffset()
        print("Block: " + Utils.getHexString(self.blockMapAdress))

        unkFloat1 = br.readFloat()
        unkFloat2 = br.readFloat()
        print("UNKFloat1: " + str(unkFloat1))
        print("UNKFloat2: " + str(unkFloat2))

        for i in range(10):
            br.readVector4D().print("UNK Vec" + str(i))

        self.offset1 = br.readOffset()
        self.offset2 = br.readOffset()
        print("PackString Offset: " + Utils.getHexString(self.offset1))
        save = br.getCurrentOffset()
        br.setCurrentOffset(self.offset1)
        print("PackString: " + br.readNullTerminatedString())
        br.setCurrentOffset(save)

        print("Drawable: " + Utils.getHexString(self.offset2))
        save = br.getCurrentOffset()
        br.setCurrentOffset(self.offset2)

        drwbl = DrawableModel()
        drwbl.readSystemMemory(br)
        self.drawables.add(drwbl)

        br.setCurrentOffset(save)

        zero1 = br.readUInt32()
        zero2 = br.readUInt32()
        zero3 = br.readUInt32()
        max1 = br.readUInt32()
        zero4 = br.readUInt32()
        print("Zero1: " + str(zero1))
        print("Zero2: " + str(zero2))
        print("Zero3: " + str(zero3))
        print("Max1: " + str(max1))
        print("Zero4: " + str(zero4))

        offset3 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset3))
        save = br.getCurrentOffset()
        br.setCurrentOffset(offset3)
        off = br.readOffset()
        print("Off = " + Utils.getHexString(off))
        while off != -1:
            save2 = br.getCurrentOffset()
            br.setCurrentOffset(off)
            name = br.readNullTerminatedString()
            print("Name: " + name)
            br.setCurrentOffset(save2)
            print(Utils.getHexString(br.getCurrentOffset()))
            off = br.readOffset()
        br.setCurrentOffset(save)
        offset4 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset4))
        childListOffset = br.readOffset()
        print("ChildListOffset: " + Utils.getHexString(childListOffset))

        zero5 = br.readUInt32()
        zero6 = br.readUInt32()
        zero7 = br.readUInt32()

        offset6 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset6))

        zero8 = br.readUInt32()

        offset7 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset7))
        offset8 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset8))
        offset9 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset9))
        offset10 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset10))

        zero9 = br.readUInt32()
        zero10 = br.readUInt32()
        zero11 = br.readUInt32()

        offset11 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset11))
        zero12 = br.readUInt32()
        zero13 = br.readUInt32()
        zero14 = br.readUInt32()
        zero15 = br.readUInt32()

        offset12 = br.readOffset()
        print("Unk offset: " + Utils.getHexString(offset12))

        print("--------------------\nChildList\n--------------------")
        save = br.getCurrentOffset()
        br.setCurrentOffset(childListOffset)
        childOffset = br.readOffset()
        while childOffset != -1:
            save2 = br.getCurrentOffset()
            print("ChildOffset: " + Utils.getHexString(childOffset))
            if childOffset < 0x0F0000:
                br.setCurrentOffset(childOffset)
                ftc = FragTypeChild(br)
                if ftc.drwblOffset != -1:
                    br.setCurrentOffset(ftc.drwblOffset)
                    drwbl = DrawableModel()
                    drwbl.readSystemMemory(br)
                    drawables.append(drwbl)
                br.setCurrentOffset(save2)
            childOffset = br.readOffset()
        br.setCurrentOffset(save)
