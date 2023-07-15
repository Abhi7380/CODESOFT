from tkinter import *
from tkinter import simpledialog
from tkinter import colorchooser

class TodoList:
    def __init__(self, root):
        self.root = root
        
        self.root.title("To-Do List")

        # Create a listbox to display the tasks
        self.task_list = Listbox(root, width=1000)
        self.task_list.pack(pady=30)

        # Create a entry widget and button for adding tasks
        self.entry = Entry(root, width=1000)
        self.entry.pack()
        self.add_button = Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=15)

        # Create buttons for editing and deleting tasks
        self.edit_button = Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=15)
        self.delete_button = Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=15)

        # Populate the listbox with some initial tasks
        self.task_list.insert(END, "Task 1")
        self.task_list.insert(END, "Task 2")
        self.task_list.insert(END, "Task 3")

    def new_method(self):
        self.add_button.pack(highlightcolor=15)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_list.insert(END, task)
            self.entry.delete(0, END)

    def edit_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            selected_task = self.task_list.get(selected_index)
            new_task = simpledialog.askstring("Edit Task", "Enter a new task:", initialvalue=selected_task)
            if new_task:
                self.task_list.delete(selected_index)
                self.task_list.insert(selected_index, new_task)

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.task_list.delete(selected_index)

# Create the main window
root = Tk()

# Create an instance of the TodoList class
todo_list = TodoList(root)

# Run the application
root.mainloop()
