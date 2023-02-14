import os
class ExtensionFilter:
    
    def __init__(self, extensions, description):
        self.extensions = extensions
        self.description = description

    def accept(self, file_path):
        if os.path.isdir(file_path):
            return True
        return os.path.splitext(file_path)[1] in self.extensions

    def get_description(self):
        return f"{self.description} ({', '.join(self.extensions)})"

