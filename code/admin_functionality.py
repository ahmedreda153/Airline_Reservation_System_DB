from tkinter import *
from tkcalendar import *
import tkinter as tk
import datetime
from tkinter import ttk
from PIL import ImageTk, Image
import DataBase_connection
import home_window
import admin_window
import signup_window
import logo_gradiant

def add_aircraft():
    admin_window.administrator_page.destroy()
    global model_entry,type_entry,capacity_entry,manufacturer_entry
    global add_aircraft_page

    add_aircraft_page = tk.Tk()
    add_aircraft_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    add_aircraft_page.resizable(False, False)

    canvas= Canvas(add_aircraft_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(add_aircraft_page, text="⬅", command= lambda: home_window.back(add_aircraft_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    add_aircraft_page.title("Add Air Craft")
    global model_entry,type_entry,capacity_entry,manufacturer_entry
    #page title
    canvas.create_text(home_window.screen_width / 2 - 170 , 150, anchor=tk.NW, text="Add An Aircraft", fill="black", font =("Trebuchet MS", 36, "bold"))
    #input type
    canvas.create_text(home_window.screen_width / 2 - 300 , 260, anchor=tk.NW, text="Type ", fill="black", font =("Trebuchet MS", 24))
    type_entry = tk.Entry(add_aircraft_page,font=("Trebuchet MS", 15))
    type_entry.place(x=800, y=267, width=250, height=30)
    #input model
    canvas.create_text(home_window.screen_width / 2 - 300 , 360, anchor=tk.NW, text="Model ", fill="black", font =("Trebuchet MS", 24))
    model_entry = tk.Entry(add_aircraft_page,font=("Trebuchet MS", 15))
    model_entry.place(x=800, y=367, width=250, height=30)
    #input capacity
    canvas.create_text(home_window.screen_width / 2 - 300 , 460, anchor=tk.NW, text="Capacity ", fill="black", font =("Trebuchet MS", 24))
    capacity_entry = tk.Entry(add_aircraft_page,font=("Trebuchet MS", 15))
    capacity_entry.place(x=800, y=467, width=250, height=30)
    #input manufacturer
    canvas.create_text(home_window.screen_width / 2 - 300 , 560, anchor=tk.NW, text="Manufacturer ", fill="black", font =("Trebuchet MS", 24))
    manufacturer_entry = tk.Entry(add_aircraft_page,font=("Trebuchet MS", 15))
    manufacturer_entry.place(x=800, y=567, width=250, height=30)

    update_button = tk.Button(add_aircraft_page, text="ADD AIRCRAFT", command= lambda:add_aircraft_submit(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    update_button.place(x=home_window.screen_width / 2 - 100, y=700, width=250, height=50)

def add_aircraft_submit(event):
    if model_entry.get() == "" or type_entry.get() == "" or capacity_entry.get() == "" or manufacturer_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please fill all the fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        insert_query="INSERT INTO AIRCRAFT (CAPACITY, MODEL, AIRCRAFT_TYPE, MANUFACTURER) VALUES (?, ?, ?, ?)"
        values = (capacity_entry.get(), model_entry.get(),type_entry.get(), manufacturer_entry.get())
        DataBase_connection.cursor.execute(insert_query, values)
        DataBase_connection.conn.commit()
        message = event.create_text(home_window.screen_width / 2, 670, text="Aircraft added successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(message))
        type_entry.delete(0, END)
        model_entry.delete(0, END)
        capacity_entry.delete(0, END)
        manufacturer_entry.delete(0, END)
    
def List_aircraft(page, x_axis = 0, y_axis = 0):
    for widget in page.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()  
    tree = ttk.Treeview(page)
    style =ttk.Style()
    tree["columns"]=("SERIAL_NUM","AIRCRAFT_TYPE","MODEL", "CAPACITY", "MANUFACTURER")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("SERIAL_NUM", width=153)
    tree.column("AIRCRAFT_TYPE", width=180)
    tree.column("MODEL", width=153)
    tree.column("CAPACITY", width=120)
    tree.column("MANUFACTURER", width=170)

    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("SERIAL_NUM", text="SERIAL_NUM",anchor=tk.CENTER)
    tree.heading("AIRCRAFT_TYPE", text="AIRCRAFT_TYPE",anchor=tk.CENTER)
    tree.heading("MODEL", text="MODEL",anchor=tk.CENTER)
    tree.heading("CAPACITY", text="CAPACITY",anchor=tk.CENTER)
    tree.heading("MANUFACTURER", text="MANUFACTURER",anchor=tk.CENTER)
    style.configure("Treeview.Heading", foreground="black", font=("Trebuchet MS", 16, "bold"))
    style.configure("Treeview.Column", foreground="black", font=("Trebuchet MS", 6, "bold"))

    select_query = "SELECT SERIAL_NUM, AIRCRAFT_TYPE, MODEL, CAPACITY, MANUFACTURER from AIRCRAFT"
    DataBase_connection.cursor.execute(select_query)
    rows = DataBase_connection.cursor.fetchall()
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)
    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.place(x=x_axis, y=y_axis)
    # Configure tags to color rows
    tree.tag_configure("oddrow", background="#e9f2f7")
    tree.tag_configure("evenrow", background="#91b9cf")
    tree.tag_configure("customfont", font=("Trebuchet MS",12, "normal"))

    # Apply tags to alternate rows
    for i in range(len(tree.get_children())):
        if i % 2 == 0:
            tree.item(tree.get_children()[i], tags=("customfont","evenrow"))
        else:
            tree.item(tree.get_children()[i], tags=("customfont","oddrow"))
    
    tree_height = len(tree.get_children())
    tree["height"] = tree_height
    if tree_height > 10:
        tree["height"] = 10

def update_aircraft():
    admin_window.administrator_page.destroy()
    global update_aircraft_page
    update_aircraft_page = tk.Tk()
    update_aircraft_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    update_aircraft_page.resizable(False, False)

    canvas= Canvas(update_aircraft_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(update_aircraft_page, text="⬅", command= lambda: home_window.back(update_aircraft_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    List_aircraft(update_aircraft_page, home_window.screen_width / 2 - 40, 200)
    global aircraft_id_entry, aircraft_capacity_entry
    canvas.create_text(177, 310, text="AirCraft ID", fill="black", font =("Trebuchet MS", 24))
    aircraft_id_entry = tk.Entry(update_aircraft_page,font=("Trebuchet MS", 15))
    aircraft_id_entry.place(x=350, y=300,width=250,height=30)

    canvas.create_text(200, 410, text="New Capacity", fill="black", font =("Trebuchet MS", 24))
    aircraft_capacity_entry =tk.Entry(update_aircraft_page,font=("Trebuchet MS", 15)) 
    aircraft_capacity_entry.place(x=350, y=400,width=250,height=30)
    tk.Entry(update_aircraft_page,font=("Trebuchet MS", 15))
    submit_button = tk.Button(update_aircraft_page, text="Update Aircraft", command=lambda:update_aircraft_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)
    
def update_aircraft_submit(event):
    if aircraft_id_entry.get() == "" or aircraft_capacity_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please fill all the fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        update_query = f"UPDATE AIRCRAFT SET CAPACITY = '{aircraft_capacity_entry.get()}' WHERE SERIAL_NUM = '{aircraft_id_entry.get()}'"
        DataBase_connection.cursor.execute(update_query)
        DataBase_connection.conn.commit()
        List_aircraft(update_aircraft_page, home_window.screen_width / 2 - 40, 200)
        Message = event.create_text(home_window.screen_width / 2, 670, text="Aircraft Updated Successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(Message))
    List_aircraft(update_aircraft_page, home_window.screen_width / 2 - 40, 200)
    aircraft_id_entry.delete(0, END)
    aircraft_capacity_entry.delete(0, END)
    
def delete_aircraft(): 
    admin_window.administrator_page.destroy()
    global delete_aircraft_page, aircraft_deleted_id_entry

    delete_aircraft_page = tk.Tk()
    delete_aircraft_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    delete_aircraft_page.resizable(False, False)

    canvas= Canvas(delete_aircraft_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(delete_aircraft_page, text="⬅", command= lambda: home_window.back(delete_aircraft_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    List_aircraft(delete_aircraft_page, home_window.screen_width / 2 - 40, 200)
    canvas.create_text(200, 350, text="AirCraft ID", fill="black", font =("Trebuchet MS", 24))
    aircraft_deleted_id_entry = tk.Entry(delete_aircraft_page,font=("Trebuchet MS", 15))
    aircraft_deleted_id_entry.place(x=350, y=340,width=250,height=30)

    submit_button = tk.Button(delete_aircraft_page, text="DELETE AIRCRAFT", command=lambda:delete_aircraft_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def delete_aircraft_submit(event):
    if aircraft_deleted_id_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please enter the Aircraft ID", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        delete_query = f"DELETE FROM AIRCRAFT WHERE SERIAL_NUM ='{aircraft_deleted_id_entry.get()}'"
        DataBase_connection.cursor.execute(delete_query)
        DataBase_connection.conn.commit()
        List_aircraft(delete_aircraft_page, home_window.screen_width / 2 - 40, 200)
        Message = event.create_text(home_window.screen_width / 2, 670, text="Aircraft Deleted Successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(Message))
        aircraft_deleted_id_entry.delete(0, END)

def add_flight():
    admin_window.administrator_page.destroy()
    global serialNum_entry,flightNum_entry,arrivalTime_entry,departureTime_entry,sourceLocation_entry,destinationLocation_entry,duration_entry,airLine_entry,price_entry
    global add_flight_page

    add_flight_page = tk.Tk()
    add_flight_page.resizable(False, False)
    add_flight_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(add_flight_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    add_flight_page.title("Flight")
    List_aircraft(add_flight_page,home_window.screen_width / 2 - 40, 200)
    back_btn = tk.Button(add_flight_page, text="⬅", command= lambda: home_window.back(add_flight_page, admin_window.admin_page),font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)
    #Serial_Num
    canvas.create_text(200, 220, text="Aircraft Serial Number", fill="black", font =("Trebuchet MS", 24))
    serialNum_entry = tk.Entry(add_flight_page,font=("Trebuchet MS", 15))
    serialNum_entry.place(x=390, y=210,width=250,height=30)
    #Arrival_Time
    canvas.create_text(127, 280, text="Arrival Time", fill="black", font =("Trebuchet MS", 24))
    arrivalTime_entry = logo_gradiant.CustomEntry(add_flight_page, "YYYY-MM-DD HH:MM:SS", font=("Trebuchet MS", 15), fg="grey", justify="center")
    arrivalTime_entry.place(x=390, y=270,width=250,height=30)
    #Departure_Time
    canvas.create_text(150, 340, text="Departure Time", fill="black", font =("Trebuchet MS", 24))
    departureTime_entry = logo_gradiant.CustomEntry(add_flight_page, "YYYY-MM-DD HH:MM:SS", font=("Trebuchet MS", 15), fg="grey", justify="center")
    departureTime_entry.place(x=390, y=330,width=250,height=30)
    #Source_Location
    canvas.create_text(150, 400, text="Source location", fill="black", font =("Trebuchet MS", 24))
    sourceLocation_entry = tk.Entry(add_flight_page,font=("Trebuchet MS", 15))
    sourceLocation_entry.place(x=390, y=390,width=250,height=30)
    #Destination_Location
    canvas.create_text(187, 460, text="Destination Location", fill="black", font =("Trebuchet MS", 24))
    destinationLocation_entry = tk.Entry(add_flight_page,font=("Trebuchet MS", 15))
    destinationLocation_entry.place(x=390, y=450,width=250,height=30)
    #AirLine
    canvas.create_text(122, 520, text="Flight Price", fill="black", font =("Trebuchet MS", 24))
    price_entry = tk.Entry(add_flight_page,font=("Trebuchet MS", 15))
    price_entry.place(x=390, y=510,width=250,height=30)
    #Price
    canvas.create_text(87, 580, text="Airline", fill="black", font =("Trebuchet MS", 24))
    airLine_entry = tk.Entry(add_flight_page,font=("Trebuchet MS", 15))
    airLine_entry.place(x=390, y=570,width=250,height=30)
    #Submit
    submit_button = tk.Button(add_flight_page, text="Add Flight", command=lambda: add_flight_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def add_flight_submit(event):
    if serialNum_entry.get() == "" or arrivalTime_entry.get() == "" or departureTime_entry.get() == "" or sourceLocation_entry.get() == "" or destinationLocation_entry.get() == "" or airLine_entry.get() == "" or price_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please fill all the fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        insert_query="INSERT INTO FLIGHT (SERIAL_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, AIRLINE, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (serialNum_entry.get(), arrivalTime_entry.get(), departureTime_entry.get(), sourceLocation_entry.get(), destinationLocation_entry.get(),airLine_entry.get(),price_entry.get())
        DataBase_connection.cursor.execute(insert_query, values)
        DataBase_connection.conn.commit()
        message = event.create_text(home_window.screen_width / 2, 670, text="Flight added successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(message))
        serialNum_entry.delete(0, END)
        arrivalTime_entry.delete(0, END)
        arrivalTime_entry.insert(0, "YYYY-MM-DD HH:MM:SS")
        departureTime_entry.delete(0, END)
        departureTime_entry.insert(0, "YYYY-MM-DD HH:MM:SS")
        sourceLocation_entry.delete(0, END)
        destinationLocation_entry.delete(0, END)
        price_entry.delete(0, END)
        airLine_entry.delete(0, END)

def List_flight(page, source = "default", destination = "default", x_axis = 0, y_axis = 0):
    for widget in page.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()    
    style =ttk.Style()
    tree = ttk.Treeview(page)
    tree["columns"]=("FLIGHT_NUM", "SERIAL_NUM", "ARRIVAL_TIME", "DEPARTURE_TIME", "SOURCE_LOCATION", "DESTINATION_LOCATION", "PRICE", "AIRLINE")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("FLIGHT_NUM", width=170)
    tree.column("SERIAL_NUM", width=170)
    tree.column("ARRIVAL_TIME", width=192)
    tree.column("DEPARTURE_TIME", width=192)
    tree.column("SOURCE_LOCATION", width=192)
    tree.column("DESTINATION_LOCATION", width=192)
    tree.column("PRICE", width=140)
    tree.column("AIRLINE", width=192)

    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("FLIGHT_NUM", text="FLIGHT_NUM", anchor=tk.CENTER)
    tree.heading("SERIAL_NUM", text="SERIAL_NUM", anchor=tk.CENTER)
    tree.heading("ARRIVAL_TIME", text="ARRIVAL_TIME", anchor=tk.CENTER)
    tree.heading("DEPARTURE_TIME", text="DEPARTURE_TIME", anchor=tk.CENTER)
    tree.heading("SOURCE_LOCATION", text="SOURCE", anchor=tk.CENTER)
    tree.heading("DESTINATION_LOCATION", text="DESTINATION", anchor=tk.CENTER)
    tree.heading("PRICE", text="PRICE", anchor=tk.CENTER)
    tree.heading("AIRLINE", text="AIRLINE", anchor=tk.CENTER)
    style.configure("Treeview.Heading", foreground="black", font=("Trebuchet MS", 16, "bold"))
    style.configure("Treeview.Column", foreground="black", font=("Trebuchet MS", 6, "bold"))

    if source == "default" and destination == "default":
        select_query = "SELECT FLIGHT_NUM, SERIAL_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, PRICE, AIRLINE FROM FLIGHT"
    else:
        select_query = f"SELECT FLIGHT_NUM, SERIAL_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, PRICE, AIRLINE FROM FLIGHT WHERE SOURCE_LOCATION='{source}' AND DESTINATION_LOCATION='{destination}'"
    
    DataBase_connection.cursor.execute(select_query)
    rows = DataBase_connection.cursor.fetchall()

    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)

    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.place(x=x_axis, y=y_axis)
    # Configure tags to color rows
    tree.tag_configure("oddrow", background="#e9f2f7")
    tree.tag_configure("evenrow", background="#91b9cf")
    tree.tag_configure("customfont", font=("Trebuchet MS",12, "normal"), foreground="black")

    # Apply tags to alternate rows
    for i in range(len(tree.get_children())):
        if i % 2 == 0:
            tree.item(tree.get_children()[i], tags=("customfont","evenrow"))
        else:
            tree.item(tree.get_children()[i], tags=("customfont","oddrow"))
    
    tree_height = len(tree.get_children())
    tree["height"] = tree_height
    if tree_height > 10:
        tree["height"] = 10

def update_flight():
    admin_window.administrator_page.destroy()
    global update_flight_page

    update_flight_page = tk.Tk()
    update_flight_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    update_flight_page.resizable(False, False)

    canvas= Canvas(update_flight_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    update_flight_page.title("Update Flight")

    back_btn = tk.Button(update_flight_page, text="⬅", command= lambda: home_window.back(update_flight_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    List_flight(update_flight_page, "default", "default", 30, 200)
    global flightNUM_id_entry, flightserial_id_entry,flightArrivalTime_entry,flightDEPARTURETime_entry,price_updated_entry
    canvas.create_text(253, 500, text="Enter The Flight Number", font=("Trebuchet MS", 24), fill="black")
    flightNUM_id_entry= tk.Entry(update_flight_page,font=("Trebuchet MS", 15))
    flightNUM_id_entry.place(x=550, y=485, width=250,height=30)

    canvas.create_text(276, 550, text="Enter The New Arrival Time", font=("Trebuchet MS", 24), fill="black")
    flightArrivalTime_entry= logo_gradiant.CustomEntry(update_flight_page, "YYYY-MM-DD HH:MM:SS", font=("Trebuchet MS", 15), fg="grey", justify=CENTER)
    flightArrivalTime_entry.place(x=550, y=535, width=250,height=30)

    canvas.create_text(300, 600, text="Enter The New Departure Time", font=("Trebuchet MS", 24), fill="black")
    flightDEPARTURETime_entry= logo_gradiant.CustomEntry(update_flight_page, "YYYY-MM-DD HH:MM:SS", font=("Trebuchet MS", 15), fg="grey", justify=CENTER)
    flightDEPARTURETime_entry.place(x=550, y=585, width=250,height=30)

    canvas.create_text(224, 650, text="Enter The New Price", font=("Trebuchet MS", 24), fill="black")
    price_updated_entry= tk.Entry(update_flight_page,font=("Trebuchet MS", 15))
    price_updated_entry.place(x=550, y=635, width=250,height=30)

    submit_button = tk.Button(update_flight_page, text="Update Flight", command=lambda:update_flight_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def update_flight_submit(event):
    if flightNUM_id_entry.get()=="" or flightArrivalTime_entry.get()=="" or flightDEPARTURETime_entry.get()=="" or price_updated_entry.get()=="":
        error_message = event.create_text(home_window.screen_width / 2, 690, text="Please fill all the fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        update_query = f"UPDATE FLIGHT SET ARRIVAL_TIME = '{flightArrivalTime_entry.get()}', DEPARTURE_TIME = '{flightDEPARTURETime_entry.get()}', PRICE='{price_updated_entry.get()}' WHERE FLIGHT_NUM = '{flightNUM_id_entry.get()}'"
        DataBase_connection.cursor.execute(update_query)
        DataBase_connection.conn.commit()
        success_message = event.create_text(home_window.screen_width / 2, 690, text="Flight Updated Successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(success_message))
        List_flight(update_flight_page, "default", "default", 30, 200)
        flightNUM_id_entry.delete(0, END)
        flightArrivalTime_entry.delete(0, END)
        flightArrivalTime_entry.insert(0, "YYYY-MM-DD HH:MM:SS")
        flightDEPARTURETime_entry.delete(0, END)
        flightDEPARTURETime_entry.insert(0, "YYYY-MM-DD HH:MM:SS")
        price_updated_entry.delete(0, END)

def delete_flight():
    admin_window.administrator_page.destroy()
    global delete_flight_page

    delete_flight_page = tk.Tk()
    delete_flight_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    delete_flight_page.resizable(False, False)

    canvas= Canvas(delete_flight_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    delete_flight_page.title("Delete Flight")

    back_btn = tk.Button(delete_flight_page, text="⬅", command= lambda: home_window.back(delete_flight_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    List_flight(delete_flight_page, "default", "default", 30, 200)

    global flight_deleted_id_entry
    canvas.create_text(200, 550, text="Enter The Flight ID", font=("Trebuchet MS", 24), fill="black")
    
    flight_deleted_id_entry = tk.Entry(delete_flight_page,font=("Trebuchet MS", 15))
    flight_deleted_id_entry.place(x=350, y=535,width=250,height=30)

    submit_button = tk.Button(delete_flight_page, text="Delete Flight", command=lambda:delete_flight_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def delete_flight_submit(event):
    if flight_deleted_id_entry.get()=="":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please enter the flight ID", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        delete_query = f"DELETE FROM FLIGHT WHERE FLIGHT_NUM ='{flight_deleted_id_entry.get()}'"
        DataBase_connection.cursor.execute(delete_query)
        DataBase_connection.conn.commit()
        if DataBase_connection.cursor.rowcount == 0:
            error_message = event.create_text(home_window.screen_width / 2, 670, text="Flight ID not found", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(error_message))
        else:
            success_message = event.create_text(home_window.screen_width / 2, 670, text="Flight Deleted Successfully", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(success_message))
            List_flight(delete_flight_page, "default", "default", 30, 200)
            flight_deleted_id_entry.delete(0, END)

def add_pilot():
    admin_window.administrator_page.destroy()
    global Pname_entry, DOB_entry,add_pilot_page

    add_pilot_page = tk.Tk()
    add_pilot_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(add_pilot_page, width= home_window.screen_width, height= home_window.screen_height)
    add_pilot_page.resizable(False, False)
    logo_gradiant.background(canvas)
    canvas.pack()
    
    back_btn = tk.Button(add_pilot_page, text="⬅", command= lambda: home_window.back(add_pilot_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)
    
    add_pilot_page.title("Add Pilot")

    canvas.create_text(home_window.screen_width  / 2, 170, text="Add a Captain", fill="black", font =("Trebuchet MS", 44, "bold"))
    canvas.create_text(home_window.screen_width / 2 - 165 , 340, text="Pilot Name", fill="black", font =("Trebuchet MS", 24))
    Pname_entry = tk.Entry(add_pilot_page, font=("Trebuchet MS", 15))
    Pname_entry.place(x=750, y=325,width=250,height=30)

    canvas.create_text(home_window.screen_width / 2 - 150, 470, text="Date of Birth", fill="black", font =("Trebuchet MS", 24))
    global DOB_entry
    DOB_entry = tk.Entry(add_pilot_page, font=("Trebuchet MS", 15))
    DOB_entry.place(x=750, y=455,width=250,height=30)
    DOB_entry.insert(0, 'YYYY-MM-DD')
    DOB_entry.bind("<Button-1>", signup_window.pick_date)

    submit_button = tk.Button(add_pilot_page, text="ADD PILOT", command=lambda:submit_pilot(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def submit_pilot(event):
    if Pname_entry.get()=="" or DOB_entry.get()=="":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please fill all the fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        dob = datetime.datetime.strptime(DOB_entry.get(), "%Y-%m-%d")
        age = signup_window.calculate_age(dob)
        insert_query = f"INSERT INTO PILOT (PNAME, DOB, AGE) VALUES ('{Pname_entry.get()}', '{DOB_entry.get()}', '{age}')"
        DataBase_connection.cursor.execute(insert_query)
        DataBase_connection.conn.commit()
        success_message = event.create_text(home_window.screen_width / 2, 670, text="Pilot Added Successfully", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(success_message))
        Pname_entry.delete(0, END)
        DOB_entry.delete(0, END)
        DOB_entry.insert(0, 'YYYY-MM-DD')

def List_pilot(page, x_axis = 0, y_axis = 0):
    for widget in page.winfo_children():
        if isinstance(widget, ttk.Treeview) and page != assign_pilotToAircraft_page:
            widget.destroy()  
    tree = ttk.Treeview(page)
    style =ttk.Style()
    tree["columns"] = ("SSN", "PNAME", "AGE", "DOB")

    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("SSN", anchor=tk.CENTER, width=165)
    tree.column("PNAME", anchor=tk.CENTER, width=165)
    tree.column("AGE", anchor=tk.CENTER, width=165)
    tree.column("DOB", anchor=tk.CENTER, width=165)

    tree.heading("#0", text="", anchor=tk.CENTER)
    tree.heading("SSN", text="SSN", anchor=tk.CENTER)
    tree.heading("PNAME", text="PNAME", anchor=tk.CENTER)
    tree.heading("AGE", text="AGE", anchor=tk.CENTER)
    tree.heading("DOB", text="DOB", anchor=tk.CENTER)
    style.configure("Treeview.Heading", foreground="black", font=("Trebuchet MS", 16, "bold"))
    style.configure("Treeview.Column", foreground="black", font=("Trebuchet MS", 6, "bold"))
    
    select_query = "SELECT * FROM PILOT"
    DataBase_connection.cursor.execute(select_query)
    rows = DataBase_connection.cursor.fetchall()
    for row in rows:
        values = [str(value) for value in row]
        tree.insert("", tk.END, values=values)

    for col in tree["columns"]:
        tree.column(col, anchor=tk.CENTER)
    tree.place(x=x_axis, y=y_axis)
    # Configure tags to color rows
    tree.tag_configure("oddrow", background="#e9f2f7")
    tree.tag_configure("evenrow", background="#91b9cf")
    tree.tag_configure("customfont", font=("Trebuchet MS",12, "normal"))

    # Apply tags to alternate rows
    for i in range(len(tree.get_children())):
        if i % 2 == 0:
            tree.item(tree.get_children()[i], tags=("customfont","evenrow"))
        else:
            tree.item(tree.get_children()[i], tags=("customfont","oddrow"))
    
    tree_height = len(tree.get_children())
    tree["height"] = tree_height
    if tree_height > 10:
        tree["height"] = 10

def assign_pilotToAircraft():
    admin_window.administrator_page.destroy()
    global assign_pilotToAircraft_page, pilot_id_entry, aircraft_id_entry

    assign_pilotToAircraft_page = tk.Tk()
    assign_pilotToAircraft_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(assign_pilotToAircraft_page, width= home_window.screen_width, height= home_window.screen_height)
    assign_pilotToAircraft_page.resizable(False, False)

    logo_gradiant.background(canvas)
    canvas.pack()
    assign_pilotToAircraft_page.title("Assign Pilot")

    back_btn = tk.Button(assign_pilotToAircraft_page, text="⬅", command= lambda: home_window.back(assign_pilotToAircraft_page, admin_window.admin_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    canvas.create_text(1100, 230, text="AIRCRAFT TABLE", fill="black", font =("Trebuchet MS", 26, "bold"))
    List_aircraft(assign_pilotToAircraft_page, home_window.screen_width / 2 - 40, 270)
    canvas.create_text(350, 230, text="PILOT TABLE", fill="black", font =("Trebuchet MS", 26, "bold"))
    List_pilot(assign_pilotToAircraft_page, 20, 270)

    canvas.create_text(177, 560, text="Enter The Pilot SSN", fill="black", font =("Trebuchet MS", 24))
    pilot_id_entry = tk.Entry(assign_pilotToAircraft_page,font=("Trebuchet MS", 15))
    pilot_id_entry.place(x=350, y=545,width=250,height=30)

    canvas.create_text(190, 640, text="Enter The Aircraft ID", fill="black", font =("Trebuchet MS", 24))
    aircraft_id_entry = tk.Entry(assign_pilotToAircraft_page,font=("Trebuchet MS", 15))
    aircraft_id_entry.place(x=350, y=625,width=250,height=30)

    submit_button = tk.Button(assign_pilotToAircraft_page, text="ASSIGN PILOT", command=lambda:assign_pilotToAircraft_submit(canvas), font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    submit_button.place(x=643, y=710, width=200, height=50)

def assign_pilotToAircraft_submit(event):
    if pilot_id_entry.get() == "" or aircraft_id_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 685, text="Please Fill All The Fields", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, lambda: event.delete(error_message))
    else:
        select_query = f"SELECT * FROM FLYING WHERE SSN = '{pilot_id_entry.get()}' AND SERIAL_NUM = '{aircraft_id_entry.get()}'"
        DataBase_connection.cursor.execute(select_query)
        rows = DataBase_connection.cursor.fetchall()
        print(rows)
        if len(rows) != 0:
            error_message = event.create_text(home_window.screen_width / 2, 685, text="Pilot Already Assigned To This Aircraft", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(error_message))
        else:
            insert_query = f"INSERT INTO FLYING (SSN, SERIAL_NUM) VALUES ('{pilot_id_entry.get()}', '{aircraft_id_entry.get()}')"
            DataBase_connection.cursor.execute(insert_query)
            DataBase_connection.conn.commit()
            success_message = event.create_text(home_window.screen_width / 2, 685, text="Pilot Assigned Successfully", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(success_message))
            List_aircraft(assign_pilotToAircraft_page, home_window.screen_width / 2 - 40, 270)
            List_pilot(assign_pilotToAircraft_page, 20, 270)
            pilot_id_entry.delete(0, END)
            aircraft_id_entry.delete(0, END)
