from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
from tkinter import ttk
import DataBase_connection
import home_window
import signin_window
import customer_window
import admin_functionality

def book_flight():
    customer_window.customer_page.destroy()
    global source_entry, destination_entry
    global book_flight_page
    book_flight_page = tk.Tk()
    x = int(home_window.screen_width/2 - 800/2)
    y = int(home_window.screen_height/2 - 600/2)
    book_flight_page.geometry(f"900x500+{x}+{y}")
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
    admin_functionality.List_flight(book_flight_page, source_entry.get(), destination_entry.get())
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
    select_flight = f"SELECT FLIGHT_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, PRICE FROM FLIGHT WHERE FLIGHT_NUM = '{flight_number_entry.get()}'"
    DataBase_connection.cursor.execute(select_flight)
    result_flight = DataBase_connection.cursor.fetchone()
    print(result_flight)
    
    print(signin_window.email)
    select_person = f"SELECT ID, FNAME, LNAME FROM PERSON WHERE EMAIL = '{signin_window.email}'"
    DataBase_connection.cursor.execute(select_person)
    result_person = DataBase_connection.cursor.fetchone()
    print(selected_class_booking.get())
    if selected_class_booking.get() == 1:
        set_class = "First Class"
        price = result_flight[5] * 1.5
    elif selected_class_booking.get() == 2:
        set_class = "Business Class"
        price = result_flight[5] * 1.25
    else:
        set_class = "Economy Class"
        price = result_flight[5]
    print(price)
    insert_query = f"INSERT INTO TICKET (FLIGHT_NUM, ID, PRICE, PNAME, SOURCE_LOCATION, DESTINATION_LOCATION, SEAT, CLASS, ARRIVAL_TIME, DEPARTURE_TIME) VALUES ('{result_flight[0]}', '{result_person[0]}', '{price}', '{result_person[1]}', '{result_flight[3]}', '{result_flight[4]}', '1', '{set_class}', '{result_flight[1]}', '{result_flight[2]}')"
    DataBase_connection.cursor.execute(insert_query)
    DataBase_connection.conn.commit()
    DataBase_connection.cursor.execute(f"INSERT INTO PASSENGER (FLIGHT_NUM, P_ID, FNAME, LNAME) VALUES ('{result_flight[0]}', '{result_person[0]}', '{result_person[1]}', '{result_person[2]}')")
    DataBase_connection.conn.commit()

    

def booked_tickets_list(page):
    tree = ttk.Treeview(page)
    tree["columns"] = ("Ticket ID", "Flight Number", "Customer ID", "Customer Name", "Source Location", "Destination Location", "Price", "Seat", "Class", "Arrival Time", "Departure Time")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Ticket ID", anchor=CENTER, width=100)
    tree.column("Flight Number", anchor=CENTER, width=100)
    tree.column("Customer ID", anchor=CENTER, width=100)
    tree.column("Customer Name", anchor=CENTER, width=100)
    tree.column("Source Location", anchor=CENTER, width=100)
    tree.column("Destination Location", anchor=CENTER, width=100)
    tree.column("Price", anchor=CENTER, width=100)
    tree.column("Seat", anchor=CENTER, width=100)
    tree.column("Class", anchor=CENTER, width=100)
    tree.column("Arrival Time", anchor=CENTER, width=100)
    tree.column("Departure Time", anchor=CENTER, width=100)

    tree.heading("Ticket ID", text="Ticket ID", anchor=CENTER)
    tree.heading("Flight Number", text="Flight Number", anchor=CENTER)
    tree.heading("Customer ID", text="Customer ID", anchor=CENTER)
    tree.heading("Customer Name", text="Customer Name", anchor=CENTER)
    tree.heading("Source Location", text="Source Location", anchor=CENTER)
    tree.heading("Destination Location", text="Destination Location", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("Seat", text="Seat", anchor=CENTER)
    tree.heading("Class", text="Class", anchor=CENTER)
    tree.heading("Arrival Time", text="Arrival Time", anchor=CENTER)
    tree.heading("Departure Time", text="Departure Time", anchor=CENTER)

    select_ID = f"SELECT ID FROM PERSON WHERE EMAIL = '{signin_window.email}'"
    DataBase_connection.cursor.execute(select_ID)
    result_ID = DataBase_connection.cursor.fetchone()
    select_query = f"SELECT TICKETID, FLIGHT_NUM, ID, PNAME, SOURCE_LOCATION, DESTINATION_LOCATION, PRICE, SEAT, CLASS, ARRIVAL_TIME, DEPARTURE_TIME FROM TICKET WHERE ID = '{result_ID[0]}'"
    DataBase_connection.cursor.execute(select_query)
    result = DataBase_connection.cursor.fetchall()
    for row in result:
        values = [str(value) for value in row]
        tree.insert("", END, values=values)
    for col in tree["columns"]:
        tree.heading(col, text=col, anchor=CENTER)
    tree.place(x=0, y=0)

def cancel_flight():
    customer_window.customer_page.destroy()
    global cancel_flight_page ,cancel_flight_entry
    cancel_flight_page =tk.Tk()
    x = int(home_window.screen_width/2 - 800/2)
    y = int(home_window.screen_height/2 - 600/2)
    cancel_flight_page.geometry(f"900x500+{x}+{y}")
    booked_tickets_list(cancel_flight_page)
    cancel_flight_label = tk.Label(cancel_flight_page, text="Enter the ticket id: ")
    cancel_flight_label.place(x=10,y=250)
    cancel_flight_entry= tk.Entry(cancel_flight_page)
    cancel_flight_entry.place(x=200,y=250)
    submit_button = tk.Button(cancel_flight_page, text="Submit", width=10, height=2, command= cancel_flight_submit)
    submit_button.place(x=210, y=400)

def cancel_flight_submit():
    DataBase_connection.cursor.execute(f"DELETE FROM TICKET WHERE TICKETID ='{cancel_flight_entry.get()}'")
    DataBase_connection.conn.commit()
    done = Label(cancel_flight_page, text = "Ticket cancelled successfully")
    done.place(x=190, y=330)
    booked_tickets_list(cancel_flight_page)

def change_class():
    customer_window.customer_page.destroy()
    global change_class_page,change_class_ticket_number_entry,selected_class
    change_class_page = tk.Tk()
    x = int(home_window.screen_width/2 - 800/2)
    y = int(home_window.screen_height/2 - 600/2)
    change_class_page.geometry(f"900x500+{x}+{y}")
    change_class_page.title("Change Class Page")
    booked_tickets_list(change_class_page)

    change_class_ticket_number_label = tk.Label(change_class_page, text="Ticket Number")
    change_class_ticket_number_label.place(x=10, y=310)
    change_class_ticket_number_entry = tk.Entry(change_class_page)
    change_class_ticket_number_entry.place(x=100, y=310)

    selected_class = tk.IntVar(value=1)
    change_class_label =  tk.Label(change_class_page, text="Select Class : ")
    change_class_label.place(x=130, y=340)

    change_class_option1 = Radiobutton(change_class_page, text="First Class", value=1, variable=selected_class)
    change_class_option1.place(x=200, y=340)

    change_class_option2 = Radiobutton(change_class_page, text="Business Class", value=2, variable=selected_class)
    change_class_option2.place(x=200, y=370) 

    change_class_option3 = Radiobutton(change_class_page, text="Economy Class", value=3, variable=selected_class)
    change_class_option3.place(x=200, y=400) 

    #submit
    submit_button = tk.Button(change_class_page, text="Submit", width=10, height=2, command=change_class_submit)
    submit_button.place(x=210, y=450)
    
def change_class_submit():
    DataBase_connection.cursor.execute(f"SELECT FLIGHT_NUM from TICKET where TICKETID = '{change_class_ticket_number_entry.get()}'")
    flight_num = DataBase_connection.cursor.fetchone()
    DataBase_connection.cursor.execute(f"SELECT PRICE from FLIGHT where FLIGHT_NUM = '{flight_num[0]}'")
    flight_price = DataBase_connection.cursor.fetchone()
    if selected_class.get()==1:
        changed_value="First Class"
        changed_price = flight_price[0] * 1.5
    elif selected_class.get()==2:
        changed_value="Business Class"
        changed_price = flight_price[0] * 1.25
    else:
        changed_value="Economy Class"
        changed_price = flight_price[0]

    DataBase_connection.cursor.execute(f"update TICKET set CLASS= '{changed_value}', PRICE= '{changed_price}' where TICKETID = '{change_class_ticket_number_entry.get()}'")
    DataBase_connection.conn.commit()

    done = Label(change_class_page, text = "class changed successfully")
    done.place(x=210, y=470)
    booked_tickets_list(change_class_page)