import os
import sys
import handle_functions
# =================tkinter======================#
try:
    from tkinter import Tk, ttk, messagebox, IntVar, StringVar
except:
    print("Cannot import required Tkinter!")
    sys.exit()


class tab_info(ttk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.GUI_tab_info()

    def GUI_tab_info(self):

        self.text_info = ttk.Label(self, text="web scrape\nauthor: laomi3u\ncreated date: 29/04/2023")
        self.text_info.pack(fill="both", padx=20, pady=50)
