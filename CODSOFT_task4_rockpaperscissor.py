import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", "yellow"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        user_score_var.set(user_score_var.get() + 1)
        return "You win!", "green"
    else:
        computer_score_var.set(computer_score_var.get() + 1)
        return "Computer wins!", "red"

def play():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(choices)

    result, color = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    update_score_label()
    
    root.configure(background=color)

def update_score_label():
    score_label.config(text=f"User: {user_score_var.get()}  Computer: {computer_score_var.get()}")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Set the default background color
root.configure(background="white")

choices = ["rock", "paper", "scissors"]

user_choice_var = tk.StringVar()

# User choice radio buttons
for choice in choices:
    radio_button = tk.Radiobutton(root, text=choice, variable=user_choice_var, value=choice)
    radio_button.pack(pady=5)

# Play button
play_button = tk.Button(root, text="Play", command=play)
play_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Score label
user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
score_label = tk.Label(root, text="", font=("Helvetica", 12))
score_label.pack(side=tk.RIGHT, anchor=tk.NE)
update_score_label()

# Run the GUI
root.mainloop()
