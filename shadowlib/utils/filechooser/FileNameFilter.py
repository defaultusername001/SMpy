import os
class FileNameFilter:
    
    def __init__(self, file_names, description):
        self.file_names = file_names
        self.description = description

    def accept(self, file_path):
        if os.path.isdir(file_path):
            return True
        return os.path.basename(file_path) in self.file_names

    def get_description(self):
        return f"{self.description} ({', '.join(self.file_names)})"

