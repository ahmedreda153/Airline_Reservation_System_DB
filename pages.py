import pyodbc
import datetime
from tkinter import *
from tkcalendar import *
import tkinter as tk

home_page = tk.Tk()
# home_page.geometry("500x500")
screen_width = home_page.winfo_screenwidth()
screen_height = home_page.winfo_screenheight()
x = int((screen_width / 2) - (500 / 2))
y = int((screen_height / 2) - (600 / 2))
home_page.geometry(f"500x500+{x}+{y}")
home_page.title("Airline Reservation System")

def home():
    # Create label
    page_title = Label(home_page, text = "Airline Reservation System")
    page_title.config(font =("Courier", 14))
    page_title.pack(pady=50)

    signUp = tk.Button(home_page, text="Sign Up", command=sign_up, width=10, height=2)
    signUp.place(x=140, y=240)
    signIn = tk.Button(home_page, text="Sign In", command=sign_in, width=10, height=2)
    signIn.place(x=290, y=240)

def sign_in():
    home_page.destroy()
    global email_entry_login, password_entry_login
    global sign_in_page
    sign_in_page = tk.Tk()
    sign_in_page.geometry(f"500x500+{x}+{y}")
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

def sign_up():
    global Fname_entry, Lname_entry, email_entry, password_entry, DOB_entry, city_entry, state_entry, zipcode_entry, street_entry, phone_entry, selected_role
    home_page.destroy()
    sign_up_page = tk.Tk()
    # sign_up_page.geometry("500x500")
    sign_up_page.geometry(f"500x500+{x}+{y}")
    sign_up_page.title("Sign Up")
    selected_role = tk.IntVar(value=1)
    #input first name
    Fname_label = tk.Label(sign_up_page, text="First Name")
    Fname_label.place(x=10, y=10)
    Fname_entry = tk.Entry(sign_up_page)
    Fname_entry.place(x=100, y=10)
    #input last name
    Lname_label = tk.Label(sign_up_page, text="Last Name")
    Lname_label.place(x=10, y=40)
    Lname_entry = tk.Entry(sign_up_page)
    Lname_entry.place(x=100, y=40)
    #input email
    email_label = tk.Label(sign_up_page, text="Email")
    email_label.place(x=10, y=70)
    email_entry = tk.Entry(sign_up_page)
    email_entry.place(x=100, y=70)
    #input password
    password_label = tk.Label(sign_up_page, text="Password")
    password_label.place(x=10, y=100)
    password_entry = tk.Entry(sign_up_page)
    password_entry.place(x=100, y=100)
    #input date of birth
    DOB_label = tk.Label(sign_up_page, text="Date of Birth")
    DOB_label.place(x=10, y=130)
    global DOB_entry
    DOB_entry= tk.Entry(sign_up_page, highlightthickness=0, relief='flat')
    DOB_entry.place(x=100, y=130)
    DOB_entry.insert(0, 'YYYY-MM-DD')
    DOB_entry.bind("<Button-1>", pick_date)
    #input city 
    city_label = tk.Label(sign_up_page, text="City")
    city_label.place(x=10, y=160)
    city_entry = tk.Entry(sign_up_page)
    city_entry.place(x=100, y=160)
    #input state 
    state_label = tk.Label(sign_up_page, text="State")
    state_label.place(x=10, y=190)
    state_entry = tk.Entry(sign_up_page)
    state_entry.place(x=100, y=190)
    #input zipcode 
    zipcode_label = tk.Label(sign_up_page, text="Zipcode")
    zipcode_label.place(x=10, y=220)
    zipcode_entry = tk.Entry(sign_up_page)
    zipcode_entry.place(x=100, y=220)
    #input zipcode 
    street_label = tk.Label(sign_up_page, text="Street")
    street_label.place(x=10, y=250)
    street_entry = tk.Entry(sign_up_page)
    street_entry.place(x=100, y=250)
    #input zipcode 
    phone_label = tk.Label(sign_up_page, text="Phone Number")
    phone_label.place(x=10, y=280)
    phone_entry = tk.Entry(sign_up_page)
    phone_entry.place(x=100, y=280)
    #input User role
    role_label =  tk.Label(sign_up_page, text="Select your Role : ")
    role_label.place(x=10, y=310)
    role_option1 = Radiobutton(sign_up_page, text="Customer", value=1, variable=selected_role)
    role_option1.place(x=120, y=310)
    role_option2 = Radiobutton(sign_up_page, text="Admin", value=2, variable=selected_role)
    role_option2.place(x=220, y=310)
    #submit
    submit_button = tk.Button(sign_up_page, text="Submit", width=10, height=2, command=signup_submit)
    submit_button.place(x=210, y=390)






