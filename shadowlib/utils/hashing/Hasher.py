from abc import ABC, abstractmethod

class Hasher(ABC):
    @abstractmethod
    def hash(self, value: str) -> int: #int can do long here
        pass
