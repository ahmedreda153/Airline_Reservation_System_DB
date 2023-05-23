from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import home_window
import signin_window
import customer_functionality
import update_userInfo_window
import logo_gradiant

isCustomer = False

def customer_page():
    global isCustomer
    isCustomer = True
    if signin_window.isOpen==True:
        signin_window.sign_in_page.destroy()
        signin_window.isOpen=False
        
    global user_page
    user_page = tk.Tk()
    user_page.geometry(f"{home_window.screen_width}x{home_window.screen_height}")

    canvas= Canvas(user_page, width= home_window.screen_width, height= home_window.screen_height)
    logo_gradiant.background(canvas)
    canvas.pack()

    back_btn = tk.Button(user_page, text="⬅", command= lambda: home_window.back(user_page, home_window.home), font=(50), bd=0, bg="white", fg="black")
    back_btn.place(x=15, y=15, anchor=CENTER, height=30, width=30)

    user_page.title("Customer Page")

    book_button = tk.Button(user_page, text="Reserve Your Flight", command=customer_functionality.book_flight ,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    book_button.place(x=130, y=220, width=500, height=100)

    
    cancel_button = tk.Button(user_page, text="Cancel Reservation", command=customer_functionality.cancel_flight,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=0)
    cancel_button.place(x=130, y=370, width=500, height=100)
    
    class_button = tk.Button(user_page, text="Switch Cabin Class", command=customer_functionality.change_class,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=1)
    class_button.place(x=130, y=520, width=500, height=100)
    
    update_info_button = tk.Button(user_page, text="Modify Personal Information", command=update_userInfo_window.update_info,font =("Trebuchet MS", 24), bg="#DDDBEF", bd=0)
    update_info_button.place(x=130, y=670, width=500, height=100)

    side_image = Image.open("F:/database_project/code/21211.png")
    # Reduce the size of the image
    side_image_width, side_image_height = side_image.size
    side_new_width = side_image_width // 3  # Specify the new width
    side_new_height = side_image_height // 3  # Specify the new height
    side_resized_image = side_image.resize((side_new_width, side_new_height), Image.ANTIALIAS)

    # Convert the resized image to PhotoImage
    side_photo_image = ImageTk.PhotoImage(side_resized_image)

    # Set the image on the canvas
    canvas.create_image(690, 150, anchor=tk.NW, image=side_photo_image)
    canvas.side_photo_image = side_photo_image