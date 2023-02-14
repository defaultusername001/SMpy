class ImgV1(ImgLoader):
    def load(self, path: Path) -> Type[Img]:
        items = []

        with open(f"{path.stem}.dir", "rb") as file:
            while True:
                item_offset = int.from_bytes(file.read(4), "little") * 2048
                item_size = int.from_bytes(file.read(4), "little") * 2048
                item_name = file.read(24).rstrip(b'\x00').decode()
                item_type = Utils.getFileType(item_name)
                item = ImgItem(item_name)
                item.offset = item_offset
                item.size = item_size
                item.type = item_type
                items.append(item)
                if file.read(1) == b'':
                    break

        return Img(items=items, path=path)