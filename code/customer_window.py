from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
import home_window
import signin_window
import customer_functionality
import update_userInfo_window

isCustomer = False

def customer_page():
    global isCustomer
    isCustomer = True
    signin_window.sign_in_page.destroy()
    global customer_page
    customer_page = tk.Tk()
    customer_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
    customer_page.title("Customer Page")

    book_button = tk.Button(customer_page, text="Book", width=20, height=2, command=customer_functionality.book_flight)
    book_button.place(x=10, y=10)
    
    cancel_button = tk.Button(customer_page, text="Cancel", width=20, height=2, command=customer_functionality.cancel_flight)
    cancel_button.place(x=10, y=50)
    
    class_button = tk.Button(customer_page, text="Change Class", width=20, height=2, command=customer_functionality.change_class)
    class_button.place(x=10, y=90)
    
    update_info_button = tk.Button(customer_page, text="Update Info", width=20, height=2, command=update_userInfo_window.update_info)
    update_info_button.place(x=10, y=130)