from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import DataBase_connection
import home_window
import signin_window
import customer_window
import admin_window

def update_info():
    if customer_window.isCustomer == True:
        customer_window.customer_page.destroy()
    else:
        admin_window.admin_page.destroy()
    global update_info_page, personPass_entry,phoneNum_entry,cityUpdate_entry,personState_entry,streetUpdate_entry,zipCode_entry
    update_info_page = tk.Tk()
    update_info_page.title("Update Info")
    update_info_page.geometry(f"500x500+{home_window.x}+{home_window.y}")

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