from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk
import DataBase_connection
import home_window
import signin_window
import customer_window
import admin_functionality
import logo_gradiant

def book_flight():
    customer_window.user_page.destroy()
    global source_entry, destination_entry, book_flight_page

    book_flight_page = tk.Tk()
    book_flight_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")
    global canvas
    canvas= Canvas(book_flight_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(book_flight_page, text="⬅", command= lambda: home_window.back(book_flight_page, customer_window.customer_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    book_flight_page.title("Book Flight")
    #input source
    canvas.create_text(100, 200, text="Source", fill="black", font =("Trebuchet MS", 24))
    source_entry = tk.Entry(book_flight_page,font=("Trebuchet MS", 15))
    source_entry.place(x=170, y=190,width=250,height=30)
    #input destination
    canvas.create_text(600, 200, text="Destination", fill="black", font =("Trebuchet MS", 24))
    destination_entry = tk.Entry(book_flight_page,font=("Trebuchet MS", 15))
    destination_entry.place(x=700, y=190,width=250,height=30)
    #submit
    submit_button = tk.Button(book_flight_page, text="Search", command=book_flight_submit, font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=1200, y=180, height=50, width=250)
    admin_functionality.List_flight(book_flight_page, "default", "default", 40, 270)
    global flight_number_entry, selected_class_booking
    canvas.create_text(155, 550, text="Flight Number", fill="black", font =("Trebuchet MS", 24))
    flight_number_entry = tk.Entry(book_flight_page,font=("Trebuchet MS", 15))
    flight_number_entry.place(x=300, y=535,width=250,height=30)
    canvas.create_text(145, 605, text="Select Class:", fill="black", font =("Trebuchet MS", 24))
    selected_class_booking = 1
    global radiobtn_photo1, radiobtn_photo2, radiobtn1, radiobtn2, radiobtn3
    radiobtn_photo1 = PhotoImage(file="F:\database_project\code\\Radio Button 1 mt7dd.png") # write the full path of the image in your computer
    radiobtn1 = tk.Button(book_flight_page, image=radiobtn_photo1, command=lambda: select_role(1), bd=0)
    radiobtn1.place(x=312, y=605, anchor=CENTER, height=20, width=20)
    canvas.create_text(380, 605, text="First Class", fill="black", font =("Trebuchet MS", 16))
    radiobtn_photo2 = PhotoImage(file="F:\database_project\code\\Radio Button 1 fady.png")
    radiobtn2 = tk.Button(book_flight_page, image=radiobtn_photo2, command=lambda: select_role(2), bd=0)
    radiobtn2.place(x=312, y=645, anchor=CENTER, height=20, width=20)
    canvas.create_text(398, 645, text="Business Class", fill="black", font =("Trebuchet MS", 16))
    radiobtn3 = tk.Button(book_flight_page, image=radiobtn_photo2, command=lambda: select_role(3), bd=0)
    radiobtn3.place(x=312, y=685, anchor=CENTER, height=20, width=20)
    canvas.create_text(400, 685, text="Economy Class", fill="black", font =("Trebuchet MS", 16))

    submit_button = tk.Button(book_flight_page, text="Book Ticket", command=lambda:add_flight_to_customer(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def book_flight_submit():
    if source_entry.get() == "" or destination_entry.get() == "":
        admin_functionality.List_flight(book_flight_page, "default", "default", 40, 270)
    else:
        admin_functionality.List_flight(book_flight_page, source_entry.get(), destination_entry.get(), 40, 270)
        source_entry.delete(0,END)
        destination_entry.delete(0,END)


def select_role(role):
    global selected_class_booking
    selected_class_booking = role
    if role == 1:
        radiobtn1.config(image=radiobtn_photo1)
        radiobtn2.config(image=radiobtn_photo2)
        radiobtn3.config(image=radiobtn_photo2)
    elif role == 2:
        radiobtn1.config(image=radiobtn_photo2)
        radiobtn2.config(image=radiobtn_photo1)
        radiobtn3.config(image=radiobtn_photo2)
    else:
        radiobtn1.config(image=radiobtn_photo2)
        radiobtn2.config(image=radiobtn_photo2)
        radiobtn3.config(image=radiobtn_photo1)

def add_flight_to_customer(event):
    if flight_number_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 685, text="Please fill all the required fields.", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, event.delete, error_message)
    else:
        select_flight = f"SELECT FLIGHT_NUM, ARRIVAL_TIME, DEPARTURE_TIME, SOURCE_LOCATION, DESTINATION_LOCATION, PRICE FROM FLIGHT WHERE FLIGHT_NUM = '{flight_number_entry.get()}'"
        DataBase_connection.cursor.execute(select_flight)
        result_flight = DataBase_connection.cursor.fetchone()
        
        select_person = f"SELECT ID, FNAME, LNAME FROM PERSON WHERE EMAIL = '{signin_window.email}'"
        DataBase_connection.cursor.execute(select_person)
        result_person = DataBase_connection.cursor.fetchone()
        if selected_class_booking == 1:
            set_class = "First Class"
            price = result_flight[5] * 1.5
        elif selected_class_booking == 2:
            set_class = "Business Class"
            price = result_flight[5] * 1.25
        else:
            set_class = "Economy Class"
            price = result_flight[5]
        ###########    JOIN    ##########
        check_unique = f"SELECT TICKET.ID, TICKET.FLIGHT_NUM FROM TICKET, PERSON WHERE TICKET.ID = PERSON.ID AND PERSON.EMAIL = '{signin_window.email}' AND TICKET.FLIGHT_NUM = '{flight_number_entry.get()}'"
        DataBase_connection.cursor.execute(check_unique)
        result_check_uninqe = DataBase_connection.cursor.fetchone()
        if result_check_uninqe != None:
            global remove_text
            remove_text = canvas.create_text(home_window.screen_width / 2, 685, text="You can not book a flight twice", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, canvas.delete, remove_text)
        else:
            insert_query = f"INSERT INTO TICKET (FLIGHT_NUM, ID, PRICE, PNAME, SOURCE_LOCATION, DESTINATION_LOCATION, SEAT, CLASS, ARRIVAL_TIME, DEPARTURE_TIME) VALUES ('{result_flight[0]}', '{result_person[0]}', '{price}', '{result_person[1] + ' ' + result_person[2]}', '{result_flight[3]}', '{result_flight[4]}', '1', '{set_class}', '{result_flight[1]}', '{result_flight[2]}')"
            DataBase_connection.cursor.execute(insert_query)
            DataBase_connection.conn.commit()
            DataBase_connection.cursor.execute(f"INSERT INTO PASSENGER (FLIGHT_NUM, P_ID, FNAME, LNAME) VALUES ('{result_flight[0]}', '{result_person[0]}', '{result_person[1]}', '{result_person[2]}')")
            DataBase_connection.conn.commit()
            flight_number_entry.delete(0,END)
            Message = event.create_text(home_window.screen_width / 2, 685, text="Flight booked successfully.", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, event.delete, Message)

def booked_tickets_list(page):
    for widget in page.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()  
    style =ttk.Style()
    tree = ttk.Treeview(page)
    tree["columns"] = ("Ticket ID", "Flight Number", "User ID", "User Name", "Source", "Destination", "Price", "Seat", "Class", "Arrival Time", "Departure Time")
    tree.column("#0", width=0, stretch=NO)
    tree.column("Ticket ID", anchor=CENTER, width=115)
    tree.column("Flight Number", anchor=CENTER, width=150)
    tree.column("User ID", anchor=CENTER, width=125)
    tree.column("User Name", anchor=CENTER, width=139)
    tree.column("Source", anchor=CENTER, width=139)
    tree.column("Destination", anchor=CENTER, width=139)
    tree.column("Price", anchor=CENTER, width=110)
    tree.column("Seat", anchor=CENTER, width=110)
    tree.column("Class", anchor=CENTER, width=139)
    tree.column("Arrival Time", anchor=CENTER, width=150)
    tree.column("Departure Time", anchor=CENTER, width=170)

    tree.heading("Ticket ID", text="Ticket ID", anchor=CENTER)
    tree.heading("Flight Number", text="Flight Number", anchor=CENTER)
    tree.heading("User ID", text="User ID", anchor=CENTER)
    tree.heading("User Name", text="User Name", anchor=CENTER)
    tree.heading("Source", text="Source", anchor=CENTER)
    tree.heading("Destination", text="Destination", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("Seat", text="Seat", anchor=CENTER)
    tree.heading("Class", text="Class", anchor=CENTER)
    tree.heading("Arrival Time", text="Arrival Time", anchor=CENTER)
    tree.heading("Departure Time", text="Departure Time", anchor=CENTER)
    style.configure("Treeview.Heading", foreground="black", font=("Trebuchet MS", 16, "bold"))
    style.configure("Treeview.Column", foreground="black", font=("Trebuchet MS", 6, "bold"))

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
    tree.place(x=17, y=200)
    #Configure tags to color rows
    tree.tag_configure("oddrow", background="#e9f2f7")
    tree.tag_configure("evenrow", background="#91b9cf")
    tree.tag_configure("customfont", font=("Trebuchet MS",12, "normal"))

    #Apply tags to alternate rows
    for i in range(len(tree.get_children())):
        if i % 2 == 0:
            tree.item(tree.get_children()[i], tags=("customfont","evenrow"))
        else:
            tree.item(tree.get_children()[i], tags=("customfont","oddrow"))
    
    tree_height = len(tree.get_children())
    tree["height"] = tree_height
    if tree_height > 10:
        tree["height"] = 10

def cancel_flight():
    customer_window.user_page.destroy()
    global cancel_flight_page ,cancel_flight_entry

    cancel_flight_page = tk.Tk()
    cancel_flight_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(cancel_flight_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(cancel_flight_page, text="⬅", command= lambda: home_window.back(cancel_flight_page, customer_window.customer_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    booked_tickets_list(cancel_flight_page)
    canvas.create_text(155, 550, text="Enter the ticket id:", font=("Trebuchet MS", 24), fill="black")
    cancel_flight_entry= tk.Entry(cancel_flight_page,font=("Trebuchet MS", 15))
    cancel_flight_entry.place(x=300, y=535,width=250,height=30)

    submit_button = tk.Button(cancel_flight_page, text="Cancel", command=lambda:cancel_flight_submit(canvas),font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def cancel_flight_submit(event):
    if cancel_flight_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please enter the ticket id", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, event.delete, error_message)
    else:
        select_query = f"SELECT TICKETID FROM TICKET WHERE TICKETID = '{cancel_flight_entry.get()}'"
        DataBase_connection.cursor.execute(select_query)
        result = DataBase_connection.cursor.fetchone()
        if result == None:
            error_message = event.create_text(home_window.screen_width / 2, 670, text="Ticket id is not found", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, event.delete, error_message)
        else:
            DataBase_connection.cursor.execute(f"DELETE FROM TICKET WHERE TICKETID ='{cancel_flight_entry.get()}'")
            DataBase_connection.conn.commit()
            cancel_flight_entry.delete(0,END)
            message = event.create_text(home_window.screen_width / 2, 670, text="Ticket cancelled", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(message))
            booked_tickets_list(cancel_flight_page)

def change_class():
    customer_window.user_page.destroy()
    global change_class_page, change_class_ticket_number_entry, selected_class

    change_class_page = tk.Tk()
    change_class_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(change_class_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(change_class_page, text="⬅", command= lambda: home_window.back(change_class_page, customer_window.customer_page), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    change_class_page.title("Change Class Page")
    booked_tickets_list(change_class_page)

    canvas.create_text(155, 550, text="Ticket Number", fill="black", font =("Trebuchet MS", 24))
    change_class_ticket_number_entry = tk.Entry(change_class_page,font=("Trebuchet MS", 15))
    change_class_ticket_number_entry.place(x=300, y=535,width=250,height=30)

    canvas.create_text(145, 605, text="Select Class:", fill="black", font =("Trebuchet MS", 24))

    selected_class = 1
    global radiobtn1_changed,radiobtn2_changed,radiobtn3_changed
    global radiobtn_photo1_changed, radiobtn_photo2_changed
    radiobtn_photo1_changed = PhotoImage(file="F:\database_project\code\\Radio Button 1 mt7dd.png")
    radiobtn1_changed = tk.Button(change_class_page, image=radiobtn_photo1_changed, command=lambda: select_changed_role(1), bd=0)
    radiobtn1_changed.place(x=312, y=605, anchor=CENTER, height=20, width=20)
    canvas.create_text(380, 605, text="First Class", fill="black", font =("Trebuchet MS", 16))
    radiobtn_photo2_changed = PhotoImage(file="F:\database_project\code\\Radio Button 1 fady.png")
    radiobtn2_changed = tk.Button(change_class_page, image=radiobtn_photo2_changed, command=lambda: select_changed_role(2), bd=0)
    radiobtn2_changed.place(x=312, y=645, anchor=CENTER, height=20, width=20)
    canvas.create_text(398, 645, text="Business Class", fill="black", font =("Trebuchet MS", 16))
    radiobtn3_changed = tk.Button(change_class_page, image=radiobtn_photo2_changed, command=lambda: select_changed_role(3), bd=0)
    radiobtn3_changed.place(x=312, y=685, anchor=CENTER, height=20, width=20)
    canvas.create_text(400, 685, text="Economy Class", fill="black", font =("Trebuchet MS", 16))

    submit_button = tk.Button(change_class_page, text="SWITCH CLASS", command=lambda:change_class_submit(canvas), font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    submit_button.place(x=643, y=710, height=50, width=250)

def select_changed_role(role):
    global selected_class
    selected_class = role
    if role == 1:
        radiobtn1_changed.config(image=radiobtn_photo1_changed)
        radiobtn2_changed.config(image=radiobtn_photo2_changed)
        radiobtn3_changed.config(image=radiobtn_photo2_changed)
    elif role == 2:
        radiobtn1_changed.config(image=radiobtn_photo2_changed)
        radiobtn2_changed.config(image=radiobtn_photo1_changed)
        radiobtn3_changed.config(image=radiobtn_photo2_changed)
    else:
        radiobtn1_changed.config(image=radiobtn_photo2_changed)
        radiobtn2_changed.config(image=radiobtn_photo2_changed)
        radiobtn3_changed.config(image=radiobtn_photo1_changed)
    
def change_class_submit(event):
    if change_class_ticket_number_entry.get() == "":
        error_message = event.create_text(home_window.screen_width / 2, 670, text="Please enter ticket number", fill="black", font =("Trebuchet MS", 24))
        event.after(5000, event.delete, error_message)
    else:
        DataBase_connection.cursor.execute(f"SELECT FLIGHT_NUM from TICKET where TICKETID = '{change_class_ticket_number_entry.get()}'")
        flight_num = DataBase_connection.cursor.fetchone()
        if flight_num == None:
            error_message = event.create_text(home_window.screen_width / 2, 670, text="Ticket number doesn't exist", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, event.delete, error_message)
        else:
            DataBase_connection.cursor.execute(f"SELECT PRICE from FLIGHT where FLIGHT_NUM = '{flight_num[0]}'")
            flight_price = DataBase_connection.cursor.fetchone()
            if selected_class==1:
                changed_value="First Class"
                changed_price = flight_price[0] * 1.5
            elif selected_class==2:
                changed_value="Business Class"
                changed_price = flight_price[0] * 1.25
            else:
                changed_value="Economy Class"
                changed_price = flight_price[0]
            DataBase_connection.cursor.execute(f"update TICKET set CLASS= '{changed_value}', PRICE= '{changed_price}' where TICKETID = '{change_class_ticket_number_entry.get()}'")
            DataBase_connection.conn.commit()
            message = event.create_text(home_window.screen_width/2, 670, text="class changed successfully", fill="black", font =("Trebuchet MS", 24))
            event.after(5000, lambda: event.delete(message))
            booked_tickets_list(change_class_page)