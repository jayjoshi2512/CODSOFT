# Contact Book Application
# The Contact Book is a desktop application built with Python and Tkinter for efficient contact management. Users can easily add, view, search, update, and delete contacts. Contacts are displayed in a stylish table with equally spaced columns for names and phone numbers, ensuring clarity and readability. The application ensures phone numbers are numeric and unique across contacts. It features an intuitive interface with clean input dialogs and attractive, color-coded buttons for each function. The Contact Book provides a simple and visually appealing way to manage your contact information effectively, combining functionality with a user-friendly design.

import tkinter as tk
from tkinter import messagebox, Toplevel, Entry, Label, Button
from tkinter.font import Font
from tkinter import ttk

# Data Structure to store contacts
contacts = {}

# Custom input dialog function
def custom_input_dialog(title, fields):
    input_window = Toplevel(root)
    input_window.title(title)
    input_window.geometry("400x200")
    input_window.config(bg="#e8f4f8")
    
    entries = {}
    
    for i, field in enumerate(fields):
        label = Label(input_window, text=field, bg="#e8f4f8", fg="#333333", font=custom_font)
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = Entry(input_window, font=custom_font, bg="#ffffff", fg="#333333", bd=2, relief="groove")
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry
    
    def on_submit():
        for field, entry in entries.items():
            entries[field] = entry.get()
        input_window.destroy()
    
    submit_btn = Button(input_window, text="Submit", command=on_submit, width=10, bg="#4caf50", fg="white", font=custom_font, bd=0, highlightthickness=0)
    submit_btn.grid(row=len(fields), columnspan=2, pady=10)
    
    input_window.transient(root)
    input_window.grab_set()
    root.wait_window(input_window)
    
    return entries

# Functions for contact operations
def add_contact():
    fields = ["Name", "Phone Number"]
    inputs = custom_input_dialog("Add Contact", fields)
    name = inputs["Name"]
    phone = inputs["Phone Number"]
    if not name or not phone:
        messagebox.showerror("Error", "Both fields are required!")
        return
    if not phone.isdigit():
        messagebox.showerror("Error", "Phone number must be numeric!")
        return
    for contact_name, details in contacts.items():
        if phone == details["phone"]:
            messagebox.showerror("Error", f"Contact with phone number {phone} already exists with name {contact_name}!")
            return
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return
    contacts[name] = {"phone": phone}
    messagebox.showinfo("Success", f"Contact {name} added successfully!")
    view_contacts()

def view_contacts():
    for item in contact_tree.get_children():
        contact_tree.delete(item)
    for index, (name, details) in enumerate(contacts.items(), start=1):
        contact_tree.insert("", "end", values=(index, name, details['phone']))

def search_contact():
    fields = ["Search Query"]
    inputs = custom_input_dialog("Search Contact", fields)
    query = inputs["Search Query"]
    found_contacts = {name: details for name, details in contacts.items() if query.lower() in name.lower() or query in details['phone']}
    for item in contact_tree.get_children():
        contact_tree.delete(item)
    if found_contacts:
        for index, (name, details) in enumerate(found_contacts.items(), start=1):
            contact_tree.insert("", "end", values=(index, name, details['phone']))
    else:
        messagebox.showinfo("No Match", "No matching contacts found!")

def update_contact():
    fields = ["Name", "New Phone Number"]
    inputs = custom_input_dialog("Update Contact", fields)
    name = inputs["Name"]
    phone = inputs["New Phone Number"]
    if name in contacts:
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number must be numeric!")
            return
        contacts[name] = {"phone": phone}
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    fields = ["Name"]
    inputs = custom_input_dialog("Delete Contact", fields)
    name = inputs["Name"]
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Setting up the GUI
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")
root.config(bg="#e8f4f8")

# Custom font
custom_font = Font(family="Helvetica", size=12, weight="bold")
title_font = Font(family="Helvetica", size=16, weight="bold")

# Style configuration for Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=(None, 12, 'bold'), background="#4caf50", foreground="white")
style.configure("Treeview", font=(None, 12), rowheight=25, background="#f0f0f0", foreground="#333333")
style.map("Treeview", background=[('selected', '#4caf50')], foreground=[('selected', 'white')])

# Title Label
title_label = tk.Label(root, text="Contact Book", font=title_font, bg="#e8f4f8", fg="#333333")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#e8f4f8")
frame.pack(pady=20)

btn_add = tk.Button(frame, text="Add Contact", command=add_contact, width=15, bg="#4caf50", fg="white", font=custom_font, bd=0, highlightthickness=0)
btn_add.grid(row=0, column=0, padx=10, pady=5)

btn_view = tk.Button(frame, text="View Contacts", command=view_contacts, width=15, bg="#2196f3", fg="white", font=custom_font, bd=0, highlightthickness=0)
btn_view.grid(row=0, column=1, padx=10, pady=5)

btn_search = tk.Button(frame, text="Search Contact", command=search_contact, width=15, bg="#ff9800", fg="white", font=custom_font, bd=0, highlightthickness=0)
btn_search.grid(row=0, column=2, padx=10, pady=5)

btn_update = tk.Button(frame, text="Update Contact", command=update_contact, width=15, bg="#f44336", fg="white", font=custom_font, bd=0, highlightthickness=0)
btn_update.grid(row=1, column=0, padx=10, pady=5)

btn_delete = tk.Button(frame, text="Delete Contact", command=delete_contact, width=15, bg="#9c27b0", fg="white", font=custom_font, bd=0, highlightthickness=0)
btn_delete.grid(row=1, column=1, padx=10, pady=5)

# Create Treeview
columns = ('Index', 'Name', 'Phone')
contact_tree = ttk.Treeview(root, columns=columns, show='headings')
contact_tree.heading('Index', text='Index')
contact_tree.heading('Name', text='Name')
contact_tree.heading('Phone', text='Phone')

# Set column widths to be equal
contact_tree.column('Index', width=50)
contact_tree.column('Name', width=275)
contact_tree.column('Phone', width=275)

contact_tree.pack(pady=20)

# Start the GUI main loop
root.mainloop()
