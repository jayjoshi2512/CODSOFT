# "Experience the timeless fun of Rock-Paper-Scissors in this engaging tkinter-based game. Players face off against a computer opponent, selecting their choice of Rock, Paper, or Scissors. The game dynamically determines the winner based on classic rules: Rock crushes Scissors, Scissors cuts Paper, and Paper covers Rock. With stylish button designs and intuitive user interface, players can easily navigate through rounds. At the end of each game, the result is displayed, showcasing the winner alongside their respective scores. It's a perfect blend of nostalgia and modern design, offering endless entertainment for players of all ages."

import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play a round
def play_round(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Update the result label
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    
    # Update scores
    if result == "You win!":
        scores['user'] += 1
    elif result == "You lose!":
        scores['computer'] += 1
    
    # Update score label
    score_label.config(text=f"Score - You: {scores['user']} Computer: {scores['computer']}")

# Function to reset the game and display result
def reset_game():
    # Get the winner and total points
    winner = "You" if scores['user'] > scores['computer'] else "Computer" if scores['user'] < scores['computer'] else "It's a tie"
    total_points = f"You: {scores['user']}, Computer: {scores['computer']}"

    # Display the result in a message box
    if winner == "It's a tie":
        messagebox.showinfo("Game Result", f"It's a tie! \n{total_points}")
    else:
        messagebox.showinfo("Game Result", f"The winner is {winner}!\n{total_points}")

    # Reset scores and labels
    scores['user'] = 0
    scores['computer'] = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 Computer: 0")

# Setting up the GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.config(bg="#F5F5F5")

# Fonts
title_font = ("Arial", 20, "bold")
button_font = ("Arial", 12)
result_font = ("Arial", 14)

# Colors
button_colors = ['#4CAF50', '#03A9F4', '#FF9800']  # Dark green, Dark blue, and Dark orange colors for buttons
reset_button_bg = "#3576D0"  # Dark Blue color for reset button

# Title
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=title_font, bg="#F5F5F5", fg="#333333")
title_label.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=result_font, bg="#F5F5F5", fg="#333333")
result_label.pack(pady=20)

# Score label
scores = {'user': 0, 'computer': 0}
score_label = tk.Label(root, text="Score - You: 0 Computer: 0", font=result_font, bg="#F5F5F5", fg="#333333")
score_label.pack(pady=10)

# Buttons for user choice
button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=20)

def create_button(text, command, color):
    button = tk.Button(button_frame, text=text, font=button_font, width=10, command=command, bg=color, fg="white", relief="flat")
    button.pack(side="left", padx=10)
    return button

rock_button = create_button("Rock", lambda: play_round("Rock"), button_colors[0])
paper_button = create_button("Paper", lambda: play_round("Paper"), button_colors[1])
scissors_button = create_button("Scissors", lambda: play_round("Scissors"), button_colors[2])

# Reset button
reset_button = tk.Button(root, text="Reset", font=button_font, width=10, command=reset_game, bg=reset_button_bg, fg="white", relief="flat")
reset_button.pack(pady=20)

# Main loop
root.mainloop()
