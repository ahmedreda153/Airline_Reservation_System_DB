from tkinter import *
from tkcalendar import *
import tkinter as tk
import tkinter as tk
import signup_window
import signin_window

global home_page, screen_width, screen_height, x, y

# def home():
#     def open_signup():
#         import signup_window
#         signup_window.sign_up()
#     global home_page, screen_width, screen_height, x, y
#     home_page = tk.Tk()
#     home_page.resizable(False, False)
#     screen_width = home_page.winfo_screenwidth()
#     screen_height = home_page.winfo_screenheight()
#     x = int((screen_width / 2) - (500 / 2))
#     y = int((screen_height / 2) - (600 / 2))
#     home_page.geometry(f"500x500+{x}+{y}")
#     home_page.title("Airline Reservation System")
#     # Create label
#     page_title = Label(home_page, text = "Airline Reservation System")
#     page_title.config(font =("Courier", 14))
#     page_title.pack(pady=50)

#     signUp = tk.Button(home_page, text="Sign Up", command=open_signup, width=10, height=2)
#     signUp.place(x=140, y=240)
#     signIn = tk.Button(home_page, text="Sign In", command=signin_window.sign_in, width=10, height=2)
#     signIn.place(x=290, y=240)

def home():
    def open_signup():
        import signup_window
        signup_window.sign_up()
    global home_page, screen_width, screen_height, x, y
    home_page = tk.Tk()
    screen_width = home_page.winfo_screenwidth()
    screen_height = home_page.winfo_screenheight()
    x = int((screen_width / 2) - (500 / 2))
    y = int((screen_height / 2) - (600 / 2))
    home_page.geometry(f"500x500+{x}+{y}")
    # home_page.geometry(f"{screen_width}x{screen_height}")
    home_page.title("Airline Reservation System")
    # Create label
    page_title = Label(home_page, text = "Airline Reservation System")
    page_title.config(font =("Comic Sans MS", 22, "bold"))
    page_title.pack(pady=50)

    middle_words1 = Label(home_page, text = "Search less,\nTravel more!")
    middle_words1.config(font =("Comic Sans MS", 18))
    middle_words1.pack(pady=15)

    signUp = tk.Button(home_page, text="CREATE AN ACCOUNT", command=open_signup, font=("Comic Sans MS", 12, "bold"), foreground="white", background="black")
    # signUp.place(x=130, y=290)
    signUp.place(relx=0.5, rely=0.62, anchor=CENTER, height=50, width=250)
    signIn = tk.Button(home_page, text="LOG IN", command=signin_window.sign_in, font=("Comic Sans MS", 12, "bold") , foreground="white", background="black")
    # signIn.place(x=130, y=350)
    signIn.place(relx=0.5, rely=0.75, anchor=CENTER, height=50, width=250)