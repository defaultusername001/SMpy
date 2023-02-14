import hashlib

class SHA1Hasher:
    
    @staticmethod
    def hash(input_data: bytes) -> str:
        try:
            sha1 = hashlib.sha1()
            sha1.update(input_data)
            return sha1.hexdigest()
        except Exception as ex:
            return None
