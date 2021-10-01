# How we can make clock using python?

# Make a Clock using Python | Python Project 1

# How to make a clock using python. This is a simple python project. 

# Import necessary libraries.

from tkinter import *

from tkinter.ttk import *

from time import strftime


# Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI. Tkinter is included with standard GNU/Linux, Microsoft Windows and macOS installs of Python. The name Tkinter comes from Tk interface.

# Let's create a UI for our clock.

root = Tk()
root.title("Clock")

# Define a function to get our time.

def time():
    #string = strftime('%H:%M:%S %p') for 24 hour format
    string = strftime('%I:%M:%S %p') # for 12 hour format

    # %I =  Hour (12-hour clock) as a zero-padded decimal number.

    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital, 80"), background="black", foreground = "cyan")

label.pack(anchor='center')

time()  

mainloop()
# 

# Made By :- Vishwanath Pratap Singh Rathor.