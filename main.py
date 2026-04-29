import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
Uname = simpledialog.askstring(title="Flages quiz",
 prompt="Please enter your username",
 prompt="Welcome to my flages quiz",)
score = 0
