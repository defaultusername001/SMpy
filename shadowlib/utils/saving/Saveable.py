from abc import ABC, abstractmethod

class Saveable(ABC):
    
    @property
    @abstractmethod
    def is_save_required(self) -> bool:
        pass
    
    @abstractmethod
    def set_save_required(self):
        pass
    
    @abstractmethod
    def set_save_required(self, is_save_required: bool):
        pass

class SaveableFile(Saveable):
    
    def __init__(self):
        self._is_save_required = False

    @property
    def is_save_required(self) -> bool:
        return self._is_save_required
    
    def set_save_required(self):
        self._is_save_required = True
    
    def set_save_required(self, is_save_required: bool):
        self._is_save_required = is_save_required
