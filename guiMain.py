#the file to manage all of the GUI
from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("800x800")

frame = ttk.Frame(root, padding=10)
frame.grid()

root.mainloop()