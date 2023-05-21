from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
import DataBase_connection
import home_window
import admin_window
import customer_window

def sign_in():
    home_window.home_page.destroy()
    global sign_in_page, email_entry_login, password_entry_login
    sign_in_page = tk.Tk()
    sign_in_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
    sign_in_page.title("Sign In")
    #input email
    email_label = tk.Label(sign_in_page, text="Email")
    email_label.place(x=10, y=10)
    email_entry_login = tk.Entry(sign_in_page)
    email_entry_login.place(x=100, y=10)
    #input pw
    password_label = tk.Label(sign_in_page, text="password")
    password_label.place(x=10, y=40)
    password_entry_login = tk.Entry(sign_in_page)
    password_entry_login.place(x=100, y=40)

    submit_button = tk.Button(sign_in_page, text="Submit", width=10, height=2, command=check_valid_login)
    submit_button.place(x=210, y=300)
    
def check_valid_login():
    global email
    email = email_entry_login.get()
    select_query = f"select EMAIL, PERSON_PASSWORD, PERSON_ROLE from PERSON WHERE EMAIL = '{email_entry_login.get()}' AND PERSON_PASSWORD = '{password_entry_login.get()}'"
    DataBase_connection.cursor.execute(select_query)
    result = DataBase_connection.cursor.fetchone()
    if result == None:
        failed = Label(sign_in_page, text = "login failed")
        failed.place(x=215, y=175)
    elif(result[2]=='Admin'):
        admin_window.admin_page()
    else:
        customer_window.customer_page()