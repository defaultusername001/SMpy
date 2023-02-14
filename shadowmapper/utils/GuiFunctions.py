import tkinter as tk
import tkinter.messagebox as messagebox
import logging
import sys

class GuiFunctions:
    @staticmethod
    def set_look_and_feel():
        try:
            tk.Tk().tk.call('tk', 'setPalette', 'gray')
        except Exception as e:
            logging.error(f"Couldn't set look and feel: {e}")
    
    @staticmethod
    def center_window(root):
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f"{width}x{height}+{x}+{y}")

    @staticmethod
    def show_error(root, title, msg):
        messagebox.showerror(title, msg, parent=root)
