import pyodbc
import datetime
from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#sba7 el noor

#connect database
server = 'DESKTOP-Q66QLBQ\SQLEXPRESS'
database = 'AIRLINE_RESERVATION'
username = 'DESKTOP-Q66QLBQ\ahmed reda'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Trusted_Connection=yes;')
cursor = conn.cursor()


def home():
    global home_page, screen_width, screen_height, x, y
    home_page = tk.Tk()
    screen_width = home_page.winfo_screenwidth()
    screen_height = home_page.winfo_screenheight()
    x = int((screen_width / 2) - (500 / 2))
    y = int((screen_height / 2) - (600 / 2))
    home_page.geometry(f"500x500+{x}+{y}")
    home_page.title("Airline Reservation System")
    # Create label
    page_title = Label(home_page, text = "Airline Reservation System")
    page_title.config(font =("Courier", 14))
    page_title.pack(pady=50)

    signUp = tk.Button(home_page, text="Sign Up", command=sign_up, width=10, height=2)
    signUp.place(x=140, y=240)
    signIn = tk.Button(home_page, text="Sign In", command=sign_in, width=10, height=2)
    signIn.place(x=290, y=240)

def pick_date(event):
    global cal, date_window
    date_window = tk.Toplevel()
    date_window.grab_set()
    # date_window.geometry("300x300")
    x = int((screen_width / 2) - (300 / 2))
    y = int((screen_height / 2) - (300 / 2))
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
    cursor.execute(insert_query, values)
    conn.commit()

def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

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
    
def check_valid_login():
    global email
    email = email_entry_login.get()
    select_query = f"select EMAIL, PERSON_PASSWORD, PERSON_ROLE from PERSON WHERE EMAIL = '{email_entry_login.get()}' AND PERSON_PASSWORD = '{password_entry_login.get()}'"
    cursor.execute(select_query)
    result = cursor.fetchone()
    if result == None:
        failed = Label(sign_in_page, text = "login failed")
        failed.place(x=215, y=175)
    elif(result[2]=='Admin'):
        admin_page()
    else:
        customer_page()

def admin_page():
    sign_in_page.destroy()
    global admin_page
    admin_page = tk.Tk()
    admin_page.geometry(f"500x500+{x}+{y}")
    admin_page.title("Admin Page")
    #add aircraft
    add_aircraft_button = tk.Button(admin_page, text="Add Aircraft", width=20, height=2, command=add_aircraft)
    add_aircraft_button.pack()
    add_aircraft_button.place(x=10, y=10)
    #update aircraft
    update_aircraft_button = tk.Button(admin_page, text="Update Aircraft", width=20, height=2, command=update_aircraft)
    update_aircraft_button.pack()
    update_aircraft_button.place(x=10, y=50)
    #delete aircraft
    delete_aircraft_button = tk.Button(admin_page, text="Delete Aircraft", width=20, height=2, command=delete_aircraft)
    delete_aircraft_button.pack()
    delete_aircraft_button.place(x=10, y=90)
    #add flight
    add_flight_button = tk.Button(admin_page, text="Add Flight", width=20, height=2, command=add_flight)
    add_flight_button.pack()
    add_flight_button.place(x=10, y=250)
    #update flight
    update_flight_button = tk.Button(admin_page, text="Update Flight", width=20, height=2, command=update_flight)
    update_flight_button.pack()
    update_flight_button.place(x=10, y=290)
    #delete flight
    delete_flight_button = tk.Button(admin_page, text="Delete Flight", width=20, height=2, command=delete_flight)
    delete_flight_button.pack()
    delete_flight_button.place(x=10, y=330)

def customer_page():
    sign_in_page.destroy()
    global customer_page
    customer_page = tk.Tk()
    customer_page.geometry(f"500x500+{x}+{y}")
    customer_page.title("Customer Page")

    book_button = tk.Button(customer_page, text="Book", width=20, height=2, command=book_flight)
    book_button.pack()
    book_button.place(x=10, y=10)
    
    cancel_button = tk.Button(customer_page, text="Cancel", width=20, height=2, command=cancel_flight)
    cancel_button.pack()
    cancel_button.place(x=10, y=50)
    
    class_button = tk.Button(customer_page, text="Change Class", width=20, height=2, command=change_class)
    class_button.pack()
    class_button.place(x=10, y=90)
    
    update_info_button = tk.Button(customer_page, text="Update Info", width=20, height=2, command=update_info)
    update_info_button.pack()
    update_info_button.place(x=10, y=130)

def change_class():
    customer_page.destroy()
    global change_class_page
    change_class_page = tk.Tk()
    change_class_page.geometry(f"500x500+{x}+{y}")
    change_class_page.title("Customer Page")
    selected_class = tk.IntVar(value=1)
    change_class_label =  tk.Label(change_class_page, text="Select Class : ")
    change_class_label.place(x=10, y=40)

    change_class_option1 = Radiobutton(change_class_page, text="First Class", value=1, variable=selected_class)
    change_class_option1.place(x=120, y=40)

    change_class_option2 = Radiobutton(change_class_page, text="Business Class", value=2, variable=selected_class)
    change_class_option2.place(x=220, y=40) 

    change_class_option3 = Radiobutton(change_class_page, text="Economy Class", value=3, variable=selected_class)
    change_class_option3.place(x=320, y=40) 

    #submit
    submit_button = tk.Button(change_class_page, text="Submit", width=10, height=2, command=change_class_submit)
    submit_button.place(x=210, y=390)
    
def change_class_submit():
    print("")    

def update_info():
    if customer_page:
        customer_page.destroy()
    else:
        admin_page.destroy()
    global update_info_page
    update_info_page = tk.Tk()
    update_info_page.geometry(f"500x500+{x}+{y}")
    global personPass_entry,phoneNum_entry,cityUpdate_entry,personState_entry,streetUpdate_entry,zipCode_entry

    personPass_label = tk.Label(update_info_page, text="Enter the new Password: ")
    personPass_label.place(x=10, y=10)
    personPass_entry = tk.Entry(update_info_page)
    personPass_entry.place(x=180, y=10)

    phoneNum_label = tk.Label(update_info_page, text="Enter the new phone Number: ")
    phoneNum_label.place(x=10, y=40)
    phoneNum_entry = tk.Entry(update_info_page)
    phoneNum_entry.place(x=180, y=40)

    personState_label = tk.Label(update_info_page, text="Enter the State: ")
    personState_label.place(x=10, y=70)
    personState_entry = tk.Entry(update_info_page)
    personState_entry.place(x=180, y=70)

    cityUpdate_label = tk.Label(update_info_page, text="Enter the City: ")
    cityUpdate_label.place(x=10, y=100)
    cityUpdate_entry = tk.Entry(update_info_page)
    cityUpdate_entry.place(x=180, y=100)
    
    streetUpdate_label = tk.Label(update_info_page, text="Enter the Street: ")
    streetUpdate_label.place(x=10, y=130)
    streetUpdate_entry = tk.Entry(update_info_page)
    streetUpdate_entry.place(x=180, y=130)

    zipCode_label = tk.Label(update_info_page, text="Enter the zip code: ")
    zipCode_label.place(x=10, y=160)
    zipCode_entry = tk.Entry(update_info_page)
    zipCode_entry.place(x=180, y=160)

    update_button = tk.Button(update_info_page, text="Update", command=update_data_submit)
    update_button.place(x=215, y=210)

def update_data_submit():
    if personPass_entry.get():
        cursor.execute(f"UPDATE PERSON SET PERSON_PASSWORD = '{personPass_entry.get()}' WHERE EMAIL = '{email}'")
        conn.commit()
    if phoneNum_entry.get():
        cursor.execute(f"UPDATE PERSON SET PHONENUM = '{phoneNum_entry.get()}' WHERE EMAIL = '{email}'")
        conn.commit()
    if personState_entry.get():
        if not cityUpdate_entry.get() or not streetUpdate_entry.get() or not zipCode_entry.get():
            messagebox.showerror("Error", "Please fill all the required fields (City, Street, Zip Code).")
        else:
            cursor.execute(f"UPDATE PERSON SET STATE = '{personState_entry.get()}' WHERE EMAIL = '{email}'")
            conn.commit()
    if cityUpdate_entry.get():
        if not streetUpdate_entry.get() or not zipCode_entry.get():
            messagebox.showerror("Error", "Please fill all the required fields (Street, Zip Code).")
        else:
            cursor.execute(f"UPDATE PERSON SET CITY = '{cityUpdate_entry.get()}' WHERE EMAIL = '{email}'")
            conn.commit()
    if streetUpdate_entry.get():
        if not zipCode_entry.get():
            messagebox.showerror("Error", "Please fill all the required fields (Zip Code).")
        else:
            cursor.execute(f"UPDATE PERSON SET STREET = '{streetUpdate_entry.get()}' WHERE EMAIL = '{email}'")
            conn.commit()
    if zipCode_entry.get():
        cursor.execute(f"UPDATE PERSON SET ZIPCODE = '{zipCode_entry.get()}' WHERE EMAIL = '{email}'")
        conn.commit()

def book_flight():
    customer_page.destroy()
    global source_entry, destination_entry
    global book_flight_page
    book_flight_page = tk.Tk()
    book_flight_page.geometry(f"500x500+{x}+{y}")
    book_flight_page.title("Book Flight")
    #input source
    source_label = tk.Label(book_flight_page, text="source")
    source_label.place(x=10, y=10)
    source_entry = tk.Entry(book_flight_page)
    source_entry.place(x=80, y=10)
    #input des
    destination_label = tk.Label(book_flight_page, text="Destination")
    destination_label.place(x=10, y=40)
    destination_entry = tk.Entry(book_flight_page)
    destination_entry.place(x=80, y=40)
    
    submit_button = tk.Button(book_flight_page, text="search", width=10, height=2, command= book_flight_submit)
    submit_button.place(x=350, y=15)

def book_flight_submit():
    List_flight(book_flight_page, source_entry.get(), destination_entry.get())
    global flight_number_entry
    global selected_class_booking
    
    flight_number_label = tk.Label(book_flight_page, text="Flight Number")
    flight_number_label.place(x=10, y=310)
    flight_number_entry = tk.Entry(book_flight_page)
    flight_number_entry.place(x=100, y=310)

    selected_class_booking = tk.IntVar(value=1)
    class_label =  tk.Label(book_flight_page, text="Select Class : ")
    class_label.place(x=10, y=340)

    class_option1 = Radiobutton(book_flight_page, text="First Class", value=1, variable=selected_class_booking)
    class_option1.place(x=100, y=340)

    class_option2 = Radiobutton(book_flight_page, text="Business Class", value=2, variable=selected_class_booking)
    class_option2.place(x=100, y=370) 

    class_option3 = Radiobutton(book_flight_page, text="Economy Class", value=3, variable=selected_class_booking)
    class_option3.place(x=100, y=400) 
    
    submit_button = tk.Button(book_flight_page, text="Submit", width=10, height=2, command= add_flight_to_customer)
    submit_button.place(x=220, y=450)
    
def add_flight_to_customer():
    select_flight = f"SELECT FLIGHT_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION FROM FLIGHT WHERE FLIGHT_NUM = '{flight_number_entry.get()}'"
    cursor.execute(select_flight)
    result_flight = cursor.fetchone()
    print(result_flight)
    
    print(email)
    select_person = f"SELECT ID, FNAME FROM PERSON WHERE EMAIL = '{email}'"
    cursor.execute(select_person)
    result_person = cursor.fetchone()
    print(result_person)
    print(selected_class_booking.get())
    if selected_class_booking.get() == 1:
        set_class = "First Class"
        price = 1000 * 1.5
    elif selected_class_booking.get() == 2:
        set_class = "Business Class"
        price = 1000 * 1.25
    else:
        set_class = "Economy Class"
        price = 102
    print(price)
    insert_query = f"INSERT INTO TICKET (FLIGHT_NUM, ID, PRICE, PNAME, SOURCE_LOCATION, DESTINATION_LOCATION, SEAT, CLASS, ARRIVAL_TIME, DEPARTURE_TIME) VALUES ('{result_flight[0]}', '{result_person[0]}', '{price}', '{result_person[1]}', '{result_flight[3]}', '{result_flight[4]}', '1', '{set_class}', '{result_flight[1]}', '{result_flight[2]}')"
    cursor.execute(insert_query)
    conn.commit()
    print("inserted")

def cancel_flight():
    print("x")
    print("y")

def add_aircraft():
    admin_page.destroy()
    global model_entry,type_entry,capacity_entry,manufacturer_entry
    global add_aircraft_page
    add_aircraft_page = tk.Tk()
    add_aircraft_page.geometry(f"500x500+{x}+{y}")
    add_aircraft_page.title("Air Craft")
    global model_entry,type_entry,capacity_entry,manufacturer_entry
    #input model
    model_label = tk.Label(add_aircraft_page, text="Model")
    model_label.place(x=10, y=10)
    model_entry = tk.Entry(add_aircraft_page)
    model_entry.place(x=100, y=10)
    #input type
    type_label = tk.Label(add_aircraft_page, text="Type")
    type_label.place(x=10, y=40)
    type_entry = tk.Entry(add_aircraft_page)
    type_entry.place(x=100, y=40)
    #input capacity
    capacity_label = tk.Label(add_aircraft_page, text="Capacity")
    capacity_label.place(x=10, y=70)
    capacity_entry = tk.Entry(add_aircraft_page)
    capacity_entry.place(x=100, y=70)
    #input manufacturer
    manufacturer_label = tk.Label(add_aircraft_page, text="Manufacturer")
    manufacturer_label.place(x=10, y=100)
    manufacturer_entry = tk.Entry(add_aircraft_page)
    manufacturer_entry.place(x=100, y=100)

    submit_button = tk.Button(add_aircraft_page, text="Submit", width=10, height=2, command=add_aircraft_submit)
    submit_button.place(x=210, y=300)

def add_aircraft_submit():
    insert_query="INSERT INTO AIRCRAFT (CAPACITY, MODEL, AIRCRAFT_TYPE, MANUFACTURER) VALUES (?, ?, ?, ?)"
    values = (capacity_entry.get(), model_entry.get(),type_entry.get(), manufacturer_entry.get())
    cursor.execute(insert_query, values)
    conn.commit()
    done = Label(add_aircraft_page, text = "aircraft added successfully")
    done.after(2000, lambda: done.destroy())
    done.place(x=215, y=175)
    
def List_aircraft(page):
    tree = ttk.Treeview(page)
    tree["columns"]=("SERIAL_NUM","AIRCRAFT_TYPE","MODEL", "CAPACITY", "MANUFACTURER")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("SERIAL_NUM", width=100)
    tree.column("AIRCRAFT_TYPE", width=100)
    tree.column("MODEL", width=100)
    tree.column("CAPACITY", width=100)
    tree.column("MANUFACTURER", width=100)

    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("SERIAL_NUM", text="SERIAL_NUM",anchor=tk.CENTER)
    tree.heading("AIRCRAFT_TYPE", text="AIRCRAFT_TYPE",anchor=tk.CENTER)
    tree.heading("MODEL", text="MODEL",anchor=tk.CENTER)
    tree.heading("CAPACITY", text="CAPACITY",anchor=tk.CENTER)
    tree.heading("MANUFACTURER", text="MANUFACTURER",anchor=tk.CENTER)

    select_query = "SELECT SERIAL_NUM, AIRCRAFT_TYPE, MODEL, CAPACITY, MANUFACTURER from AIRCRAFT"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)
    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.pack()

def update_aircraft():
    admin_page.destroy()
    global update_aircraft_page
    update_aircraft_page = tk.Tk()
    update_aircraft_page.geometry(f"500x500+{x}+{y}")
    List_aircraft(update_aircraft_page)
    global aircraft_id_entry, aircraft_capacity_entry
    aircraft_id_label = tk.Label(update_aircraft_page, text="Enter the aircraft id: ")
    aircraft_id_label.place(x=10, y=250)
    aircraft_id_entry = tk.Entry(update_aircraft_page)
    aircraft_id_entry.place(x=200, y=250)
    
    aircraft_capacity_label = tk.Label(update_aircraft_page, text="Enter the aircraft new capacity: ")
    aircraft_capacity_label.place(x=10, y=280)
    aircraft_capacity_entry = tk.Entry(update_aircraft_page)
    aircraft_capacity_entry.place(x=200, y=280)
    #aircraft_status = Entry("Enter the aircraft new status: ")
    submit_button = tk.Button(update_aircraft_page, text="Submit", width=10, height=2, command=update_aircraft_submit)
    submit_button.place(x=210, y=400)
    
def update_aircraft_submit():
    update_query = f"UPDATE AIRCRAFT SET CAPACITY = '{aircraft_capacity_entry.get()}' WHERE SERIAL_NUM = '{aircraft_id_entry.get()}'"
    cursor.execute(update_query)
    conn.commit()
    done = Label(update_aircraft_page, text = "Aircraft updated successfully")
    done.place(x=180, y=340)
    
def delete_aircraft(): 
    admin_page.destroy()
    global delete_aircraft_page
    delete_aircraft_page = tk.Tk()
    delete_aircraft_page.geometry(f"500x500+{x}+{y}")
    List_aircraft(delete_aircraft_page)
    global aircraft_deleted_id_entry
    aircraft_deleted_id_label = tk.Label(delete_aircraft_page, text="Enter the aircraft id: ")
    aircraft_deleted_id_label.place(x=10, y=250)
    aircraft_deleted_id_entry = tk.Entry(delete_aircraft_page)
    aircraft_deleted_id_entry.place(x=150, y=250)
    submit_button = tk.Button(delete_aircraft_page, text="Submit", width=10, height=2, command=delete_aircraft_submit)
    submit_button.place(x=210, y=400)

def delete_aircraft_submit():
    delete_query = f"DELETE FROM AIRCRAFT WHERE SERIAL_NUM ='{aircraft_deleted_id_entry.get()}'"
    cursor.execute(delete_query)
    conn.commit()
    done = Label(delete_aircraft_page, text = "Aircraft deleted successfully")
    done.place(x=190, y=330)

def add_flight():
    admin_page.destroy()
    global serialNum_entry,flightNum_entry,arrivalTime_entry,departureTime_entry,sourceLocation_entry,destinationLocation_entry,duration_entry,airLine_entry
    global add_flight_page
    add_flight_page = tk.Tk()
    add_flight_page.geometry(f"500x500+{x}+{y}")
    add_flight_page.title("Flight")
    List_aircraft(add_flight_page)
    #Serial_Num
    serialNum_label = tk.Label(add_flight_page, text="Aircraft Serial Number")
    serialNum_label.place(x=10, y=240)
    serialNum_entry = tk.Entry(add_flight_page)
    serialNum_entry.place(x=150, y=240)
    #Arrival_Time
    arrivalTime_label = tk.Label(add_flight_page, text="Arrival Time")
    arrivalTime_label.place(x=10, y=270)
    arrivalTime_entry = tk.Entry(add_flight_page)
    arrivalTime_entry.place(x=150, y=270)
    #Departure_Time
    departureTime_label = tk.Label(add_flight_page, text="Departure Time")
    departureTime_label.place(x=10, y=300)
    departureTime_entry = tk.Entry(add_flight_page)
    departureTime_entry.place(x=150, y=300)
    #Source_Location
    sourceLocation_label = tk.Label(add_flight_page, text="Source location")
    sourceLocation_label.place(x=10, y=330)
    sourceLocation_entry = tk.Entry(add_flight_page)
    sourceLocation_entry.place(x=150, y=330)
    #Destination_Location
    destinationLocation_label = tk.Label(add_flight_page, text="Destination Location")
    destinationLocation_label.place(x=10, y=360)
    destinationLocation_entry = tk.Entry(add_flight_page)
    destinationLocation_entry.place(x=150, y=360)
    #Duration_Time
    duration_label = tk.Label(add_flight_page, text="Duration Time")
    duration_label.place(x=10, y=390)
    duration_entry = tk.Entry(add_flight_page)
    duration_entry.place(x=150, y=390)
    #AirLine
    airLine_label = tk.Label(add_flight_page, text="AirLine")
    airLine_label.place(x=10, y=420)
    airLine_entry = tk.Entry(add_flight_page)
    airLine_entry.place(x=150, y=420)
    #Submit
    submit_button = tk.Button(add_flight_page, text="Submit", width=10, height=2, command=add_flight_submit)
    submit_button.place(x=210, y=450)

def add_flight_submit():
    insert_query="INSERT INTO FLIGHT (SERIAL_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, DURATION, AIRLINE) VALUES (?, ?, ?, ?, ?, ?, ?)"
    values = (serialNum_entry.get(), arrivalTime_entry.get(), departureTime_entry.get(),sourceLocation_entry.get(), destinationLocation_entry.get(),duration_entry.get(),airLine_entry.get())
    cursor.execute(insert_query, values)
    conn.commit()
    done = Label(add_flight_page, text = "Flight added successfully")
    done.place(x=310, y=350)

def List_flight(page, source = "default", destination = "default"):
    tree = ttk.Treeview(page)
    tree["columns"]=("FLIGHT_NUM", "SERIAL_NUM", "ARRIVAL_TIME", "DEPARTURE_TIME", "SOURCE_LOCATION", "DESTINATION_LOCATION", "DURATION", "AIRLINE")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("FLIGHT_NUM", width=100)
    tree.column("SERIAL_NUM", width=100)
    tree.column("ARRIVAL_TIME", width=100)
    tree.column("DEPARTURE_TIME", width=120)
    tree.column("SOURCE_LOCATION", width=120)
    tree.column("DESTINATION_LOCATION", width=150)
    tree.column("DURATION", width=90)
    tree.column("AIRLINE", width=100)

    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("FLIGHT_NUM", text="FLIGHT_NUM", anchor=tk.CENTER)
    tree.heading("SERIAL_NUM", text="SERIAL_NUM", anchor=tk.CENTER)
    tree.heading("ARRIVAL_TIME", text="ARRIVAL_TIME", anchor=tk.CENTER)
    tree.heading("DEPARTURE_TIME", text="DEPARTURE_TIME", anchor=tk.CENTER)
    tree.heading("SOURCE_LOCATION", text="SOURCE_LOCATION", anchor=tk.CENTER)
    tree.heading("DESTINATION_LOCATION", text="DESTINATION_LOCATION", anchor=tk.CENTER)
    tree.heading("DURATION", text="DURATION", anchor=tk.CENTER)
    tree.heading("AIRLINE", text="AIRLINE", anchor=tk.CENTER)
    
    if source == "default" and destination == "default":
        select_query = "SELECT * FROM FLIGHT"
    else:
        select_query = f"SELECT FLIGHT_NUM, SERIAL_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, DURATION, AIRLINE FROM FLIGHT WHERE SOURCE_LOCATION='{source}' AND DESTINATION_LOCATION='{destination}'"
    
    cursor.execute(select_query)
    rows = cursor.fetchall() 
    # toz fikk
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)

    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.place(x=7, y=70)

def update_flight():
    admin_page.destroy()
    global update_flight_page
    update_flight_page = tk.Tk()
    x = int(screen_width/2 - 800/2)
    y = int(screen_height/2 - 600/2)
    update_flight_page.geometry(f"900x500+{x}+{y}")
    List_flight(update_flight_page)
    global flightNUM_id_entry, flightserial_id_entry,flightArrivalTime_entry,flightDEPARTURETime_entry
    flightNUM_id_entry_label = tk.Label(update_flight_page, text="Enter the flight Number: ")
    flightNUM_id_entry_label.place(x=10, y=10)
    flightNUM_id_entry= tk.Entry(update_flight_page)
    flightNUM_id_entry.place(x=170, y=10)

    flightArrivalTime_entry_label = tk.Label(update_flight_page, text="Enter the New Arrival Time: ")
    flightArrivalTime_entry_label.place(x=10, y=40)
    flightArrivalTime_entry= tk.Entry(update_flight_page)
    flightArrivalTime_entry.place(x=170, y=40)

    flightDEPARTURETime_entry_label = tk.Label(update_flight_page, text="Enter the New DEPARTURE Time: ")
    flightDEPARTURETime_entry_label.place(x=300, y=40)
    flightDEPARTURETime_entry= tk.Entry(update_flight_page)
    flightDEPARTURETime_entry.place(x=480, y=40)

    submit_button = tk.Button(update_flight_page, text="Submit", width=10, height=2, command=update_flight_submit)
    submit_button.place(x=400, y=400)

def update_flight_submit():
    update_query = f"UPDATE FLIGHT SET ARRIVAL_TIME = '{flightArrivalTime_entry.get()}', DEPARTURE_TIME = '{flightDEPARTURETime_entry.get()}' WHERE FLIGHT_NUM = '{flightNUM_id_entry.get()}'"
    cursor.execute(update_query)
    conn.commit()
    done = Label(update_flight_page, text = "Flight updated successfully")
    done.place(x=360, y=350)

def delete_flight():
    admin_page.destroy()
    global delete_flight_page
    delete_flight_page = tk.Tk()
    x = int(screen_width/2 - 800/2)
    y = int(screen_height/2 - 600/2)
    delete_flight_page.geometry(f"900x500+{x}+{y}")
    List_flight(delete_flight_page)
    global flight_deleted_id_entry
    flight_deleted_id_label = tk.Label(delete_flight_page, text="Enter the Flight id: ")
    flight_deleted_id_label.place(x=10, y=20)
    flight_deleted_id_entry = tk.Entry(delete_flight_page)
    flight_deleted_id_entry.place(x=150, y=20)
    submit_button = tk.Button(delete_flight_page, text="Submit", width=10, height=2, command=delete_flight_submit)
    submit_button.place(x=350, y=10)

def delete_flight_submit():
    delete_query = f"DELETE FROM FLIGHT WHERE FLIGHT_NUM ='{flight_deleted_id_entry.get()}'"
    cursor.execute(delete_query)
    conn.commit()

    if cursor.rowcount == 0:
        done = Label(delete_flight_page, text="Flight not found")
    else:
        done = Label(delete_flight_page, text="Flight deleted successfully")
        
    done.place(x=190, y=400)


home()
home_page.mainloop()