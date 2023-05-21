from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
import DataBase_connection
import home_window
import admin_window

def add_aircraft():
    admin_window.admin_page.destroy()
    global model_entry,type_entry,capacity_entry,manufacturer_entry
    global add_aircraft_page
    add_aircraft_page = tk.Tk()
    add_aircraft_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
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
    DataBase_connection.cursor.execute(insert_query, values)
    DataBase_connection.conn.commit()
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
    DataBase_connection.cursor.execute(select_query)
    rows = DataBase_connection.cursor.fetchall()
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)
    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.pack()

def update_aircraft():
    admin_window.admin_page.destroy()
    global update_aircraft_page
    update_aircraft_page = tk.Tk()
    update_aircraft_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
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
    DataBase_connection.cursor.execute(update_query)
    DataBase_connection.conn.commit()
    done = Label(update_aircraft_page, text = "Aircraft updated successfully")
    done.place(x=180, y=340)
    
def delete_aircraft(): 
    admin_window.admin_page.destroy()
    global delete_aircraft_page
    delete_aircraft_page = tk.Tk()
    delete_aircraft_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
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
    DataBase_connection.cursor.execute(delete_query)
    DataBase_connection.conn.commit()
    done = Label(delete_aircraft_page, text = "Aircraft deleted successfully")
    done.place(x=190, y=330)

def add_flight():
    admin_window.admin_page.destroy()
    global serialNum_entry,flightNum_entry,arrivalTime_entry,departureTime_entry,sourceLocation_entry,destinationLocation_entry,duration_entry,airLine_entry
    global add_flight_page
    add_flight_page = tk.Tk()
    add_flight_page.geometry(f"500x500+{home_window.x}+{home_window.y}")
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
    DataBase_connection.cursor.execute(insert_query, values)
    DataBase_connection.conn.commit()
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
    
    DataBase_connection.cursor.execute(select_query)
    rows = DataBase_connection.cursor.fetchall() 
    # toz fikk
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)

    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.place(x=7, y=70)

def update_flight():
    admin_window.admin_page.destroy()
    global update_flight_page
    update_flight_page = tk.Tk()
    x = int(home_window.screen_width/2 - 800/2)
    y = int(home_window.screen_height/2 - 600/2)
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
    DataBase_connection.cursor.execute(update_query)
    DataBase_connection.conn.commit()
    done = Label(update_flight_page, text = "Flight updated successfully")
    done.place(x=360, y=350)

def delete_flight():
    admin_window.admin_page.destroy()
    global delete_flight_page
    delete_flight_page = tk.Tk()
    x = int(home_window.screen_width/2 - 800/2)
    y = int(home_window.screen_height/2 - 600/2)
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
    DataBase_connection.cursor.execute(delete_query)
    DataBase_connection.conn.commit()

    if DataBase_connection.cursor.rowcount == 0:
        done = Label(delete_flight_page, text="Flight not found")
    else:
        done = Label(delete_flight_page, text="Flight deleted successfully")
        
    done.place(x=190, y=400)