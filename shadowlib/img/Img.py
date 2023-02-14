from pathlib import Path
from typing import List, Optional

class Img:
    def __init__(self, path: Path, items: List[ImgItem]=None, isEncrypted: bool=False):
        self.path = path
        self.items = items or []
        self.isEncrypted = isEncrypted
        self._save_required = False

    @property
    def fileName(self):
        return self.path.name

    def toggleEncryption(self, enabled: bool):
        if self.isEncrypted != enabled:
            self.isEncrypted = enabled
            self._save_required = True

    @property
    def totalItemCount(self):
        return len(self.items)

    def getItemsOfType(self, extension: str) -> List[ImgItem]:
        return [item for item in self.items if item.name.endswith(extension)]

    def getItemOfTypeCount(self, extension: str) -> int:
        return len([item for item in self.items if item.name.endswith(extension)])

    def findItemIndex(self, name: str) -> int:
        for i, item in enumerate(self.items):
            if item.name == name:
                return i
        return -1

    def findItem(self, name: str) -> Optional[ImgItem]:
        for item in self.items:
            if item.name == name:
                return item
        return None

    def addItem(self, path: Path):
        if path.is_file() and path.exists():
            with open(path, "rb") as file:
                new_file = file.read()
            temp_item = ImgItem(path.name)
            temp_item.type = Utils.getResourceType(path.name)
            temp_item.offset = len(self.items)
            temp_item.size = len(new_file)
            if temp_item.isResource:
                temp_item.flags = ... # Add code to read the flags
            self.items.append(temp_item)
            with open(self.path, "ab") as file:
                file.write(new_file)
            self._save_required = True

    def removeItem(self, img_item: ImgItem):
        self.items.remove(img_item)
        self._save_required = True

    def save(self):
        # TODO: Implement IMG saving
        raise NotImplementedError("IMG Saving is not implemented")

    @classmethod
    def createNewImg(cls, path: Path):
        return cls(path)
