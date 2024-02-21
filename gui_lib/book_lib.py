import csv, os
import colorama as clrm
from pygame import mixer
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from CTkListbox import *
from PIL import Image

clear = lambda: os.system("cls")
clear()
ctk.set_appearance_mode("dark")

ctk.set_default_color_theme("dark-blue")

mixer.init()
quack_sound = mixer.Sound("duck_quack.mp3")

def lgn_read():
    with open("login_passw.csv", "r") as log_passw:
        return [{line['id']: {"name": line["name"], "password": line["password"], "favorite": line["favorite"], "admin": line["admin"]}} for line in csv.DictReader(log_passw)]

def lib_read():
    with open("book_lib_dict.csv", "r") as log_passw:
        return [{line['id']: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(log_passw)]

def edit_lib(quit_dict):
    edit_field_names = ["id", "name", "author", "release date"]
    with open("book_lib_dict.csv", "w") as book_lib:
        writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
        writer.writeheader()
        writer.writerows(quit_dict)

def orig_lgn_read():
    with open("login_passw.csv", "r") as log_passw:
        return [{"id": line["id"], "name": line["name"], "password": line["password"], "favorite": line["favorite"], "admin": line["admin"]} for line in csv.DictReader(log_passw)]

def orig_lib_read():
    with open("book_lib_dict.csv", "r") as book_lib:
        return [{"id": line["id"], "name": line["name"], "author": line["author"], "release date": line["release date"]} for line in csv.DictReader(book_lib)]

res_dict = {"res": []}

app = ctk.CTk()
app.geometry("895x600+450+100")
app.resizable(1, 1)
app.minsize(500, 500)
app.title("Deep Dark Fantasy - Lumbego Dungeon")

class lib_class():
    def __init__(self):
        self.color = "dark"
        self.user_dict_list = lgn_read()
        self.book_dict_list = lib_read()
        self.check_favrt_list = lgn_read()
        self.user_dict = self.dict_list_to_dict(self.user_dict_list)
        self.book_dict = self.dict_list_to_dict(self.book_dict_list)
        self.log_reg_var = ctk.StringVar()
        self.frm_msg_var = ctk.StringVar()
        self.left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)
        self.left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)
        self.right_frame = ctk.CTkFrame(master = app, width = 200, height = 799)
        self.right_frame.place(in_ = app, relx = 1, anchor = "n", relwidth = 0.25, relheight = 1)
        self.mid_frame = ctk.CTkFrame(master = app, width = 800, height = 798)
        self.mid_frame.place(in_ = app, relx = 0.5, anchor = "n", relwidth = 0.75, relheight = 1)
        self.act_frm = ctk.CTkFrame(master = self.right_frame, width = 150, height = 200)

    
    def destr_left_frm_func(self):
        self.left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)

        sign_in_btn = ctk.CTkButton(master = self.left_frame, text = "Sign in", 
                        width = 200, height = 40, command = lambda: self.sign_in_foo(),
                        fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                        text_color = "#6b6b6b")
        sign_in_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0015, anchor = "n")


        sign_up_btn = ctk.CTkButton(master = self.left_frame, text = "Sign up", 
                                    width = 200, height = 40, command = lambda: self.sign_up_foo(),
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        sign_up_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0505, anchor = "n")


        quit_btn = ctk.CTkButton(master = self.left_frame, text = "Quit", 
                                    width = 200, height = 40, command = app.destroy,
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        quit_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.999, anchor = "s")

        self.left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)
        
    def logout_foo(self):
        self.left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)

        sign_in_btn = ctk.CTkButton(master = self.left_frame, text = "Sign in", 
                        width = 200, height = 40, command = lambda: self.sign_in_foo(),
                        fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                        text_color = "#6b6b6b")
        sign_in_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0015, anchor = "n")


        sign_up_btn = ctk.CTkButton(master = self.left_frame, text = "Sign up", 
                                    width = 200, height = 40, command = lambda: self.sign_up_foo(),
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        sign_up_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0505, anchor = "n")


        quit_btn = ctk.CTkButton(master = self.left_frame, text = "Quit", 
                                    width = 200, height = 40, command = app.destroy,
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        quit_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.999, anchor = "s")

        self.left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)


        self.right_frame = ctk.CTkFrame(master = app, width = 200, height = 799)

        theme_slider = ctk.CTkSwitch(master = self.right_frame, text = ("Theme"), command = self.theme_foo,
                            width = 5, fg_color = ("gray"), onvalue = "Dark", offvalue = "Light")
        theme_slider.place(in_ = self.right_frame, relx = 0.25, rely = 0.989, anchor = "s")

        self.right_frame.place(in_ = app, relx = 1, anchor = "n", relwidth = 0.25, relheight = 1)

        # MID FRAME
        self.mid_frame = ctk.CTkFrame(master = app, width = 800, height = 798)
        logo_btn = ctk.CTkButton(master = self.mid_frame, 
                                image = logo_btn_img, command = quack_sound.play,
                                fg_color = "transparent", 
                                text = "", 
                                hover_color = "#4b4b4b")
        logo_btn.place(in_ = self.mid_frame, relx = 0.5, anchor = "n")


        search_entry = ctk.CTkEntry(master = self.mid_frame, placeholder_text= "Search", width = 450)
        search_entry.place(in_ = self.mid_frame, relx = 0.5, rely = 0.19, anchor = "n", relwidth = 0.8)


        srch_btn = ctk.CTkButton(master = self.mid_frame, text = "Search")
        srch_btn.place(in_ = self.mid_frame, relx = 0.5, rely = 0.25 , anchor = "n")


        # RESULT FRAME
        res_frame = ctk.CTkFrame(master = self.mid_frame, height = 450, width = 450)



        res_frame.place(in_ = self.mid_frame, relx = 0.5, rely = 0.31 , anchor = "n", relwidth = 0.8, relheight = 0.61)


        action_btn = ctk.CTkButton(master = self.mid_frame, text = "Action")
        action_btn.place(in_ = self.mid_frame, relx = 0.5, rely = 0.98 , anchor = "s")
        
        self.mid_frame.place(in_ = app, relx = 0.5, anchor = "n", relwidth = 0.75, relheight = 1)
    
    def sign_up_foo(self):
        def check_sign_up_foo():
            if len(usrnm_entry.get()) > 0 and len(passw_entry.get()) > 7: 
                self.frm_msg_var.set("Success")
                full_info_dict = {"id": id_count, "name": usrnm_entry.get().lower(), "password": passw_entry.get(), "favorite": "0", "admin": "0"}

                success_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "green")
                success_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)

                with open("login_passw.csv", "a") as log_passw:
                    writer = csv.DictWriter(log_passw, fieldnames=field_names)
                    writer.writerow(full_info_dict)

                # success_lbl.after(2499, self.destr_left_frm_func)
                success_lbl.after(2500, login_frm.destroy)
                
            else:
                self.frm_msg_var.set("Your password have to be \nat least 8 characters long")
                error_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "red")
                error_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)
                error_lbl.after(2500, error_lbl.destroy)
        
        ## REGISTRATION FRAME

        self.log_reg_var.set("Sign up")
        login_frm = ctk.CTkFrame(master = self.left_frame, width = 150, height = 200)
        
        usrnm_entry = ctk.CTkEntry(master= login_frm, width = 100, placeholder_text = "username")
        usrnm_entry.place(in_ = login_frm, relx = 0.01, rely = 0.02, relwidth = 0.99)

        passw_entry = ctk.CTkEntry(master = login_frm, width = 100, placeholder_text = "password", show = "*")
        passw_entry.place(in_ = login_frm, relx = 0.01, rely = 0.2, relwidth = 0.99)

        login_btn = ctk.CTkButton(master = login_frm, textvariable = self.log_reg_var, width = 5, command = check_sign_up_foo)
        login_btn.place(in_ = login_frm, relx = 0.1, rely = 0.4, relwidth = 0.8)

        login_frm.place(in_ = self.left_frame, relx = 0.08, rely = 0.35, relwidth = 0.9)

        frm_destr_btn = ctk.CTkButton(master = self.left_frame, text = "Quit login", 
                                    width = 200, height = 40, command = self.destr_left_frm_func,
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        frm_destr_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.95, anchor = "s")

        user_dict_list = lgn_read()
        
        id_count, field_names = len(user_dict_list) + 1, ["id", "name", "password", "favorite", "admin"]
        
        ctk.CTkLabel(master = login_frm, text = f"Your login id: {id_count}").place(in_ = login_frm, relx = 0.18, rely = 0.8)


    def dict_list_to_dict(self, dict_list):
        cycle, dict = 0, {}

        while cycle < len(dict_list):
            dict.update(dict_list[cycle])
            cycle += 1
        return dict

    def print_books_foo(self): 
        for key, val in self.book_dict.items():
            print("-----" * 10)
            print(f"{key}: Book name: {clrm.Fore.GREEN + val['name'] + clrm.Style.RESET_ALL}, Author: {clrm.Fore.GREEN + val['author'] + clrm.Style.RESET_ALL}, Year: {clrm.Fore.GREEN + val['release date'] + clrm.Style.RESET_ALL}")
        print("-----" * 10)
        print("Q: Quit to main menu")
        print("-----" * 10)
        
        return self.book_dict

    def print_users_foo(self):
        for key, val in self.user_dict.items():
            print("-----" * 10)
            print(f"{key}: Username: {clrm.Fore.GREEN + val['name'] + clrm.Style.RESET_ALL}, Password: {clrm.Fore.GREEN + val['password'] + clrm.Style.RESET_ALL}, Favorite: {clrm.Fore.GREEN + val['favorite'] + clrm.Style.RESET_ALL}, Admin: {clrm.Fore.GREEN + val['admin'] + clrm.Style.RESET_ALL}")
        print("-----" * 10)
        print("Q: Quit to main menu")
        print("-----" * 10)
        return self.user_dict
  
    def delete_foo(self, list_, tree):
        for cycle in range(1, len(list_) + 1):
            idx = f"I00{cycle}"
            print(tree.item(idx))
            tree.delete(idx)
    
    def log_res_foo(self, cycle):
        columns_ = ("Id", "Name", "Password", "Favorite", "Admin")
        res_tree = ttk.Treeview(master=res_frame, show="headings", columns=columns_)
        res_tree.place(in_=res_frame, relwidth=1, relheight=1)

        for head in range(len(columns_)):
            res_tree.heading(columns_[head], text=columns_[head])
        list_dicts = orig_lgn_read()
              
        if list_dicts[cycle - 1]:
            id_ = list_dicts[cycle - 1]["id"]
            name_ = list_dicts[cycle - 1]["name"]
            paswrd_ = list_dicts[cycle - 1]["password"]
            favrt_ = list_dicts[cycle - 1]["favorite"]
            admin_ = list_dicts[cycle - 1]["admin"]
            info = (id_, name_, paswrd_, favrt_, admin_)
            res_dict["res"].append(info)

        for row in res_dict["res"]:
            res_tree.insert("", "end", values=row)
        
        if len(search_entry.get()) == 0:
            self.delete_foo(res_dict["res"], res_tree)
            res_dict["res"] = []

    def res_foo(self, cycle):
        # RESULT FRAME
        columns_ = ("Id", "Name", "Author", "Release Year")
        res_tree = ttk.Treeview(master=res_frame, show="headings", columns=columns_)
        res_tree.place(in_=res_frame, relwidth=1, relheight=1)

        for head in range(len(columns_)):
            res_tree.heading(columns_[head], text=columns_[head])
        list_dicts = orig_lib_read()
              
        if list_dicts[cycle - 1]:
            id_ = list_dicts[cycle - 1]["id"]
            name_ = list_dicts[cycle - 1]["name"]
            author_ = list_dicts[cycle - 1]["author"]
            reles_year = list_dicts[cycle - 1]["release date"]
            info = (id_, name_, author_, reles_year)
            res_dict["res"].append(info)

        for row in res_dict["res"]:
            res_tree.insert("", "end", values=row)
        
        if len(search_entry.get()) == 0:
            self.delete_foo(res_dict["res"], res_tree)

    def theme_foo(self):
        if self.color == "dark":
            ctk.set_appearance_mode("light")
            self.color = "light"
        else:
            ctk.set_appearance_mode("dark")
            self.color = "dark"
        
    def user_id_foo(self):
        global login_entry
        return login_entry.get()
    
    def print_books_foo(self):
        for key, val in self.book_dict.items():
            print("-----" * 10)
            print(f"{key}: Book name: {clrm.Fore.GREEN + val['name'] + clrm.Style.RESET_ALL}, Author: {clrm.Fore.GREEN + val['author'] + clrm.Style.RESET_ALL}, Year: {clrm.Fore.GREEN + val['release date'] + clrm.Style.RESET_ALL}")
        print("-----" * 10)
        print("Q: Quit to main menu")
        print("-----" * 10)
        
        return self.book_dict
    
    def print_users_foo(self):
        for key, val in self.user_dict.items():
            print("-----" * 10)
            print(f"{key}: Username: {clrm.Fore.GREEN + val['name'] + clrm.Style.RESET_ALL}, Password: {clrm.Fore.GREEN + val['password'] + clrm.Style.RESET_ALL}, Favorite: {clrm.Fore.GREEN + val['favorite'] + clrm.Style.RESET_ALL}, Admin: {clrm.Fore.GREEN + val['admin'] + clrm.Style.RESET_ALL}")
        print("-----" * 10)
        print("Q: Quit to main menu")
        print("-----" * 10)
        return self.user_dict
                
    def add_srch_favrt_foo(self, favrt_inpt):
        login_field_names = ["id", "name", "password", "favorite", "admin"]
        favrt_field_names = ["id", "name", "author", "release date"]

        if favrt_inpt in self.book_dict:
            favrt_file = f'{self.check_favrt_list[int(self.self.user_id_foo()) - 1][self.self.user_id_foo()]["name"]}_favrt.csv'
            path = f"./{favrt_file}"
            check_file = os.path.exists(path)
            if check_file == True:

                with open(f"{favrt_file}", "r") as f_name:
                    user_favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(f_name)]    
                    id_count = len(user_favrt_dict_list) + 1
                    full_info_dict = {"id": id_count, "name": self.book_dict[favrt_inpt]["name"], "author": self.book_dict[favrt_inpt]["author"], "release date": self.book_dict[favrt_inpt]["release date"]}
                
                with open(f"{favrt_file}", "a") as user_favrt_file:
                    writer = csv.DictWriter(user_favrt_file, fieldnames=favrt_field_names)
                    writer.writerow(full_info_dict)
            else:
                full_info_dict = {"id": 1, "name": self.book_dict[favrt_inpt]["name"], "author": self.book_dict[favrt_inpt]["author"], "release date": self.book_dict[favrt_inpt]["release date"]}
                quit_dict = orig_lgn_read()

                for info in quit_dict:
                    quit_dict[int(self.user_id_foo()) - 1]["favorite"] = favrt_file

                with open("login_passw.csv", "w") as log_passw:
                    writer = csv.DictWriter(log_passw, fieldnames=login_field_names)
                    writer.writeheader()
                    writer.writerows(quit_dict)
    
                with open(f"{favrt_file}", "w") as f_name:
                    writer = csv.DictWriter(f_name, fieldnames=favrt_field_names)
                    writer.writeheader()
                    writer.writerow(full_info_dict)

    def add_favrt_foo(self):
        favrt_bool, check_favrt_list = 1, orig_lgn_read()
            
        while favrt_bool == 1:
            clear()
            print(clrm.Style.RESET_ALL + "============ Adding favorite book ================")
            print("Which book do you wish to add to your favorites?: ")
            book_dict = self.print_books_foo()
            favrt_inpt = input("Enter here book id: " + clrm.Fore.YELLOW).lower()

            login_field_names = ["id", "name", "password", "favorite", "admin"]
            favrt_field_names = ["id", "name", "author", "release date"]
            
            if favrt_inpt in book_dict:
                
                favrt_file = f'{check_favrt_list[int(self.self.user_id_foo()) - 1][self.self.user_id_foo()]["name"]}_favrt.csv'
                path = f"./{favrt_file}"
                check_file = os.path.exists(path)

                if check_file == 1:

                    with open(f"{favrt_file}", "r") as f_name:
                        user_favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(f_name)]    
                        id_count = len(user_favrt_dict_list) + 1
                        full_info_dict = {"id": id_count, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                    
                    with open(f"{favrt_file}", "a") as user_favrt_file:
                        writer = csv.DictWriter(user_favrt_file, fieldnames=favrt_field_names)
                        writer.writerow(full_info_dict)
                else:
                    full_info_dict = {"id": 1, "name": book_dict[favrt_inpt]["name"], "author": book_dict[favrt_inpt]["author"], "release date": book_dict[favrt_inpt]["release date"]}
                    
                    quit_dict = orig_lgn_read()

                    for info in quit_dict:
                        quit_dict[int(self.user_id_foo()) - 1]["favorite"] = favrt_file

                    with open("login_passw.csv", "w") as log_passw:
                        writer = csv.DictWriter(log_passw, fieldnames=login_field_names)
                        writer.writeheader()
                        writer.writerows(quit_dict)

                    with open(f"{favrt_file}", "w") as f_name:
                        writer = csv.DictWriter(f_name, fieldnames=favrt_field_names)
                        writer.writeheader()
                        writer.writerow(full_info_dict)
    
    def rem_favrt_foo(self):
        favrt_file = f'{self.check_favrt_list[int(self.user_id_foo()) - 1][self.user_id_foo()]["name"]}_favrt.csv'
        path = f"./{favrt_file}"
        check_file = os.path.exists(path)
        
        if check_file == 1:
            favrt_book_bool = 1
                
            while favrt_book_bool == 1:
                clear()
                print(clrm.Style.RESET_ALL + "================ Deleting the book ===============")
                print("Which book do you wish to delete?: ")
                favrt_book_dict = self.print_books_foo()
                book_id_inpt = input("Enter here book id: " + clrm.Fore.YELLOW).lower()
                print(clrm.Style.RESET_ALL + "=====" * 10)
                print()

                edit_field_names, id_count = ["id", "name", "author", "release date"], 1
                
                if book_id_inpt in favrt_book_dict:

                    with open(f"{favrt_file}", "r") as book_lib:
                        need_del_dict = [{"id": line["id"], "name": line["name"], "author": line["author"], "release date": line["release date"]} for line in csv.DictReader(book_lib)]
                    
                    with open(f"{favrt_file}", "w") as book_lib:
                        writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                        writer.writeheader()

                    for info in need_del_dict:

                        if book_id_inpt != info["id"]:
                            info["id"] = id_count
                            with open(f"{favrt_file}", "a") as book_lib:
                                writer = csv.DictWriter(book_lib, fieldnames=edit_field_names)
                                writer.writerow(info)
                            id_count += 1
                        else:
                            pass
        else:
            clear()
            print(clrm.Fore.RED + "==================== Error =======================")
            print("You don't have favorite books yet.")
            print("=====" * 10 + clrm.Style.RESET_ALL)

    def favorite_books_foo(self):
        favrt_count = 0 
        favrt_file = f'{self.check_favrt_list[int(self.user_id_foo()) - 1][self.user_id_foo()]["name"]}_favrt.csv'

        if self.check_favrt_list[int(self.user_id_foo()) - 1][self.user_id_foo()]["favorite"] == "0":
            print(clrm.Style.RESET_ALL + "\n=================== Output =======================")
            print(f"Dear {clrm.Fore.CYAN + self.check_favrt_list[int(self.user_id_foo()) - 1][self.user_id_foo()]['name'].title() + clrm.Style.RESET_ALL}, unfortunately you don't have favorite books yet.")
            print("=====" * 10)
        else:
            with open(f"{favrt_file}", "r") as check_favrt_file:
                favrt_dict_list = [{line["id"]: {"name": line["name"], "author": line["author"], "release date": line["release date"]}} for line in csv.DictReader(check_favrt_file)]
                
                print(clrm.Style.RESET_ALL + "\n=================== Output =======================")
                print("Your favorite books:")
            while favrt_count < len(favrt_dict_list):
                count = favrt_count + 1
                id_count = str(count)
                dict_out = favrt_dict_list[favrt_count][id_count]
                print("-----" * 10)
                print(f"Book name: {clrm.Fore.GREEN + dict_out['name'] + clrm.Style.RESET_ALL}, Author: {clrm.Fore.GREEN + dict_out['author'] + clrm.Style.RESET_ALL}, Release year: {clrm.Fore.GREEN + dict_out['release date'] + clrm.Style.RESET_ALL}")
                favrt_count += 1
            print("=====" * 10)
            print()

        user_inpt = input("Do you wish to continue? Y/N: " + clrm.Fore.YELLOW + clrm.Style.RESET_ALL).lower()
    
    def search_year_rnge(self):
        clear()
        res_dict["res"] = []
        cycle = 1
        search_entry.configure(placeholder_text="Enter year range like in example: xxxx-yyyy")
        first_entry = int(search_entry.get().split("-")[0])
        second_entry = int(search_entry.get().split("-")[1])
        while cycle < len(self.book_dict) + 1:
            year_int = int(self.book_dict[f"{cycle}"]["release date"])
            if  first_entry <= year_int and second_entry >= year_int:
                self.res_foo(cycle)
            cycle += 1

    def search_name_foo(self):
        clear()
        res_dict["res"] = []
        user_inpt, cycle = search_entry.get().title() ,1
        while cycle < len(self.book_dict) + 1:
            if user_inpt in self.book_dict[f"{cycle}"]["name"]:
                self.res_foo(cycle)
            cycle += 1
    
    def search_year_foo(self):
        clear()
        res_dict["res"] = []
        user_inpt, cycle = search_entry.get() ,1
        while cycle < len(self.book_dict) + 1:
            if user_inpt in self.book_dict[f"{cycle}"]["release date"]:
                self.res_foo(cycle)
            cycle += 1

    def search_author_foo(self):
        clear()
        res_dict["res"] = []
        user_inpt, cycle = search_entry.get().title(), 1
        while cycle < len(self.book_dict) + 1:
            if user_inpt in self.book_dict[f"{cycle}"]["author"]:
                self.res_foo(cycle)                
            cycle += 1
    
                
    def sign_in_foo(self):
        global login_entry  

        def list_display(dict_, list_):
            count = 0
            while count < len(dict_):
                for key in dict_:
                    list_.insert(count, key)
                    count += 1
        
        def check_sign_in_foo():
            if login_entry.get() in self.user_dict:
                clear()
                ## ADMIN FUNCTIONS
                def edit_name_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1
                
                def edit_author_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1

                def edit_year_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1
                
                def edit_all_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1
                
                def del_book_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1
                        
                def add_book_foo():
                    res_dict["res"] = []
                    book_bool, cycle = 1, 1         
                    while cycle < len(self.book_dict) + 1:
                        self.res_foo(cycle)
                        cycle += 1

                def admin_foo():
                    res_dict["res"] = []
                    user_bool, cycle = 1, 1         
                    while cycle < len(self.user_dict) + 1:
                        self.log_res_foo(cycle)
                        cycle += 1

                def edit_usrnames_foo():
                    res_dict["res"] = []
                    user_bool, cycle = 1, 1         
                    while cycle < len(self.user_dict) + 1:
                        self.log_res_foo(cycle)
                        cycle += 1


                def edit_pswrds_foo():
                    res_dict["res"] = []
                    user_bool, cycle = 1, 1         
                    while cycle < len(self.user_dict) + 1:
                        self.log_res_foo(cycle)
                        cycle += 1

    
                ## USER FUNCTIONS
                def edit_username_foo():
                    res_dict["res"] = []
                    self.log_res_foo(self.user_id_foo())


                def edit_passw_foo():
                    res_dict["res"] = []
                    self.log_res_foo(self.user_id_foo())

                ## ADMIN FUNCTIONS CHECK
                if passw_entry.get() == self.user_dict[login_entry.get()]["password"] and self.user_dict[login_entry.get()]["admin"] == "1":    
                    self.left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)
                    
                    ## LEFT AND LOGIN FRAME                        
                    self.frm_msg_var.set("Success")
                    
                    success_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "green")
                    success_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)

                    user_lbl = ctk.CTkLabel(master = self.left_frame, 
                                            text = f"Welcome, {self.user_dict[self.user_id_foo()]["name"].title()}!",
                                            text_color = "#6b6b6b")
                    user_lbl.place(in_ = self.left_frame, relx = 0.55, rely = 0.08, anchor = "n")

                    logout_btn = ctk.CTkButton(master = self.left_frame, text = "Logout", 
                                width = 200, height = 40, command = self.logout_foo, text_color = "#6b6b6b",
                                fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
                    logout_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0015, anchor = "n")

                    quit_btn = ctk.CTkButton(master = self.left_frame, text = "Quit", 
                                                width = 200, height = 40, command = app.destroy,
                                                fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                                text_color = "#6b6b6b")
                    quit_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.999, anchor = "s")
                    
                    ## RIGTH AND ACTION FRAME
                    act_frm = ctk.CTkFrame(master = self.right_frame, width = 150, height = 200)
                    act_frm.place(in_ = self.right_frame, relx = 0.02, rely = 0.35, relwidth = 0.46)

                    self.left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)

                    
                    search_dict = {"Search year range": self.search_year_rnge,
                                    "Search year": self.search_year_foo,
                                    "Search author": self.search_author_foo,
                                    "Search book": self.search_name_foo}

                    favrt_dict = {"Favorite books": self.favorite_books_foo,
                                "Add favorite book": self.add_favrt_foo,
                                "Remove favorite books": self.rem_favrt_foo,}

                    def show_search_val(selected_option):
                        if selected_option in search_dict:
                            srch_btn.configure(command=search_dict[selected_option])
                    
                    def show_favrt_val(selected_option):
                        if selected_option in favrt_dict:
                            srch_btn.configure(command=favrt_dict[selected_option])
                    
                    def show_edit_val(selected_option):
                        if selected_option in edit_dict:
                            srch_btn.configure(command=edit_dict[selected_option])
                    
                    def show_edit_acc_val(selected_option):
                        if selected_option in edit_accs_dict:
                            srch_btn.configure(command=edit_accs_dict[selected_option])
                            
                    def search_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_search_val, 
                                        bg_color = "transparent", border_width = 0,
                                        text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        list_display(search_dict, list_bx)                    

                        list_bx.place(relx = 0, rely = 0)

                    def favrt_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_favrt_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        list_display(favrt_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)

                    def edit_lib_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_edit_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")

                        list_display(edit_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)
                    
                    def edit_accs_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_edit_acc_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        
                        list_display(edit_accs_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)

                    search_dict = {"Search year range": self.search_year_rnge,
                                "Search year": self.search_year_foo,
                                "Search author": self.search_author_foo,
                                "Search book": self.search_name_foo}

                    favrt_dict = {"Favorite books": self.favorite_books_foo,
                                "Add favorite book": self.add_favrt_foo,
                                "Remove favorite books": self.rem_favrt_foo,}
                    
                    
                    edit_dict = {"Add book": add_book_foo,
                                "Remove book": del_book_foo,
                                "Edit book name": edit_name_foo,
                                "Edit Author": edit_author_foo,
                                "Edit year": edit_year_foo,
                                "Edit all": edit_all_foo}
                    
                    edit_accs_dict = {"Edit usernames": edit_usrnames_foo,
                                    "Edit passwords": edit_pswrds_foo,
                                    "Admin status": admin_foo}
                    
                    search_btn = ctk.CTkButton(master = self.right_frame, text = ("Search"), 
                            width = 200, height = 40, fg_color = "transparent", 
                            corner_radius = 5, hover_color = "#3b3b3b",
                            text_color = "#6b6b6b", command = search_btn_foo)
                    search_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.0015, anchor = "n")

                    favrt_btn = ctk.CTkButton(master = self.right_frame, text = ("Favorite books"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, 
                            hover_color = "#3b3b3b", text_color = "#6b6b6b", command = favrt_btn_foo)
                    favrt_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.0525, anchor = "n")

                    edit_lib_btn = ctk.CTkButton(master = self.right_frame, text = ("Edit library"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, 
                            hover_color = "#3b3b3b", text_color = "#6b6b6b", command = edit_lib_btn_foo)
                    edit_lib_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.1, anchor = "n")

                    edit_accs_lib_btn = ctk.CTkButton(master = self.right_frame, text = ("Edit Accounts"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, 
                            hover_color = "#3b3b3b", text_color = "#6b6b6b", command = edit_accs_foo)
                    edit_accs_lib_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.15, anchor = "n")

                ## USER FUNCTIONS CHECK
                elif passw_entry.get() == self.user_dict[login_entry.get()]["password"] and self.user_dict[login_entry.get()]["admin"] == "0":
                    self.left_frame = ctk.CTkFrame(master = app, width = 200, height = 799)
                    
                    ## LEFT AND LOGIN FRAME                        
                    self.frm_msg_var.set("Success")
                    
                    success_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "green")
                    success_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)

                    user_lbl = ctk.CTkLabel(master = self.left_frame, 
                                            text = f"Welcome, {self.user_dict[self.user_id_foo()]["name"].title()}!",
                                            text_color = "#6b6b6b")
                    user_lbl.place(in_ = self.left_frame, relx = 0.55, rely = 0.08, anchor = "n")

                    logout_btn = ctk.CTkButton(master = self.left_frame, text = "Logout", 
                                width = 200, height = 40, command = self.logout_foo, text_color = "#6b6b6b",
                                fg_color = "transparent", corner_radius = 5, hover_color = "#2b2b2b")
                    logout_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.0015, anchor = "n")

                    quit_btn = ctk.CTkButton(master = self.left_frame, text = "Quit", 
                                                width = 200, height = 40, command = app.destroy,
                                                fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                                text_color = "#6b6b6b")
                    quit_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.999, anchor = "s")
                    
                    ## RIGTH AND ACTION FRAME
                    act_frm = ctk.CTkFrame(master = self.right_frame, width = 150, height = 200)
                    act_frm.place(in_ = self.right_frame, relx = 0.02, rely = 0.35, relwidth = 0.46)

                    self.left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)


                    search_dict = {"Search year range": self.search_year_rnge,
                                "Search year": self.search_year_foo,
                                "Search author": self.search_author_foo,
                                "Search book": self.search_name_foo}
                    
                    favrt_dict = {"Favorite books": self.favorite_books_foo,
                                "Add favorite book": self.add_favrt_foo,
                                "Remove favorite books": self.rem_favrt_foo,}
                    
                    edit_acc_dict = {"Edit username": edit_username_foo,
                                    "Edit password": edit_passw_foo}
                    
                    
                    def show_search_val(selected_option):
                        if selected_option in search_dict:
                            srch_btn.configure(command=search_dict[selected_option])
                    
                    def show_favrt_val(selected_option):
                        if selected_option in favrt_dict:
                            srch_btn.configure(command=favrt_dict[selected_option])
                    
                    def show_acc_val(selected_option):
                        if selected_option in edit_acc_dict:
                            srch_btn.configure(command=edit_acc_dict[selected_option])

                    def search_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_search_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        
                        list_display(search_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)
                    
                    def favrt_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_favrt_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        
                        list_display(favrt_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)

                    def edit_acc_btn_foo():
                        list_bx = CTkListbox(master = act_frm, command = show_acc_val, 
                                            bg_color = "transparent", border_width = 0,
                                            text_color = "#6b6b6b", hover_color = "#3b3b3b")
                        
                        list_display(edit_acc_dict, list_bx)

                        list_bx.place(relx = 0, rely = 0)

                    search_btn = ctk.CTkButton(master = self.right_frame, text = ("Search"), 
                            width = 200, height = 40, fg_color = "transparent", 
                            corner_radius = 5, hover_color = "#3b3b3b",
                            text_color = "#6b6b6b", command = search_btn_foo)
                    search_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.0015, anchor = "n")

                    favrt_btn = ctk.CTkButton(master = self.right_frame, text = ("Favorite books"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, 
                            hover_color = "#3b3b3b", text_color = "#6b6b6b", command = favrt_btn_foo)
                    favrt_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.0525, anchor = "n")

                    edit_acc_btn = ctk.CTkButton(master = self.right_frame, text = ("Edit account"), 
                            width = 200, height = 40, fg_color = "transparent", corner_radius = 5, 
                            hover_color = "#3b3b3b", text_color = "#6b6b6b", command = edit_acc_btn_foo)
                    edit_acc_btn.place(in_ = self.right_frame, relx = 0.25, rely = 0.1, anchor = "n")
                else:
                    clear()
                    self.frm_msg_var.set("Wrong password")
                    error_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "red")
                    error_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)
                    error_lbl.after(2500, error_lbl.destroy)
            else:
                clear()
                self.frm_msg_var.set("Wrong Id")
                error_lbl = ctk.CTkLabel(master = login_frm, textvariable = self.frm_msg_var, text_color = "red")
                error_lbl.place(in_ = login_frm, relx = 0.054, rely = 0.6, relwidth = 0.9)
                error_lbl.after(2500, error_lbl.destroy)

    ## LEFT FRAME
        login_frm = ctk.CTkFrame(master = self.left_frame, width = 150, height = 200)

        blank_lbl = ctk.CTkLabel(master = login_frm, width = 200, height = 400, text = "")
        blank_lbl.place(in_ = login_frm, relx = 0.001, rely = 0.35)

        login_entry = ctk.CTkEntry(master= login_frm, width = 100, placeholder_text = "id")
        login_entry.place(in_ = login_frm, relx = 0.01, rely = 0.02, relwidth = 0.99)

        passw_entry = ctk.CTkEntry(master = login_frm, width = 100, placeholder_text = "password", show = "*")
        passw_entry.place(in_ = login_frm, relx = 0.01, rely = 0.2, relwidth = 0.99)

        login_btn = ctk.CTkButton(master = login_frm, textvariable = self.log_reg_var, width = 5, command = check_sign_in_foo)
        login_btn.place(in_ = login_frm, relx = 0.1, rely = 0.4, relwidth = 0.8)

        login_frm.place(in_ = self.left_frame, relx = 0.08, rely = 0.35, relwidth = 0.9)

        frm_destr_btn = ctk.CTkButton(master = self.left_frame, text = "Quit login", 
                                    width = 200, height = 40, command = self.destr_left_frm_func,
                                    fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                                    text_color = "#6b6b6b")
        frm_destr_btn.place(in_ = self.left_frame, relx = 0.5, rely = 0.95, anchor = "s")      

        check_sign_in_foo()



lib = lib_class()


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


logo_btn_img = ctk.CTkImage(Image.open(f"logo.png"), size = ((450, 120)))

## LEFT FRAME
sign_in_btn = ctk.CTkButton(master = lib.left_frame, text = "Sign in", 
                            width = 200, height = 40, command = lambda: lib.sign_in_foo(),
                            fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                            text_color = "#6b6b6b")
sign_in_btn.place(in_ = lib.left_frame, relx = 0.5, rely = 0.0015, anchor = "n")


sign_up_btn = ctk.CTkButton(master = lib.left_frame, text = "Sign up", 
                            width = 200, height = 40, command = lambda: lib.sign_up_foo(),
                            fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                            text_color = "#6b6b6b")
sign_up_btn.place(in_ = lib.left_frame, relx = 0.5, rely = 0.0505, anchor = "n")


quit_btn = ctk.CTkButton(master = lib.left_frame, text = "Quit", 
                            width = 200, height = 40, command = app.destroy,
                            fg_color = "transparent", corner_radius = 5, hover_color = "#3b3b3b",
                            text_color = "#6b6b6b")
quit_btn.place(in_ = lib.left_frame, relx = 0.5, rely = 0.999, anchor = "s")


# left_frame.place(in_ = app, relx = 0.06, anchor = "n", relwidth = 0.13, relheight = 1)


# LOGIN FRAME VARIABLES
lib.log_reg_var.set("Sign in")


# RIGHT FRAME

theme_slider = ctk.CTkSwitch(master = lib.right_frame, text = ("Theme"), command = lib.theme_foo,
                            width = 5, fg_color = ("gray"), onvalue = "Dark", offvalue = "Light")
theme_slider.place(in_ = lib.right_frame, relx = 0.25, rely = 0.989, anchor = "s")


# MID FRAME
logo_btn = ctk.CTkButton(master = lib.mid_frame, 
                        image = logo_btn_img, command = quack_sound.play,
                        fg_color = "transparent", 
                        text = "", 
                        hover_color = "#4b4b4b")
logo_btn.place(in_ = lib.mid_frame, relx = 0.5, anchor = "n")


search_entry = ctk.CTkEntry(master = lib.mid_frame, placeholder_text= "Search", width = 450)
search_entry.place(in_ = lib.mid_frame, relx = 0.5, rely = 0.19, anchor = "n", relwidth = 0.8)


srch_btn = ctk.CTkButton(master = lib.mid_frame, text = "Search")
srch_btn.place(in_ = lib.mid_frame, relx = 0.5, rely = 0.25 , anchor = "n")


# RESULT FRAME
res_frame = ctk.CTkFrame(master = lib.mid_frame, height = 450, width = 450)



res_frame.place(in_ = lib.mid_frame, relx = 0.5, rely = 0.31 , anchor = "n", relwidth = 0.8, relheight = 0.61)


action_btn = ctk.CTkButton(master = lib.mid_frame, text = "Action")
action_btn.place(in_ = lib.mid_frame, relx = 0.5, rely = 0.98 , anchor = "s")



app.mainloop()