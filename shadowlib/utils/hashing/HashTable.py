class HashTable:
    def __init__(self, hasher):
        self.hasher = hasher
        self.hashes = {}
        self.missedHashCount = 0

    def add(self, value):
        hash_value = self.hasher.hash(value)
        self.hashes[hash_value] = value

    def addhash(self, hash_value, value):
        if hash_value not in self.hashes:
            print(f"Hash was not generated by IDE entries '{value}'")
            self.missedHashCount += 1
        self.hashes[hash_value] = value

    def get(self, hash_value):
        return self.hashes.get(hash_value)