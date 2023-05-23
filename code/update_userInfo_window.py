from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import DataBase_connection
import home_window
import signin_window
import customer_window
import admin_window
import logo_gradiant

def update_info():
    if customer_window.isCustomer == True:
        customer_window.user_page.destroy()
    else:
        admin_window.administrator_page.destroy()

    global update_info_page, personPass_entry, phoneNum_entry, cityUpdate_entry, personState_entry, streetUpdate_entry, zipCode_entry
    update_info_page = tk.Tk()
    update_info_page.title("Update Info")
    update_info_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(update_info_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    if customer_window.isCustomer == True:
        back_btn = tk.Button(update_info_page, text="⬅", command= lambda: home_window.back(update_info_page, customer_window.customer_page), font=(50), bd=0, bg="white", fg="black")
        back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)
    else:
        back_btn = tk.Button(update_info_page, text="⬅", command= lambda: home_window.back(update_info_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
        back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)
    customer_window.isCustomer = False
    canvas.create_text(home_window.screen_width / 2 - 350 , 200, anchor=tk.NW, text="Enter the Password ", fill="black", font =("Trebuchet MS", 24))
    personPass_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15), show="*")
    personPass_entry.place(x=800, y=207, width=250, height=30)

    canvas.create_text(home_window.screen_width / 2 - 350 , 280, anchor=tk.NW, text="Enter the phone Number ", fill="black", font =("Trebuchet MS", 24))
    phoneNum_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15))
    phoneNum_entry.place(x=800, y=287, width=250, height=30)

    canvas.create_text(home_window.screen_width / 2 - 350 , 360, anchor=tk.NW, text="Enter the State ", fill="black", font =("Trebuchet MS", 24))
    personState_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15))
    personState_entry.place(x=800, y=367, width=250, height=30)

    canvas.create_text(home_window.screen_width / 2 - 350 , 440, anchor=tk.NW, text="Enter the City ", fill="black", font =("Trebuchet MS", 24))
    cityUpdate_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15))
    cityUpdate_entry.place(x=800, y=447, width=250, height=30)
    
    canvas.create_text(home_window.screen_width / 2 - 350 , 520, anchor=tk.NW, text="Enter the Street ", fill="black", font =("Trebuchet MS", 24))
    streetUpdate_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15))
    streetUpdate_entry.place(x=800, y=527, width=250, height=30)

    canvas.create_text(home_window.screen_width / 2 - 350 , 600, anchor=tk.NW, text="Enter the Zip Code ", fill="black", font =("Trebuchet MS", 24))
    zipCode_entry = tk.Entry(update_info_page,font=("Trebuchet MS", 15))
    zipCode_entry.place(x=800, y=607, width=250, height=30)

    update_button = tk.Button(update_info_page, text="UPDATE", command=lambda:update_data_submit(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    update_button.place(x=643, y=710, width=250, height=50)

def update_data_submit(event):
    if personPass_entry.get() == "" and phoneNum_entry.get() == "" and personState_entry.get() == "" and cityUpdate_entry.get() == "" and streetUpdate_entry.get() == "" and zipCode_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 685, text="Please fill all the required fields.", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, event.delete, error_message)
    else:
        if personPass_entry.get():
            DataBase_connection.cursor.execute(f"UPDATE PERSON SET PERSON_PASSWORD = '{personPass_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
            DataBase_connection.conn.commit()
        if phoneNum_entry.get():
            DataBase_connection.cursor.execute(f"UPDATE PERSON SET PHONENUM = '{phoneNum_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
            DataBase_connection.conn.commit()
        if personState_entry.get():
            if not cityUpdate_entry.get() or not streetUpdate_entry.get() or not zipCode_entry.get():
                messagebox.showerror("Error", "Please fill all the required fields (City, Street, Zip Code).")
            else:
                DataBase_connection.cursor.execute(f"UPDATE PERSON SET STATE = '{personState_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
                DataBase_connection.conn.commit()
        if cityUpdate_entry.get():
            if not streetUpdate_entry.get() or not zipCode_entry.get():
                messagebox.showerror("Error", "Please fill all the required fields (Street, Zip Code).")
            else:
                DataBase_connection.cursor.execute(f"UPDATE PERSON SET CITY = '{cityUpdate_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
                DataBase_connection.conn.commit()
        if streetUpdate_entry.get():
            if not zipCode_entry.get():
                messagebox.showerror("Error", "Please fill all the required fields (Zip Code).")
            else:
                DataBase_connection.cursor.execute(f"UPDATE PERSON SET STREET = '{streetUpdate_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
                DataBase_connection.conn.commit()
        if zipCode_entry.get():
            DataBase_connection.cursor.execute(f"UPDATE PERSON SET ZIPCODE = '{zipCode_entry.get()}' WHERE EMAIL = '{signin_window.email}'")
            DataBase_connection.conn.commit()   
   