class Utils:
    @staticmethod
    def getHexString(value: int) -> str:
        hex_str = format(value, 'X')
        size = 4 if len(hex_str) <= 4 else 8
        hex_str = hex_str.zfill(size)
        return '0x' + hex_str

    @staticmethod
    def getShaderName(type_val: int) -> str:
        ret = "Unknown"
        if type_val == 0x2b5170fd:
            ret = "Texture"
        elif type_val == 0x608799c6:
            ret = "SpecularTexture"
        elif type_val == 0x46b7c64f:
            ret = "NormalTexture"
        elif type_val == -718597665:
            ret = "DiffuseMap1"
        elif type_val == 606121937:
            ret = "DiffuseMap2"
        elif type_val == -64241494:
            ret = "Vector"
        elif type_val == 376311761:
            ret = "Vector"
        elif type_val == 1212833469:
            ret = "Vector"
        elif type_val == -15634147:
            ret = "Vector"
        elif type_val == -160355455:
            ret = "Vector"
        elif type_val == -2078982697:
            ret = "Vector"
        elif type_val == -677643234:
            ret = "Vector"
        elif type_val == -1168850544:
            ret = "Vector"
        elif type_val == 424198508:
            ret = "Vector"
        elif type_val == 514782960:
            ret = "Vector"
        elif type_val == -260861532:
            ret = "Matrix"
        ret += " ({})".format(type_val)
        return ret

    @staticmethod
    def getShaderType(type_val: int) -> str:
        ret = "Unknown {}".format(type_val)
        if type_val == 0:
            ret = "Texture"
        elif type_val == 4:
            ret = "Matrix"
        elif type_val == 1:
            ret = "Vector"
        return ret

    def get_file_type(file_name: str) -> int:
        file_name = file_name.lower()
        if file_name.endswith('.dff'):
            return Constants.ftDFF
        elif file_name.endswith('.txd'):
            return Constants.ftTXD
        elif file_name.endswith('.col'):
            return Constants.ftCOL
        elif file_name.endswith('.ipl'):
            return Constants.ftIPL
        elif file_name.endswith('.ide'):
            return Constants.ftIDE
        elif file_name.endswith('.wdr'):
            return Constants.ftWDR
        elif file_name.endswith('.wdd'):
            return Constants.ftWDD
        elif file_name.endswith('.wbn'):
            return Constants.ftWBN
        elif file_name.endswith('.wbd'):
            return Constants.ftWBD
        elif file_name.endswith('.wtd'):
            return Constants.ftWTD
        elif file_name.endswith('.wft'):
            return Constants.ftWFT
        elif file_name.endswith('.wad'):
            return Constants.ftWAD
        elif file_name.endswith('.wpl'):
            return Constants.ftWPL
        elif file_name.endswith('.ifp'):
            return Constants.ftIFP
        else:
            return -1

    def get_resource_type(file_name: str) -> int:
        file_name = file_name.lower()
        if file_name.endswith('.wdr'):
            return Constants.rtWDR
        elif file_name.endswith('.wdd'):
            return Constants.rtWDD
        elif file_name.endswith('.wbn'):
            return Constants.rtWBN
        elif file_name.endswith('.wbd'):
            return Constants.rtWBD
        elif file_name.endswith('.wtd'):
            return Constants.rtWTD
        elif file_name.endswith('.wft'):
            return Constants.rtWFT
        elif file_name.endswith('.wad'):
            return Constants.rtWAD
        elif file_name.endswith('.wpl'):
            return Constants.rtWPL
        else:
            return -1

    def get_total_mem_size(flags: int) -> int:
        return (get_system_mem_size(flags) + get_graphics_mem_size(flags))

    def get_system_mem_size(flags: int) -> int:
        return (flags & 0x7FF) << (((flags >> 11) & 0xF) + 8)

    def get_graphics_mem_size(flags: int) -> int:
        return ((flags >> 15) & 0x7FF) << (((flags >> 26) & 0xF) + 8)

        #constants not defined somewhere, mem_size is in the other files dw