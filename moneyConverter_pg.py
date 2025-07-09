
from tkinter import *
import customtkinter as ctk
import tkinter.font as ctkfont
import requests
from pasta.base.fstring_utils import placeholder

ctk.set_appearance_mode("dark")

top = ctk.CTk()
top.title("Money Converter")
top.geometry("1080x720")
top.resizable("false", "false")

my_font = ctk.CTkFont(family="Gotham-Bold", size = 28)
my_font_button = ctk.CTkFont(family="Gotham-Bold", size = 18)
my_font_heading = ctk.CTkFont(family="Gotham-Bold", size = 42)
my_font_subheading = ctk.CTkFont(family="Gotham-Bold", size = 30)
my_font_label1 = ctk.CTkFont(family="Gotham-Bold", size = 30)
my_font_label2 = ctk.CTkFont(family="Gotham-Bold", size = 20)
my_font_button2 = ctk.CTkFont(family="Gotham-Bold", size = 20, underline = True)
my_font_options = ctk.CTkFont(family="Gotham-Bold", size = 15)

def get_exchange_rates():
    url = "https://v6.exchangerate-api.com/v6/279ed1d45f7cec6bcd8e634d/latest/USD"
    response = requests.get(url)
    data = response.json()
    if data.get("result") == "success":
        return data['conversion_rates']
    else:
        raise Exception("Failed to fetch exchange rates")

def convert_currency():
    try:
        amount = float(moneyInput.get())
        from_curr = options.get()
        to_curr = options2.get()
        rates = get_exchange_rates()

        usd_amount = amount / rates[from_curr]
        converted = usd_amount * rates[to_curr]

        money_output.configure(text=f"{converted:.2f} {to_curr}")

    except Exception as e:
        print(f"Error: {str(e)}")

def about():
    print("About us")

def select(choice):
    options.get()
    options2.get()

def select2():
    print(options.get())
    print(options2.get())


moneyConverter_pg = ctk.CTkFrame(master=top, width=1080, height=720, fg_color="#D3ECCD")
moneyConverter_pg.place(x=0, y=0)

#Header Components ---------------------------------------------------------------------

company_name = ctk.CTkLabel(master=moneyConverter_pg,
                            text="BudgetBee",
                            font= my_font,
                            text_color = "#06923E")
company_name.place(x=20, y=12)

about_button = ctk.CTkButton(master=moneyConverter_pg,
                             text = "About",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
about_button.place(x = 710,y = 18)

services_button = ctk.CTkButton(master=moneyConverter_pg,
                             text = "Services",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
services_button.place(x = 800,y = 18)

contact_button = ctk.CTkButton(master=moneyConverter_pg,
                             text = "Contact",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
contact_button.place(x = 900,y = 18)

login_button = ctk.CTkButton(master=moneyConverter_pg,
                             text = "Login",
                             font = my_font_button,
                             height = 30,
                             width = 50,
                             text_color = "#06923E",
                             fg_color = "#D3ECCD",
                             hover_color = "#D3ECCD",
                             command = about)
login_button.place(x = 1000,y = 18)

line = ctk.CTkFrame(master=moneyConverter_pg,
                           width=1080,
                           height=2,
                           bg_color = "#06923E")
line.place(x = 0, y = 65)

#Main Components -------------------------------------------------------------------------

heading1 = ctk.CTkLabel(master = moneyConverter_pg,
                        text = "Quick Money Converter",
                        font = my_font_heading,
                        text_color = "#06923E")
heading1.place(x = 280, y = 80)

subHeading = ctk.CTkLabel(master = moneyConverter_pg,
                          text = "Want to know rates locally? Don't worry we got you!",
                          font = my_font_label2,
                          text_color = "#06923E")
subHeading.place(x = 260, y = 140)

converter_box = ctk.CTkFrame(moneyConverter_pg,
                           width = 410,
                           height = 450,
                           corner_radius = 20,
                           fg_color = "white",
                           bg_color = "white",
                           border_color="#cccccc",)
converter_box.place(x = 320, y = 200)

moneyInput_heading  = ctk.CTkLabel(master = converter_box,
                               text = "Enter amount",
                               font = my_font_label2,
                               text_color = "#06723E")
moneyInput_heading.place(x = 15, y = 30)

moneyInput = ctk.CTkEntry(master = converter_box,
                          placeholder_text = "|",
                          width = 380,
                          height = 50,
                          fg_color = "#D3ECCD",
                          bg_color = "transparent",
                          text_color = "#06723E",
                          font = my_font_label2,
                          border_color = "#06723E",
                          border_width = 3,
                          corner_radius = 12)
moneyInput.place(x = 15, y = 60)

option_heading  = ctk.CTkLabel(master = converter_box,
                               text = "Convert from?",
                               font = my_font_label2,
                               text_color = "#06723E")
option_heading.place(x = 15, y = 125)

currencies = ["INR", "USD" ,"EUR", "GBP"]

options = ctk.CTkOptionMenu(master = converter_box,
                            values = currencies,
                            width = 300,
                            height = 40,
                            fg_color = "#D3ECCD",
                            button_color = "#06723E",
                            button_hover_color = "#06723F",
                            dropdown_font = my_font_options,
                            dropdown_fg_color = "#D3ECCD",
                            dropdown_text_color = "#06723F",
                            command = select)
options.place(x = 15, y = 155)

option_heading2  = ctk.CTkLabel(master = converter_box,
                               text = "Convert to?",
                               font = my_font_label2,
                               text_color = "#06723E")
option_heading2.place(x = 15, y = 210)

options2 = ctk.CTkOptionMenu(master = converter_box,
                            values = currencies,
                            width = 300,
                            height = 40,
                            fg_color = "#D3ECCD",
                            button_color = "#06723E",
                            button_hover_color = "#06723F",
                            dropdown_font = my_font_options,
                            dropdown_fg_color = "#D3ECCD",
                            dropdown_text_color = "#06723F",
                            command = select)
options2.place(x = 15, y = 240)

convert_button = ctk.CTkButton(master = converter_box,
                               text = "Convert now",
                               width = 80,
                               height = 50,
                               font = my_font_button,
                               text_color = "#D3ECCD",
                               fg_color = "#06723E",
                               hover_color = "#06723F",
                               command = convert_currency)
convert_button.place(x = 15, y = 300)

money_output = ctk.CTkLabel(master = converter_box,
                           text = "",
                            font = my_font_label1,
                            text_color = "#06723E")
money_output.place(x = 15, y = 370)

top.mainloop()