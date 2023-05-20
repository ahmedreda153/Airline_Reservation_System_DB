import pyodbc
from tkinter import *
from tkcalendar import *
import tkinter as tk
#sba7 el 5er

home_page = tk.Tk()
home_page.geometry("500x500")
home_page.title("Airline Reservation System")

#connect database
server = 'DESKTOP-Q66QLBQ\SQLEXPRESS'
database = 'AIRLINE_RESERVATION'
username = 'DESKTOP-Q66QLBQ\ahmed reda'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Trusted_Connection=yes;')
cursor = conn.cursor()

def home():
    # Create label
    page_title = Label(home_page, text = "Airline Reservation System")
    page_title.config(font =("Courier", 14))
    page_title.pack(pady=50)

    signUp = tk.Button(home_page, text="Sign Up", command=sign_up, width=10, height=2)
    signUp.place(x=140, y=240)
    signIn = tk.Button(home_page, text="Sign In", command=sign_in, width=10, height=2)
    signIn.place(x=290, y=240)
    

    # # signUp.grid(row=0, column=0, padx=10, pady=10)

    # # signIn.grid(row=0, column=1, padx=10, pady=10)

def pick_date(event):
    global cal, date_window
    date_window = tk.Toplevel()
    date_window.grab_set()
    date_window.geometry("300x300")
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
    global Fname_entry, Lname_entry, email_entry, password_entry, DOB_entry, city_entry, state_entry, zipcode_entry, street_entry, phone_entry, role_option1, role_option2
    home_page.destroy()
    sign_up_page = tk.Tk()
    sign_up_page.geometry("500x500")
    sign_up_page.title("Sign Up")
    #input first name
    Fname_label = tk.Label(sign_up_page, text="First Name")
    Fname_label.pack()
    Fname_label.place(x=10, y=10)
    Fname_entry = tk.Entry(sign_up_page)
    Fname_entry.pack()
    Fname_entry.place(x=100, y=10)
    #input last name
    Lname_label = tk.Label(sign_up_page, text="Last Name")
    Lname_label.pack()
    Lname_label.place(x=10, y=40)
    Lname_entry = tk.Entry(sign_up_page)
    Lname_entry.pack()
    Lname_entry.place(x=100, y=40)
    #input email
    email_label = tk.Label(sign_up_page, text="Email")
    email_label.pack()
    email_label.place(x=10, y=70)
    email_entry = tk.Entry(sign_up_page)
    email_entry.pack()
    email_entry.place(x=100, y=70)
    #input password
    password_label = tk.Label(sign_up_page, text="Password")
    password_label.pack()
    password_label.place(x=10, y=100)
    password_entry = tk.Entry(sign_up_page)
    password_entry.pack()
    password_entry.place(x=100, y=100)
    #input date of birth
    DOB_label = tk.Label(sign_up_page, text="Date of Birth")
    DOB_label.pack()
    DOB_label.place(x=10, y=130)
    global DOB_entry
    DOB_entry= tk.Entry(sign_up_page, highlightthickness=0, relief='flat')
    DOB_entry.pack()
    DOB_entry.place(x=100, y=130)
    DOB_entry.insert(0, 'YYYY-MM-DD')
    DOB_entry.bind("<Button-1>", pick_date)
    #input city 
    city_label = tk.Label(sign_up_page, text="City")
    city_label.pack()
    city_label.place(x=10, y=160)
    city_entry = tk.Entry(sign_up_page)
    city_entry.pack()
    city_entry.place(x=100, y=160)
    #input state 
    state_label = tk.Label(sign_up_page, text="State")
    state_label.pack()
    state_label.place(x=10, y=190)
    state_entry = tk.Entry(sign_up_page)
    state_entry.pack()
    state_entry.place(x=100, y=190)
    #input zipcode 
    zipcode_label = tk.Label(sign_up_page, text="Zipcode")
    zipcode_label.pack()
    zipcode_label.place(x=10, y=220)
    zipcode_entry = tk.Entry(sign_up_page)
    zipcode_entry.pack()
    zipcode_entry.place(x=100, y=220)
    #input zipcode 
    street_label = tk.Label(sign_up_page, text="Street")
    street_label.pack()
    street_label.place(x=10, y=250)
    street_entry = tk.Entry(sign_up_page)
    street_entry.pack()
    street_entry.place(x=100, y=250)
    #input zipcode 
    phone_label = tk.Label(sign_up_page, text="Phone Number")
    phone_label.pack()
    phone_label.place(x=10, y=280)
    phone_entry = tk.Entry(sign_up_page)
    phone_entry.pack()
    phone_entry.place(x=100, y=280)
    #input User role
    role_label =  tk.Label(sign_up_page, text="Select your Role : ")
    role_label.pack()
    role_label.place(x=10, y=310)
    role_option1 = Radiobutton(sign_up_page, text="Customer", value=1)
    role_option1.pack()
    role_option1.place(x=120, y=310)
    role_option2 = Radiobutton(sign_up_page, text="Admin", value=2)
    role_option2.pack()
    role_option2.place(x=220, y=310)
    #submit
    submit_button = tk.Button(sign_up_page, text="Submit", width=10, height=2, command=signup_submit)
    submit_button.pack()
    submit_button.place(x=210, y=390)

def signup_submit():
    if role_option1 == 1:
        role = "Customer"
    else:    
        role = "Admin"
    insert_query = "INSERT INTO PERSON (ID, EMAIL, FNAME, LNAME, PHONENUM, AGE, CITY, PERSON_STATE, ZIPCODE, STREET, PERSON_ROLE) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (20, email_entry.get(), Fname_entry.get(), Lname_entry.get(), phone_entry.get(), 18, city_entry.get(), state_entry.get(), zipcode_entry.get(), street_entry.get(), role)
    cursor.execute(insert_query, values)
    conn.commit()

def sign_in():
    home_page.destroy()
    sign_in_page = tk.Tk()
    sign_in_page.geometry("500x500")
    sign_in_page.title("Sign Ip")
    #input email
    email_label = tk.Label(sign_in_page, text="Email")
    email_label.pack()
    email_label.place(x=10, y=10)
    email_entry = tk.Entry(sign_in_page)
    email_entry.pack()
    email_entry.place(x=100, y=10)

    password_label = tk.Label(sign_in_page, text="password")
    password_label.pack()
    password_label.place(x=10, y=40)
    password_entry = tk.Entry(sign_in_page)
    password_entry.pack()
    password_entry.place(x=100, y=40)
    
    # login(email,pw)

    

# def login(email,pw):


# def updating_user_details():
def add_aircraft():
    add_aircraft_page = tk.Tk()
    add_aircraft_page.geometry("500x500")
    add_aircraft_page.title("Air Craft")
    #input model
    model_label = tk.Label(add_aircraft_page, text="Model")
    model_label.pack()
    model_label.place(x=10, y=10)
    model_entry = tk.Entry(add_aircraft_page, textvariable=aircraft_model)
    model_entry.pack()
    model_entry.place(x=100, y=10)
    #input type
    type_label = tk.Label(add_aircraft_page, text="Type")
    type_label.pack()
    type_label.place(x=10, y=40)
    type_entry = tk.Entry(add_aircraft_page, textvariable=aircraft_type)
    type_entry.pack()
    type_entry.place(x=100, y=40)
    #input capacity
    capacity_label = tk.Label(add_aircraft_page, text="Capacity")
    capacity_label.pack()
    capacity_label.place(x=10, y=70)
    capacity_entry = tk.Entry(add_aircraft_page, textvariable=aircraft_capacity)
    capacity_entry.pack()
    capacity_entry.place(x=100, y=70)
    #input manufacturer
    manufacturer_label = tk.Label(add_aircraft_page, text="Manufacturer")
    manufacturer_label.pack()
    manufacturer_label.place(x=10, y=100)
    manufacturer_entry = tk.Entry(add_aircraft_page, textvariable=aircraft_manufacturer)
    manufacturer_entry.pack()
    manufacturer_entry.place(x=100, y=100)


# def updating_aircraft_details():
# def add_flight():
# def updating_flight_details():


home()
# home_page.resizable(True, True)
home_page.mainloop()