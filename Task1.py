#The To-Do List application is a user-friendly task management tool built with Python and Tkinter. It allows users to efficiently manage their daily tasks. Users can add new tasks, update existing ones, and delete multiple tasks simultaneously. The interface displays tasks with their respective indices for easy reference. The application features an intuitive graphical interface with buttons for adding, updating, and deleting tasks. The list box supports multiple task selection, making task management seamless and efficient. Ideal for users seeking a simple yet effective way to keep track of their tasks and improve productivity.

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Task list
        self.tasks = []

        # Title label
        self.title_label = tk.Label(root, text="To-Do List", font=('Arial', 18, 'bold'))
        self.title_label.pack(pady=10)

        # Task entry field
        self.task_entry = tk.Entry(root, font=('Arial', 14), width=40)
        self.task_entry.pack(pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", font=('Arial', 12, 'bold'), bg="#58D68D", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, font=('Arial', 12), width=40, height=10, selectmode=tk.MULTIPLE)
        self.task_listbox.pack(pady=10)

        # Buttons frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        # Update task button
        self.update_button = tk.Button(self.buttons_frame, text="Update Task", font=('Arial', 12, 'bold'), bg="#5DADE2", command=self.update_task)
        self.update_button.grid(row=0, column=0, padx=5)

        # Delete task button
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task(s)", font=('Arial', 12, 'bold'), bg="#E74C3C", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_indices = self.task_listbox.curselection()
        if not selected_task_indices:
            messagebox.showwarning("Warning", "Please select one or more tasks to delete.")
            return
        for index in reversed(selected_task_indices):
            self.tasks.pop(index)
        self.refresh_task_list()

    def update_task(self):
        selected_task_indices = self.task_listbox.curselection()
        if len(selected_task_indices) != 1:
            messagebox.showwarning("Warning", "Please select exactly one task to update.")
            return
        selected_task_index = selected_task_indices[0]
        new_task = self.task_entry.get()
        if new_task:
            self.tasks[selected_task_index] = new_task
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, f"{index + 1}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
