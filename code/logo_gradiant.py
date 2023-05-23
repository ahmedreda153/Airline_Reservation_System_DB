from tkinter import *
from tkcalendar import *
import tkinter as tk
from PIL import ImageTk, Image
import home_window

def create_gradient(canvas):
    color1 = (255, 255, 255) 
    color2 = (0, 146, 197)
    for y in range(home_window.screen_height):
        # Calculate the RGB values for each row
        r = int(color1[0] + (color2[0] - color1[0]) * y / home_window.screen_height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / home_window.screen_height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / home_window.screen_height)
        color = "#%02x%02x%02x" % (r, g, b)
        canvas.create_rectangle(0, y, home_window.screen_width, y+1, fill=color, outline="")

def create_logo(canvas):
    original_image = Image.open("F:\database_project\code\\travel_agency_logo_concept300.png")
    width, height = original_image.size
    new_width = width // 10  
    new_height = height // 10 
    resized_image = original_image.resize((new_width, new_height), Image.ANTIALIAS)
    photo_image = ImageTk.PhotoImage(resized_image)
    #Set the image on the canvas
    canvas.create_image(20, 20, anchor=tk.NW, image=photo_image)
    canvas.photo_image = photo_image
    
def background(canvas):
    create_gradient(canvas)
    create_logo(canvas)

def handle_entry_focus_in(event):
    entry = event.widget
    if entry.get() == entry.placeholder_text:
        entry.delete(0, 'end')
    entry.config(fg="black")

def handle_entry_focus_out(event):
    entry = event.widget
    if entry.get() == "":
        entry.insert(0, entry.placeholder_text)
        entry.config(fg="grey")

class CustomEntry(tk.Entry):
    def __init__(self, parent, placeholder_text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.placeholder_text = placeholder_text
        self.config(fg="grey")
        self.insert(0, self.placeholder_text)
        self.bind("<FocusIn>", handle_entry_focus_in)
        self.bind("<FocusOut>", handle_entry_focus_out)
