from typing import Type
from pathlib import Path

class ImgLoader:
    @staticmethod
    def load(path: Path) -> Type[Img]:
        # TODO: there are no import links to any of the scripts yet, obviously fix this once they are all done
        raise NotImplementedError("ImgLoader.load() is not implemented")
