from abc import ABC, abstractmethod

class IplItem(ABC): #ive never used abstract base classes lol, i think this is right? is it even necessary?
    @abstractmethod
    def read(self, line):
        pass

    @abstractmethod
    def read(self, rf):
        pass

    @abstractmethod
    def read(self, rf, hash_table):
        pass
