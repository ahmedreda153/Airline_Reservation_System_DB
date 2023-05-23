from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import signup_window
import signin_window
import logo_gradiant
import customer_window
import generate_report

global home_page, screen_width, screen_height, x, y

def back(page1, fun_page):
    page1.destroy()
    fun_page()

home_isOpened = False

def home():
    generate_report.generate_pdf_report()
    def open_signup():
        import signup_window
        signup_window.sign_up()
    global home_page, screen_width, screen_height, x, y

    customer_window.isCustomer = False
    global home_isOpened
    home_isOpened = True
    home_page = tk.Tk()
    screen_width = home_page.winfo_screenwidth() #1536
    screen_height = home_page.winfo_screenheight() #864
    home_page.geometry(f"{screen_width}x{screen_height}")
    home_page.title("Airline Reservation System")

    canvas= Canvas(home_page, width= screen_width, height= screen_height)
    home_page.resizable(False, False)
    logo_gradiant.background(canvas)

    canvas.create_text(screen_width / 2, 250, text="Airline Reservation System", fill="black", font =("Trebuchet MS", 44, "bold"))
    #Add a text in Canvas
    canvas.create_text(screen_width / 2 + 20, 350, text="Search less,Travel more ✈️", fill="black", font =("Trebuchet MS", 29, "bold"))
    canvas.pack()

    signUp = tk.Button(home_page, text="CREATE AN ACCOUNT", command=open_signup, font=("Trebuchet MS", 12, "bold"), foreground="white", background="black")
    signUp.place(relx=0.4, rely=0.65, anchor=CENTER, height=50, width=250)
    signIn = tk.Button(home_page, text="LOG IN", command=signin_window.sign_in, font=("Trebuchet MS", 12, "bold") , foreground="white", background="black")
    signIn.place(relx=0.6, rely=0.65, anchor=CENTER, height=50, width=250)

    home_page.mainloop()