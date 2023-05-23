import datetime
from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import DataBase_connection
import home_window
import logo_gradiant
from tkinter import ttk
from ttkthemes import ThemedStyle
import signin_window


def pick_date(event):
    global cal, date_window
    date_window = tk.Toplevel()
    date_window.grab_set()
    x = int((home_window.screen_width / 2) - (300 / 2))
    y = int((home_window.screen_height / 2) - (300 / 2))
    date_window.geometry(f"300x300+{x}+{y}")
    date_window.title("Pick Date")
    cal = Calendar(date_window, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)
    submit = tk.Button(date_window, text="PICK", command=lambda: grab_date(event.widget), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    submit.pack(pady=20)
    
def grab_date(test):
    test.delete(0, END)
    test.config(fg="black")
    test.insert(0, cal.get_date())
    date_window.destroy()

def calculate_age(dob):
    today = datetime.date.today()
    age = today.year - dob.year
    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1
    return age

def sign_up():
    global Fname_entry, Lname_entry, email_entry, password_entry, DOB_entry, city_entry, state_entry, zipcode_entry, street_entry, phone_entry, selected_role,sign_up_page
    home_window.home_page.destroy()
    home_window.home_isOpened = False
    sign_up_page = tk.Tk()
    sign_up_page.title("Sign Up")
    sign_up_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(sign_up_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(sign_up_page, text="⬅", command= lambda: home_window.back(sign_up_page, home_window.home), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER)

    #input first name
    canvas.create_text(home_window.screen_width / 2 - 440, 170, text="First Name", fill="black", font =("Trebuchet MS", 24))
    Fname_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    Fname_entry.place(x=500, y=157.5,width=250,height=30)
    
    # input last name
    canvas.create_text(home_window.screen_width - 627, 170, text="Last Name", fill="black", font =("Trebuchet MS", 24))
    Lname_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    Lname_entry.place(x=1055, y=157.5, width=250,height=30)

    #input email
    canvas.create_text(home_window.screen_width / 2 - 478, 270, text="Email", fill="black", font =("Trebuchet MS", 24))
    email_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    email_entry.place(x=500, y=257.5, width=250,height=30)

    #input password
    canvas.create_text(home_window.screen_width - 636 , 270, text="Password", fill="black", font =("Trebuchet MS", 24))
    password_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15), show="*")
    password_entry.place(x=1055, y=257.5,width=250,height=30)

    #input date of birth
    canvas.create_text(home_window.screen_width / 2 - 427, 370, text="Date of Birth", fill="black", font =("Trebuchet MS", 24))
    global DOB_entry
    DOB_entry= tk.Entry(sign_up_page, font=("Trebuchet MS", 15), fg="grey", justify="center")
    DOB_entry.place(x=500, y=357.5,width=250,height=30)
    DOB_entry.insert(0, 'YYYY-MM-DD')
    DOB_entry.bind("<Button-1>", pick_date)

    #input city 
    canvas.create_text(home_window.screen_width - 670 , 370, text="CITY", fill="black", font =("Trebuchet MS", 24))
    city_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    city_entry.place(x=1055, y=357.5,width=250,height=30)

    #input state 
    canvas.create_text(home_window.screen_width / 2 - 480, 470, text="State", fill="black", font =("Trebuchet MS", 24))
    state_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    state_entry.place(x=500, y=457.5,width=250,height=30)

    #input zipcode 
    canvas.create_text(home_window.screen_width - 640 , 470, text="ZIPCODE", fill="black", font =("Trebuchet MS", 24))
    zipcode_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    zipcode_entry.place(x=1055, y=457.5,width=250,height=30)

    #input street
    canvas.create_text(home_window.screen_width / 2 - 473, 570, text="Street", fill="black", font =("Trebuchet MS", 24))
    street_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    street_entry.place(x=500, y=557.5,width=250,height=30)

    #input phonenumber
    canvas.create_text(home_window.screen_width -600 , 570, text="Phone Number", fill="black", font =("Trebuchet MS", 24))
    phone_entry = tk.Entry(sign_up_page, font=("Trebuchet MS", 15))
    phone_entry.place(x=1055, y=557.5,width=250,height=30)

    selected_role = 1
    #input role
    canvas.create_text(home_window.screen_width / 2 - 400, 650, text="Select your Role:", fill="black", font =("Trebuchet MS", 24))
    global radiobtn_photo1, radiobtn1, radiobtn_photo2, radiobtn2
    radiobtn_photo1 = PhotoImage(file="F:\database_project\code\\Radio Button 1 mt7dd.png") # write the full path of the image in your computer
    radiobtn1 = tk.Button(sign_up_page, image=radiobtn_photo1, command=lambda: select_role(1), bd=0)
    radiobtn1.place(x=545, y=655, anchor=CENTER, height=20, width=20)
    canvas.create_text(615, 655, text="Customer", fill="black", font =("Trebuchet MS", 16))
    radiobtn_photo2 = PhotoImage(file="F:\database_project\code\\Radio Button 1 fady.png")
    radiobtn2 = tk.Button(sign_up_page, image=radiobtn_photo2, command=lambda: select_role(2), bd=0)
    radiobtn2.place(x=755, y=655, anchor=CENTER, height=20, width=20)
    canvas.create_text(810, 655, text="Admin", fill="black", font =("Trebuchet MS", 16))

    #submit
    submit_button = tk.Button(sign_up_page, text="REGISTER", command=lambda:signup_submit(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    submit_button.place(x=home_window.screen_width / 2 - 100, y=home_window.screen_height - 130, width=200, height=50)

def select_role(role):
    global selected_role
    selected_role = role
    if role == 1:
        radiobtn1.config(image=radiobtn_photo1)
        radiobtn2.config(image=radiobtn_photo2)
        selected_role = 1
    else:
        radiobtn1.config(image=radiobtn_photo2)
        radiobtn2.config(image=radiobtn_photo1)
        selected_role = 2

def signup_submit(event):
    if Fname_entry.get() == "" or Lname_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "" or phone_entry.get() == "" or city_entry.get() == "" or state_entry.get() == "" or zipcode_entry.get() == "" or street_entry.get() == "" or DOB_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 700, text="Please Fill All The Fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        if selected_role == 1:
            role = "Customer"
        else:    
            role = "Admin"
        insert_query = "INSERT INTO PERSON (EMAIL, FNAME, LNAME, PERSON_PASSWORD, PHONENUM, AGE, CITY, PERSON_STATE, ZIPCODE, STREET, PERSON_ROLE, DOB) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        dob = datetime.datetime.strptime(DOB_entry.get(), "%Y-%m-%d")
        age = calculate_age(dob)
        values = (email_entry.get(), Fname_entry.get(), Lname_entry.get(), password_entry.get(), phone_entry.get(), age, city_entry.get(), state_entry.get(), zipcode_entry.get(), street_entry.get(), role, DOB_entry.get())
        DataBase_connection.cursor.execute(insert_query, values)
        DataBase_connection.conn.commit()
        sign_up_page.destroy()
        signin_window.sign_in()