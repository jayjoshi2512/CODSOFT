# This Python program is a versatile password generator built with Tkinter. Users can specify the desired password length and choose from four character types: digits, uppercase letters, lowercase letters, and special symbols. Each selected type is guaranteed to be included at least once in the generated password, ensuring robust security. The interface displays the number of each character type used in the password and adjusts its size dynamically based on password length. Additionally, the program allows users to easily copy the generated password to the clipboard. This tool is ideal for creating strong, customized passwords for enhanced online security.

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_digits, use_uppercase, use_lowercase, use_symbols):
    characters = ''
    password = []
    if use_digits:
        characters += string.digits
        password.append(random.choice(string.digits))
    if use_uppercase:
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        messagebox.showerror("Error", "Please select at least one option for password generation.")
        return ""

    # Generate the remaining characters randomly
    while len(password) < length:
        password.append(random.choice(characters))
    
    # Shuffle the list to avoid a predictable pattern
    random.shuffle(password)

    password = ''.join(password)

    count_digits = sum(c in string.digits for c in password)
    count_uppercase = sum(c in string.ascii_uppercase for c in password)
    count_lowercase = sum(c in string.ascii_lowercase for c in password)
    count_symbols = sum(c in string.punctuation for c in password)

    return password, count_digits, count_uppercase, count_lowercase, count_symbols

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        use_digits = digits_var.get()
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_symbols = symbols_var.get()

        if use_digits + use_uppercase + use_lowercase + use_symbols > length:
            messagebox.showerror("Error", "Length is too short to include at least one of each selected type.")
            return

        password, count_digits, count_uppercase, count_lowercase, count_symbols = generate_password(
            length, use_digits, use_uppercase, use_lowercase, use_symbols
        )

        password_label.config(text=f"Generated Password:\n\n{password}")

        digits_count_label.config(text=f"- {count_digits}")
        uppercase_count_label.config(text=f"- {count_uppercase}")
        lowercase_count_label.config(text=f"- {count_lowercase}")
        symbols_count_label.config(text=f"- {count_symbols}")

        # Calculate new window size based on password length
        base_width = 500
        base_height = 400
        char_width = 10
        char_height = 30

        num_lines = (len(password) * char_width) // base_width + 1
        new_height = base_height + (num_lines - 1) * char_height
        new_width = max(base_width, min(1000, len(password) * char_width))

        root.geometry(f"{new_width}x{new_height}")

        password_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        copy_button.pack(side=tk.RIGHT, pady=5)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

def copy_password():
    password = password_label.cget("text").split(":\n\n")[1]
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password generated yet.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")
root.resizable(True, True)
root.configure(background="#ebebeb")

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 24), pady=10, bg="#ebebeb")
title_label.pack()

# Length label and entry
length_frame = tk.Frame(root, bg="#ebebeb")
length_frame.pack(pady=5)
length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 12), bg="#ebebeb")
length_label.grid(row=0, column=0, padx=(0, 10))
length_entry = tk.Entry(length_frame, font=("Arial", 12), width=5)
length_entry.grid(row=0, column=1, padx=(0, 10))

# Options frame
options_frame = tk.Frame(root, bg="#ebebeb")
options_frame.pack(pady=5)

# Checkboxes with counts
digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(options_frame, text="Digits", variable=digits_var, bg="#ebebeb", font=("Arial", 12))
digits_check.grid(row=0, column=0, sticky=tk.W)
digits_count_label = tk.Label(options_frame, text="- 0", bg="#ebebeb", font=("Arial", 12))
digits_count_label.grid(row=0, column=1, sticky=tk.W)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(options_frame, text="Uppercase Characters", variable=uppercase_var, bg="#ebebeb", font=("Arial", 12))
uppercase_check.grid(row=1, column=0, sticky=tk.W)
uppercase_count_label = tk.Label(options_frame, text="- 0", bg="#ebebeb", font=("Arial", 12))
uppercase_count_label.grid(row=1, column=1, sticky=tk.W)

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(options_frame, text="Lowercase Characters", variable=lowercase_var, bg="#ebebeb", font=("Arial", 12))
lowercase_check.grid(row=2, column=0, sticky=tk.W)
lowercase_count_label = tk.Label(options_frame, text="- 0", bg="#ebebeb", font=("Arial", 12))
lowercase_count_label.grid(row=2, column=1, sticky=tk.W)

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(options_frame, text="Special Symbols", variable=symbols_var, bg="#ebebeb", font=("Arial", 12))
symbols_check.grid(row=3, column=0, sticky=tk.W)
symbols_count_label = tk.Label(options_frame, text="- 0", bg="#ebebeb", font=("Arial", 12))
symbols_count_label.grid(row=3, column=1, sticky=tk.W)

# Generate and Copy Password buttons frame
buttons_frame = tk.Frame(root, bg="#ebebeb")
buttons_frame.pack()

# Generate button
generate_button = tk.Button(buttons_frame, text="Generate Password", command=generate_and_display_password, font=("Arial", 12), bg="#4CAF50", fg="white")
generate_button.pack(side=tk.LEFT, padx=5)

# Password frame to add padding
password_frame = tk.Frame(root, bg="#ebebeb")
password_frame.pack(fill=tk.BOTH, expand=True)

# Password label
password_label = tk.Label(password_frame, text="", font=("Arial", 14), wraplength=900, bg="#ebebeb")
password_label.pack(pady=10, fill=tk.BOTH, expand=True)

# Copy password button
copy_button = tk.Button(buttons_frame, text="Copy Password", command=copy_password, font=("Arial", 12), bg="#3576D0", fg="white")

root.mainloop()
