import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FileChooserUtil:
    
    @staticmethod
    def open_file_chooser(parent, file_types, initial_dir=None):
        file_path = filedialog.askopenfilename(
            initialdir=initial_dir,
            title="Open file..",
            filetypes=file_types,
            parent=parent
        )
        if file_path:
            return file_path
        else:
            return None
