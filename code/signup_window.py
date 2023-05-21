import datetime
from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
import DataBase_connection
import home_window

def pick_date(event):
    global cal, date_window
    date_window = tk.Toplevel()
    date_window.grab_set()
    # date_window.geometry("300x300")
    x = int((home_window.screen_width / 2) - (300 / 2))
    y = int((home_window.screen_height / 2) - (300 / 2))
    date_window.geometry(f"300x300+{x}+{y}")
    date_window.title("Pick Date")
    cal = Calendar(date_window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)
    submit = tk.Button(date_window, text="Submit", command=grab_date)
    submit.pack(pady=20)
    
def grab_date():
    DOB_entry.delete(0, END)
    DOB_entry.insert(0, cal.get_date())
    date_window.destroy()

def sign_up():
    global Fname_entry, Lname_entry, email_entry, password_entry, DOB_entry, city_entry, state_entry, zipcode_entry, street_entry, phone_entry, selected_role
    home_window.home_page.destroy()
    sign_up_page = tk.Tk()
    # sign_up_page.geometry("500x500")
    sign_up_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
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

def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

def signup_submit():
    print(selected_role.get())
    if selected_role.get() == 1:
        role = "Customer"
    else:    
        role = "Admin"
    insert_query = "INSERT INTO PERSON (EMAIL, FNAME, LNAME, PERSON_PASSWORD, PHONENUM, AGE, CITY, PERSON_STATE, ZIPCODE, STREET, PERSON_ROLE, DOB) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    dob = datetime.datetime.strptime(DOB_entry.get(), "%Y-%m-%d")
    age = calculate_age(dob)
    values = (email_entry.get(), Fname_entry.get(), Lname_entry.get(), password_entry.get(), phone_entry.get(), age, city_entry.get(), state_entry.get(), zipcode_entry.get(), street_entry.get(), role, DOB_entry.get())
    DataBase_connection.cursor.execute(insert_query, values)
    DataBase_connection.conn.commit()