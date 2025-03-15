# This File Contains All the Functions Related to the GUI
# All GUI is done through tkinter

import tkinter as tk
from tkinter import ttk

def CreateApp():
    # Create a Window
    window = tk.Tk()
    window.title('MyDokkanInfo')
    window.geometry('800x500')

    label = ttk.Label(master=window, text='This is my Application!')
    label.pack()

    # Run GUI
    window.mainloop()