from tkinter import Tk, Button, Entry
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert('end', str(current) + str(number))

def button_clear():
    entry.delete(0, 'end')

def button_equal():
    result = eval(entry.get())
    entry.delete(0, 'end')
    entry.insert('end', result)

def button_sqrt():
    number = float(entry.get())
    result = math.sqrt(number)
    entry.delete(0, 'end')
    entry.insert('end', result)

def create_button(text, row, column, command=None):
    button = Button(window, text=text, padx=20, pady=10, command=command)
    button.grid(row=row, column=column)
    return button

# Create the main window
window = Tk()
window.title("Calculator")

# Create the entry field
entry = Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the number buttons
number_buttons = [create_button(str(num), row=1 + i//3, column=i%3, command=lambda num=num: button_click(num)) for i, num in enumerate(range(1, 10))]
number_buttons.append(create_button('0', row=4, column=1, command=lambda: button_click(0)))

# Create the operator buttons
operator_buttons = [
    create_button('+', row=4, column=3, command=lambda: button_click('+')),
    create_button('-', row=3, column=3, command=lambda: button_click('-')),
    create_button('*', row=2, column=3, command=lambda: button_click('*')),
    create_button('/', row=5, column=2, command=lambda: button_click('/')),
    create_button('^', row=1, column=3, command=lambda: button_click('**')),
    create_button('!', row=4, column=0, command=lambda: button_click('!')),
    create_button('.', row=4, column=2, command=lambda: button_click('.'))
]

# Create the clear, equal, and square root buttons
create_button('C', row=5, column=0, command=button_clear)
create_button('=', row=5, column=1, command=button_equal)
create_button('√', row=5, column=3, command=button_sqrt)

# Run the main loop
window.mainloop()

