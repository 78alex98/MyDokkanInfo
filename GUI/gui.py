# This File Contains All the Functions Related to the GUI
# All GUI is done through tkinter

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Global Variables
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

def CreateApp():
    # Create a Window
    window = ctk.CTk()
    window.title('MyDokkanInfo')
    window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.resizable(True, True)

    # Main Menu Frame
    main_frame = ctk.CTkFrame(master=window)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=25)
    main_frame.rowconfigure((1,3), weight=10)
    main_frame.rowconfigure(2, weight=1)
    main_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    main_frame.grid_propagate(False)

    # Menu Bar Frame
    CreateMenuBar(main_frame, 0, 0, 10, 10)

    # Title Frame
    title_frame = ctk.CTkFrame(master=main_frame)
    title_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    title_frame.rowconfigure(0, weight=1)
    title_frame.columnconfigure(0, weight=1)
    title_frame.grid_propagate(False)

    welcome_label = ctk.CTkLabel(master=title_frame, text='Welcome to\nMyDokkanInfo!', font=('', 30))
    welcome_label.grid(row=0, column=0, pady=10, sticky='')

    # Recent Cards Frame
    recent_frame = ctk.CTkFrame(master=main_frame)
    recent_frame.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
    recent_frame.grid_propagate(False)

    # Footer Frame
    footer_frame = ctk.CTkFrame(master=main_frame)
    footer_frame.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')
    footer_frame.grid_propagate(False)

    # Run GUI
    window.mainloop()

def CreateMenuBar(master, mb_row, mb_column, pad_x, pad_y):
    menubar_color = 'gray'
    menubar_innercolor = 'gray'
    menubar_inner_pad = 5

    menu_frame = ctk.CTkFrame(master=master, fg_color=menubar_color)
    menu_frame.grid(row=mb_row, column=mb_column, padx=pad_x, pady=pad_y, sticky='nsew')
    menu_frame.rowconfigure(0, weight=1)
    menu_frame.columnconfigure((0,1,2,3,4), weight=1)
    menu_frame.grid_propagate(False)

    home_menu = ctk.CTkButton(master=menu_frame, text='Home', fg_color=menubar_innercolor)
    home_menu.grid(row=0, column=0, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    card_menu = ctk.CTkButton(master=menu_frame, text='Cards', fg_color=menubar_innercolor)
    card_menu.grid(row=0, column=1, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    team_menu = ctk.CTkButton(master=menu_frame, text='Teams', fg_color=menubar_innercolor)
    team_menu.grid(row=0, column=2, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    cat_menu = ctk.CTkButton(master=menu_frame, text='Categories', fg_color=menubar_innercolor)
    cat_menu.grid(row=0, column=3, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    links_menu = ctk.CTkButton(master=menu_frame, text='Links', fg_color=menubar_innercolor)
    links_menu.grid(row=0, column=4, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')