from Crypto.Cipher import AES

class Encrypter:
    def __init__(self, key: bytes):
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encryptAES(self, data: bytes) -> bytes:
        return self.cipher.encrypt(data)


#idk which cryptodome, cipher, pycryptodome f*ing works anymore, just find one and stick to it.