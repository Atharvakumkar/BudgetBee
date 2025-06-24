from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys

ctk.set_appearance_mode("dark")

# Main Window
signup = ctk.CTk()
signup.title("SmartFinance Signup")
signup.geometry("1080x720")
signup.resizable(False, False)

# Fonts
my_font_heading = ctk.CTkFont(family="Gotham-Bold", size=42)
my_font_subheading = ctk.CTkFont(family="Gotham-Bold", size=30)
my_font_label1 = ctk.CTkFont(family="Gotham-Bold", size=28)
my_font_label2 = ctk.CTkFont(family="Gotham-Bold", size=18)
my_font_button = ctk.CTkFont(family="Gotham-Bold", size=20, underline=True)

# Background
main_frame = ctk.CTkFrame(master=signup, width=1080, height=720, fg_color="#D3ECCD")
main_frame.place(x=0, y=0)

# Branding
logo = ctk.CTkLabel(main_frame, text="SmartFinance 💸", font=my_font_heading, text_color="#06923E")
logo.place(x=50, y=240)

descrp = ctk.CTkLabel(main_frame, text="Let’s get you started.", font=my_font_subheading, text_color="#06923E")
descrp.place(x=50, y=310)

# Shadow
shadow = ctk.CTkFrame(main_frame, width=410, height=460, corner_radius=25, fg_color="#b8dbb8")
shadow.place(x=604, y=144)

# Signup Box
signup_box = ctk.CTkFrame(main_frame, width=400, height=450, corner_radius=25,
                          fg_color="#ffffff", bg_color="#ffffff",
                          border_color="#06923E", border_width=1)
signup_box.place(x=600, y=140)

# Header
strip = ctk.CTkFrame(signup_box, width=400, height=5, fg_color="#06923E")
strip.place(x=0, y=0)

title = ctk.CTkLabel(signup_box, text="Sign Up", font=my_font_label1, text_color="#06923E")
title.place(x=20, y=20)

# Entry Fields
entry_name = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="👤 Full Name", width=350, height=40,
                          fg_color="white", border_color="#06923E", corner_radius=10)
entry_name.place(x=20, y=80)

entry_email = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="📧 Email", width=350, height=40,
                           fg_color="white", border_color="#06923E", corner_radius=10)
entry_email.place(x=20, y=140)

entry_password = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="🔒 Password", width=350, height=40,
                              fg_color="white", border_color="#06923E", corner_radius=10, show="*")
entry_password.place(x=20, y=200)

entry_confirm = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="🔒 Confirm Password", width=350, height=40,
                             fg_color="white", border_color="#06923E", corner_radius=10, show="*")
entry_confirm.place(x=20, y=260)

# Validation + Redirect
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
        messagebox.showinfo("Success", "Account Created Successfully!")
        signup.destroy()
        subprocess.Popen([sys.executable, "login.py"])

# Submit Button
signup_btn = ctk.CTkButton(signup_box, text="Create Account", font=my_font_label2, height=40, width=350,
                           text_color="#D3ECCD", fg_color="#06923E", hover_color="#045B27", command=validate_and_go)
signup_btn.place(x=20, y=330)

signup.mainloop()
