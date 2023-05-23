from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import DataBase_connection
import home_window
import admin_window
import customer_window
import logo_gradiant
import generate_report

isOpen= False

def sign_in():
    global isOpen
    isOpen=True
    if home_window.home_isOpened:
        home_window.home_page.destroy()
        home_window.home_isOpened=False

    global sign_in_page, email_entry_login, password_entry_login, canvas
    #input email
    sign_in_page = tk.Tk()
    sign_in_page.title("Sign In")
    sign_in_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(sign_in_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(sign_in_page, text="⬅", command= lambda: home_window.back(sign_in_page, home_window.home), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER)
    #large the button
    canvas.create_text(home_window.screen_width  / 2, 170, text="Login to your account", fill="black", font =("Trebuchet MS", 44, "bold"))
    canvas.create_text(home_window.screen_width / 2-175 , 340, text="Email", fill="black", font =("Trebuchet MS", 24))
    email_entry_login = tk.Entry(sign_in_page, font=("Trebuchet MS", 15))
    email_entry_login.place(x=700, y=325,width=250,height=30)
    #input pw
    canvas.create_text(home_window.screen_width /2-150, 470, text="Password", fill="black", font =("Trebuchet MS", 24))
    password_entry_login = tk.Entry(sign_in_page, show="*", font=("Trebuchet MS", 15))
    password_entry_login.place(x=700, y=455,width=250,height=30)

    submit_button = tk.Button(sign_in_page, text="LOGIN", command=lambda:check_valid_login(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    submit_button.place(x=home_window.screen_width / 2 - 100, y=home_window.screen_height - 240, width=200, height=50)

def check_valid_login(event):
    generate_report.generate_pdf_report()
    if email_entry_login.get() == "" or password_entry_login.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 700, text="Please Fill All The Fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, event.delete, error_message)
    else:
        global email
        email = email_entry_login.get()
        select_query = f"select EMAIL, PERSON_PASSWORD, PERSON_ROLE from PERSON WHERE EMAIL = '{email_entry_login.get()}' AND PERSON_PASSWORD = '{password_entry_login.get()}'"
        DataBase_connection.cursor.execute(select_query)
        result = DataBase_connection.cursor.fetchone()
        if result == None:
            canvas.create_text(home_window.screen_width / 2, home_window.screen_height - 270, text="login failed", fill="black", font =("Trebuchet MS", 24))
        elif(result[2]=='Admin'):
            admin_window.admin_page()
        else:
            customer_window.customer_page()