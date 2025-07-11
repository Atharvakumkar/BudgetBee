from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
from pymongo import MongoClient

uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client.budgetBee
signup_collection = db.SignUpDetails

ctk.set_appearance_mode("dark")

signup = ctk.CTk()
signup.title("Signup")
signup.geometry("1080x720")
signup.resizable(False, False)

my_font_heading = ctk.CTkFont(family="Gotham-Bold", size=42)
my_font_subheading = ctk.CTkFont(family="Gotham-Bold", size=30)
my_font_label1 = ctk.CTkFont(family="Gotham-Bold", size=30)
my_font_label2 = ctk.CTkFont(family="Gotham-Bold", size=20)
my_font_button = ctk.CTkFont(family="Gotham-Bold", size=20, underline=True)

signup_main_frame = ctk.CTkFrame(master=signup, width=1080, height=720, fg_color="#D3ECCD")
signup_main_frame.place(x=0, y=0)

logo = ctk.CTkLabel(master=signup_main_frame, text="BudgetBee", font=my_font_heading, text_color="#06923E")
logo.place(x=40, y=280)

descrp = ctk.CTkLabel(master=signup_main_frame, text="Smart finance for smarter students",
                      font=my_font_subheading, text_color="#06923E")
descrp.place(x=40, y=340)

shadow = ctk.CTkFrame(master=signup_main_frame, width=400, height=450, fg_color="#b8dbb8")
shadow.place(x=610, y=165)

signup_box = ctk.CTkFrame(master=signup_main_frame, width=400, height=450, fg_color="#ffffff", bg_color="#ffffff")
signup_box.place(x=600, y=150)

title = ctk.CTkLabel(master=signup_box, text="Sign Up", font=my_font_label1, text_color="#06923E")
title.place(x=20, y=20)

sub_title = ctk.CTkLabel(master=signup_box, text="Already Signed up?", font=my_font_label2, text_color="#06923E")
sub_title.place(x=20, y=65)

login_button = ctk.CTkButton(master=signup_box, text="Login", font=my_font_button,
                              height=30, width=50, text_color="#06923E",
                              fg_color="white", hover_color="white", command=lambda: subprocess.Popen([sys.executable, "loginnew.py"]))
login_button.place(x=230, y=64)

line_signup = ctk.CTkFrame(master=signup_box, width=350, height=2,
                           bg_color="#06923E", fg_color="#06923E")
line_signup.place(x=20, y=120)

entry_name = ctk.CTkEntry(master=signup_box, font=my_font_label2,
                          placeholder_text="👤 Full Name", width=350, height=40,
                          fg_color="white", border_color="#06923E",
                          text_color="#06923E", corner_radius=10)
entry_name.place(x=20, y=150)

entry_email = ctk.CTkEntry(master=signup_box, font=my_font_label2,
                           placeholder_text="📧 Email", width=350, height=40,
                           fg_color="white", border_color="#06923E",
                           text_color="#06923E", corner_radius=10)
entry_email.place(x=20, y=205)

entry_password = ctk.CTkEntry(master=signup_box, font=my_font_label2,
                              placeholder_text="🔒 Password", width=350, height=40,
                              fg_color="white", border_color="#06923E",
                              corner_radius=10, text_color="#06923E", show=".")
entry_password.place(x=20, y=260)

entry_confirm = ctk.CTkEntry(master=signup_box, font=my_font_label2,
                             placeholder_text="🔒 Confirm Password", width=350, height=40,
                             fg_color="white", border_color="#06923E",
                             corner_radius=10, text_color="#06923E", show=".")
entry_confirm.place(x=20, y=315)

def validate_and_go():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get()
    confirm = entry_confirm.get()

    if name == "":
        messagebox.showerror("Error", "Full Name cannot be empty.")
    elif "@" not in email or "." not in email:
        messagebox.showerror("Error", "Enter a valid email address.")
    elif len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters.")
    elif password != confirm:
        messagebox.showerror("Error", "Passwords do not match.")
    else:
        signup_details = {
            'name': name,
            'email': email,
            'password': password 
        }

        try:
            signup_collection.insert_one(signup_details)
            messagebox.showinfo("Success", "Account Created Successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to sign up: {e}")

signup_btn = ctk.CTkButton(master=signup_box, text="Create Account",
                           font=my_font_label2, height=40, width=350,
                           text_color="#D3ECCD", fg_color="#06923E",
                           hover_color="#045B27", command=validate_and_go)
signup_btn.place(x=20, y=370)

signup.mainloop()
