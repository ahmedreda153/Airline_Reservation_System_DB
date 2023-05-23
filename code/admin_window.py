from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import home_window
import signin_window
import admin_functionality
import update_userInfo_window
import logo_gradiant


def admin_page():
    if signin_window.isOpen == True:
        signin_window.sign_in_page.destroy()
        signin_window.isOpen=False
    global administrator_page
    administrator_page = tk.Tk()
    administrator_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    administrator_page.resizable(False, False)

    canvas= Canvas(administrator_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    back_image = ImageTk.PhotoImage(Image.open("F:/database_project/code/plane.png"))
    canvas.create_image(900, 415, image=back_image)
    canvas.back_image = back_image
    canvas.pack()

    back_btn = tk.Button(administrator_page, text="⬅", command= lambda: home_window.back(administrator_page, home_window.home), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)
    administrator_page.title("Admin Page")

    add_aircraft_button = tk.Button(administrator_page, text="Add Aircraft", command=admin_functionality.add_aircraft,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    add_aircraft_button.place(x=159, y=220, width=300, height=100)
    #update aircraft
    update_aircraft_button = tk.Button(administrator_page, text="Update Aircraft", width=20, height=2, command=admin_functionality.update_aircraft,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    update_aircraft_button.place(x=159, y=420,width=300, height=100)
    #delete aircraft
    delete_aircraft_button = tk.Button(administrator_page, text="Delete Aircraft", width=20, height=2, command=admin_functionality.delete_aircraft,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    delete_aircraft_button.place(x=159, y=620,width=300, height=100)
    #add flight
    add_flight_button = tk.Button(administrator_page, text="Add Flight", width=20, height=2, command=admin_functionality.add_flight,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    add_flight_button.place(x=618, y=220,width=300, height=100)
    #update flight
    update_flight_button = tk.Button(administrator_page, text="Update Flight", width=20, height=2, command=admin_functionality.update_flight,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    update_flight_button.place(x=618, y=420,width=300, height=100)
    #delete flight
    delete_flight_button = tk.Button(administrator_page, text="Delete Flight", width=20, height=2, command=admin_functionality.delete_flight,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    delete_flight_button.place(x=618, y=620,width=300, height=100)
    #add_pilot
    add_pilot_button = tk.Button(administrator_page, text="Add Pilot", width=20, height=2, command=admin_functionality.add_pilot,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    add_pilot_button.place(x=1077, y=220,width=300, height=100)
    #assign pilot
    assign_pilot_button = tk.Button(administrator_page, text="Assign Pilot", width=20, height=2, command=admin_functionality.assign_pilotToAircraft,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    assign_pilot_button.place(x=1077, y=420,width=300, height=100)
    #update info
    update_info_button = tk.Button(administrator_page, text="Update Info", width=20, height=2, command=update_userInfo_window.update_info,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    update_info_button.place(x=1077, y=620,width=300, height=100)