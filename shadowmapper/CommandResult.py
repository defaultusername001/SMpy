from enum import Enum

class CommandResult(Enum):
    SUCCESS = 1
    FAILED = 2
    
    def __init__(self, error=None):
        self.error = error
