# Importing tkinter module for GUI
from tkinter import *

# Importing random module for generating passwords
import random

# Creating a window object
window = Tk()

# Setting the title and size of the window
window.title("Password Generator")
window.geometry("400x500")

# Creating a label widget for the title
label = Label(window, text="Password Generator", font=("Arial", 20))
label.pack(pady=10)

# Creating a text entry widget for entering the user name
user_entry = Entry(window, width=30, borderwidth=5)
user_entry.pack(pady=10)

# Creating a label widget for the user name
user_label = Label(window, text="Enter your user name")
user_label.pack(pady=10)

# Creating a text entry widget for entering the length of the password
length_entry = Entry(window, width=30, borderwidth=5)
length_entry.pack(pady=10)

# Creating a label widget for the length of the password
length_label = Label(window, text="Enter the length of the password (4-16)")
length_label.pack(pady=10)

# Creating a text entry widget for displaying the password
password_entry = Entry(window, width=30, borderwidth=5)
password_entry.pack(pady=10)

# Creating a label widget for the password
password_label = Label(window, text="Your password")
password_label.pack(pady=10)

# Creating a list of characters for the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Defining the functions for the buttons

# Function to generate and display a random password of given length
def button_generate():
    try:
        length = int(length_entry.get())
        if 4 <= length <= 16:
            password = ""
            for i in range(length):
                password += random.choice(characters)
            password_entry.delete(0, END)
            password_entry.insert(0, password)
        else:
            password_entry.delete(0, END)
            password_entry.insert(0, "Invalid length")
    except:
        password_entry.delete(0, END)
        password_entry.insert(0, "Invalid length")

# Function to accept the user name and password and display a message
def button_accept():
    user_name = user_entry.get()
    password = password_entry.get()
    if user_name and password and 4 <= len(password) <= 16:
        message = f"Your user name is {user_name} and your password is {password}"
    else:
        message = "Please enter a user name and generate a valid password"
    message_label.config(text=message)

# Function to clear the user name and password entries
def button_reset():
    user_entry.delete(0, END)
    length_entry.delete(0, END)
    password_entry.delete(0, END)
    message_label.config(text="")

# Creating the buttons for the generator
generate_button = Button(window, text="Generate Password", padx=40, pady=20, command=button_generate)
generate_button.pack(pady=10)

# Creating the button for accepting the user name and password
accept_button = Button(window, text="Accept", padx=40, pady=20, command=button_accept)
accept_button.pack(pady=10)

# Creating the button for resetting the entries
reset_button = Button(window, text="Reset", padx=40, pady=20, command=button_reset)
reset_button.pack(pady=10)

# Creating a label widget for displaying the message
message_label = Label(window, text="")
message_label.pack(pady=10)

# Starting the main loop of the window
window.mainloop()
