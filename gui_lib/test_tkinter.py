import os
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

clear = lambda: os.system("cls")
clear()

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("895x600+450+100")
app.resizable(1, 1)
app.minsize(500, 500)
app.title("Aboba library")
app.grid_rowconfigure(1, weight = 1)
app.grid_columnconfigure(1, weight = 1)

logo_icon = tk.PhotoImage(file = "coconut.png")

app.iconphoto(0, logo_icon)

# Top and bottom forming frames 
top_frame = ctk.CTkFrame(master = app, width = 200, height = 1)
top_frame.grid(row = 0, column = 0, sticky = "nwe")
top_frame.grid_propagate(0)

bottom_frame = ctk.CTkFrame(master = app, width = 200, height = 1)
bottom_frame.grid(row = 3, column = 0, sticky = "nwe")
bottom_frame.grid_propagate(0)


logo_btn = tk.PhotoImage(file = "./logo.png")

# LEFT FRAME
left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)


sign_in_btn = ctk.CTkButton(master = left_frame, text = "Sign in", 
                            width = 200, height = 40, 
                            fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
sign_in_btn.place(in_ = left_frame, relx = 0.5, rely = 0.0015, anchor = "n")


sign_up_btn = ctk.CTkButton(master = left_frame, text = "Sign up", 
                            width = 200, height = 40, 
                            fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
sign_up_btn.place(in_ = left_frame, relx = 0.5, rely = 0.055, anchor = "n")


login_frm = ctk.CTkFrame(master = left_frame, width = 150, height = 200)
login_frm.place(in_ = left_frame, relx = 0.08, rely = 0.35, relwidth = 0.9)


quit_btn = ctk.CTkButton(master = left_frame, text = "Quit", 
                            width = 200, height = 40, 
                            fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
quit_btn.place(in_ = left_frame, relx = 0.5, rely = 0.99, anchor = "s")


left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)


# RIGHT FRAME
right_frame = ctk.CTkFrame(master = app, width = 200, height = 799)


search_btn = ctk.CTkButton(master = right_frame, text = ("Search"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
search_btn.place(in_ = right_frame, relx = 0.25, rely = 0.0015, anchor = "n")


favrt_btn = ctk.CTkButton(master = right_frame, text = ("Favorite books"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
favrt_btn.place(in_ = right_frame, relx = 0.25, rely = 0.055, anchor = "n")


theme_slider = ctk.CTkSwitch(master = right_frame, text = ("Theme"), 
                            width = 5, fg_color = ("gray"))
theme_slider.place(in_ = right_frame, relx = 0.25, rely = 0.98, anchor = "s")


right_frame.place(in_ = app, relx = 1, anchor = "n", relwidth = 0.25, relheight = 1)


# MID FRAME
mid_frame = ctk.CTkFrame(master = app, width = 800, height = 798)


logo_btn = ctk.CTkButton(master = mid_frame, image = logo_btn, fg_color = "transparent", text = "", hover_color = "#1b1b1b")
logo_btn.place(in_ = mid_frame, relx = 0.5, anchor = "n")


search_entry = ctk.CTkEntry(master = mid_frame, placeholder_text= "Search", width = 450)
search_entry.place(in_ = mid_frame, relx = 0.5, rely = 0.19, anchor = "n", relwidth = 0.8)


search_btn = ctk.CTkButton(master = mid_frame, text = "Search")
search_btn.place(in_ = mid_frame, relx = 0.5, rely = 0.25 , anchor = "n")


# RESULT FRAME
res_frame = ctk.CTkFrame(master = mid_frame, height = 450, width = 450)



res_frame.place(in_ = mid_frame, relx = 0.5, rely = 0.31 , anchor = "n", relwidth = 0.8, relheight = 0.61)


action_btn = ctk.CTkButton(master = mid_frame, text = "Action")
action_btn.place(in_ = mid_frame, relx = 0.5, rely = 0.98 , anchor = "s")

mid_frame.place(in_ = app, relx = 0.5, anchor = "n", relwidth = 0.75, relheight = 1)

app.mainloop()