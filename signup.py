from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys

ctk.set_appearance_mode("dark")

# Window
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

# Main frame
main_frame = ctk.CTkFrame(master=signup, width=1080, height=720, fg_color="#D3ECCD")
main_frame.place(x=0, y=0)

# Branding Left
logo = ctk.CTkLabel(main_frame, text="SmartFinance ", font=my_font_heading, text_color="#06923E")
logo.place(x=50, y=240)

descrp = ctk.CTkLabel(main_frame, text="Let's get you started!", font=my_font_subheading, text_color="#06923E")
descrp.place(x=50, y=310)

# Shadow effect
shadow = ctk.CTkFrame(main_frame, width=410, height=470, corner_radius=25, fg_color="#c8e5c8")
shadow.place(x=604, y=134)

# Signup Box
signup_box = ctk.CTkFrame(main_frame, width=400, height=460, corner_radius=20, fg_color="white")
signup_box.place(x=600, y=130)

# Header
header = ctk.CTkFrame(signup_box, width=400, height=5, fg_color="#06923E")
header.place(x=0, y=0)

title = ctk.CTkLabel(signup_box, text="Sign Up", font=my_font_label1, text_color="#06923E")
title.place(x=20, y=20)

# Entries
entry_name = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="👤 Full Name", width=350, height=40,
                           fg_color="white", border_color="#06923E", corner_radius=10)
entry_name.place(x=20, y=70)

entry_email = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="📧 Email", width=350, height=40,
                            fg_color="white", border_color="#06923E", corner_radius=10)
entry_email.place(x=20, y=125)

entry_password = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="🔒 Password", width=350, height=40,
                               fg_color="white", border_color="#06923E", show="*", corner_radius=10)
entry_password.place(x=20, y=180)

entry_confirm = ctk.CTkEntry(signup_box, font=my_font_label2, placeholder_text="🔒 Confirm Password", width=350, height=40,
                              fg_color="white", border_color="#06923E", show="*", corner_radius=10)
entry_confirm.place(x=20, y=235)

info = ctk.CTkLabel(signup_box, text="Password must be at least 6 characters", font=my_font_label2, text_color="gray")
info.place(x=20, y=280)

# Validation + redirect
def go_to_login():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get()
    confirm = entry_confirm.get()

    if not name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return
    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror("Error", "Enter a valid email (e.g. name@gmail.com)!")
        return
    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters!")
        return
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    signup.destroy()
    subprocess.Popen([sys.executable, "login.py"])

# Button
signup_btn = ctk.CTkButton(signup_box, text="✅ Create Account", font=my_font_label2, height=40, width=350,
                            text_color="#D3ECCD", fg_color="#06923E", hover_color="#045B27", command=go_to_login)
signup_btn.place(x=20, y=320)

# Separator
line = ctk.CTkFrame(signup_box, width=350, height=1, fg_color="#b0b0b0")
line.place(x=20, y=375)

# Go back to login
back_label = ctk.CTkLabel(signup_box, text="Already have an account?", font=my_font_label2, text_color="#06923E")
back_label.place(x=20, y=390)

def back_to_login():
    signup.destroy()
    subprocess.Popen([sys.executable, "login.py"])

login_btn = ctk.CTkButton(signup_box, text="← Back to Login", font=my_font_button, height=30, width=150,
                           text_color="#06923E", fg_color="white", hover_color="#eeeeee", command=back_to_login)
login_btn.place(x=215, y=387)

# Raise window
signup.lift()
signup.attributes("-topmost", True)
signup.after(500, lambda: signup.attributes("-topmost", False))

signup.mainloop()
