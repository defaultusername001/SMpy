from Crypto.Cipher import AES
import logging

class Decrypter:
    def __init__(self, key: bytes):
        self.cipher = AES.new(key, AES.MODE_ECB)
    #ECBlocks are done 16x, im not sure if this is right
    def decrypt16byteBlock(self, rf):
        tempBuffer = bytearray(16) 
        rf.readinto(tempBuffer)
        for j in range(16):  
            try:
                tempBuffer = self.cipher.decrypt(tempBuffer)
            except Exception as ex:
                logging.getLogger('ImgV3').error(ex)
        return tempBuffer

    def decrypt(self, data: bytes):
        tempData = bytearray(data)
        for j in range(16):  
            try:
                tempData = self.cipher.decrypt(tempData)
            except Exception as ex:
                logging.getLogger('ImgV3').error(ex)
        return tempData
### here it is again but using java, which I dont want to do 

from javax.crypto import Cipher
from javax.crypto.spec import SecretKeySpec
from java.util.logging import Level, Logger

class Decrypter:
    def __init__(self, key):
        self.cipher = Cipher.getInstance("Rijndael/ECB/NoPadding")
        self.cipher.init(Cipher.DECRYPT_MODE, SecretKeySpec(key, "Rijndael"))
        self.tempBuffer = bytearray(16)

    def decrypt16byteBlock(self, rf):
        rf.readBytes(self.tempBuffer)
        for j in range(16): 
            try:
                self.tempBuffer = self.cipher.doFinal(self.tempBuffer)
            except Exception as ex:
                Logger.getLogger("ImgV3").log(Level.SEVERE, None, ex)
        return self.tempBuffer

    def decrypt(self, data):
        tempData = bytearray(data)
        for j in range(16):
            try:
                tempData = self.cipher.doFinal(tempData)
            except Exception as ex:
                Logger.getLogger("ImgV3").log(Level.SEVERE, None, ex)
        return tempData
