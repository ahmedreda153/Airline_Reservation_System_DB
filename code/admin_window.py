from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
import home_window
import signin_window
import admin_functionality
import update_userInfo_window


def admin_page():
    signin_window.sign_in_page.destroy()
    global admin_page
    admin_page = tk.Tk()
    admin_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
    admin_page.title("Admin Page")
    #add aircraft
    add_aircraft_button = tk.Button(admin_page, text="Add Aircraft", width=20, height=2, command=admin_functionality.add_aircraft)
    add_aircraft_button.place(x=10, y=10)
    #update aircraft
    update_aircraft_button = tk.Button(admin_page, text="Update Aircraft", width=20, height=2, command=admin_functionality.update_aircraft)
    update_aircraft_button.place(x=10, y=50)
    #delete aircraft
    delete_aircraft_button = tk.Button(admin_page, text="Delete Aircraft", width=20, height=2, command=admin_functionality.delete_aircraft)
    delete_aircraft_button.place(x=10, y=90)
    #add flight
    add_flight_button = tk.Button(admin_page, text="Add Flight", width=20, height=2, command=admin_functionality.add_flight)
    add_flight_button.place(x=10, y=250)
    #update flight
    update_flight_button = tk.Button(admin_page, text="Update Flight", width=20, height=2, command=admin_functionality.update_flight)
    update_flight_button.place(x=10, y=290)
    #delete flight
    delete_flight_button = tk.Button(admin_page, text="Delete Flight", width=20, height=2, command=admin_functionality.delete_flight)
    delete_flight_button.place(x=10, y=330)
    #update info
    update_info_button = tk.Button(admin_page, text="Update Info", width=20, height=2, command=update_userInfo_window.update_info)
    update_info_button.place(x=10, y=130)
    #add_pilot
    add_pilot_button = tk.Button(admin_page, text="Add Pilot", width=20, height=2, command=admin_functionality.add_pilot)
    add_pilot_button.place(x=10, y=170)
    #assign pilot
    assign_pilot_button = tk.Button(admin_page, text="Assign Pilot", width=20, height=2, command=admin_functionality.assign_pilotToAircraft)
    assign_pilot_button.place(x=10, y=210)