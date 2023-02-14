class ImgLoaderFactory:
    @staticmethod
    def getImgLoader(game_type, encryption_key=None):
        if game_type == GameType.GTA_III:
            return ImgV1()
        elif game_type == GameType.GTA_VC:
            return ImgV1()
        elif game_type == GameType.GTA_SA:
            return ImgV2()
        elif game_type == GameType.GTA_IV:
            if encryption_key is None:
                raise ValueError("Encryption key is required to load GTA: IV images")
            return ImgV3(encryption_key)
        else:
            raise ValueError(f"GameType is unknown '{game_type}'")
