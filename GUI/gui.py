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

    # By Default, Launch With Main Menu Page
    current_page = CreateMainMenuPage(window)

    # Run GUI
    window.mainloop()

def CreateMainMenuPage(master):
    # Main Menu Frame
    main_frame = ctk.CTkFrame(master=master)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=0)
    main_frame.rowconfigure(1, weight=10)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=0)
    main_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    main_frame.grid_propagate(False)

    # Menu Bar Frame
    CreateMenuBar(main_frame, 0, 0, 10, 10, master)

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

    CreateFooterBar(main_frame, 3, 0, 10, 10)

    # Return Whole Page
    return main_frame

def CreateCardListPage(master):
    # Main Menu Frame
    main_frame = ctk.CTkFrame(master=master)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=0)
    main_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
    main_frame.grid_propagate(False)

    # Menu Bar Frame
    CreateMenuBar(main_frame, 0, 0, 10, 10, master)

    return main_frame

def CreateMenuBar(master, mb_row, mb_column, pad_x, pad_y, window):
    menubar_color = 'gray'
    menubar_innercolor = 'gray'
    menubar_inner_pad = 5
    menubar_height = 50

    menu_frame = ctk.CTkFrame(master=master, height=menubar_height, fg_color=menubar_color)
    menu_frame.grid(row=mb_row, column=mb_column, padx=pad_x, pady=pad_y, sticky='nsew')
    menu_frame.rowconfigure(0, weight=1)
    menu_frame.columnconfigure((0,1,2,3,4), weight=1)
    menu_frame.grid_propagate(False)

    home_menu = ctk.CTkButton(master=menu_frame, text='Home', fg_color=menubar_innercolor, command = lambda : SwitchToHome(window, master))
    home_menu.grid(row=0, column=0, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    card_menu = ctk.CTkButton(master=menu_frame, text='Cards', fg_color=menubar_innercolor, command = lambda : SwitchToCardList(window, master))
    card_menu.grid(row=0, column=1, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    team_menu = ctk.CTkButton(master=menu_frame, text='Teams', fg_color=menubar_innercolor)
    team_menu.grid(row=0, column=2, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    cat_menu = ctk.CTkButton(master=menu_frame, text='Categories', fg_color=menubar_innercolor)
    cat_menu.grid(row=0, column=3, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')
    links_menu = ctk.CTkButton(master=menu_frame, text='Links', fg_color=menubar_innercolor)
    links_menu.grid(row=0, column=4, padx=menubar_inner_pad, pady=menubar_inner_pad, sticky='ew')

def CreateFooterBar(master, mb_row, mb_column, pad_x, pad_y):
    footerbar_color = 'transparent'
    footerbar_innercolor = 'transparent'
    footerbar_inner_padx = 30
    footerbar_inner_pady = 0
    footerbar_height = 40

    # Footer Frame
    footer_frame = ctk.CTkFrame(master=master, height=footerbar_height,fg_color=footerbar_color)
    footer_frame.grid(row=mb_row, column=mb_column, padx=pad_x, pady=pad_y, sticky='nsew')
    footer_frame.rowconfigure(0, weight=1)
    footer_frame.columnconfigure((0,1,2,3), weight=1)
    footer_frame.grid_propagate(False)

    admin_menu = ctk.CTkButton(master=footer_frame, text='Admin', fg_color=footerbar_innercolor)
    admin_menu.grid(row=0, column=0, padx=footerbar_inner_padx, pady=footerbar_inner_pady, sticky='sew')
    admin_menu = ctk.CTkButton(master=footer_frame, text='Updates/News', fg_color=footerbar_innercolor)
    admin_menu.grid(row=0, column=1, padx=footerbar_inner_padx, pady=footerbar_inner_pady, sticky='sew')
    admin_menu = ctk.CTkButton(master=footer_frame, text='Settings', fg_color=footerbar_innercolor)
    admin_menu.grid(row=0, column=2, padx=footerbar_inner_padx, pady=footerbar_inner_pady, sticky='sew')
    admin_menu = ctk.CTkButton(master=footer_frame, text='Credits', fg_color=footerbar_innercolor)
    admin_menu.grid(row=0, column=3, padx=footerbar_inner_padx, pady=footerbar_inner_pady, sticky='sew')

def SwitchToHome(window, cur_page):
    cur_page.destroy()
    cur_page = CreateMainMenuPage(window)
    print('Switched to Home')

def SwitchToCardList(window, cur_page):
    cur_page.destroy()
    cur_page = CreateCardListPage(window)
    print('Switched to Card List')