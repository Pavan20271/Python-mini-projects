import tkinter as tk
import random

# Define options and their corresponding values
options = ["Rock", "Paper", "Scissors"]
values = {
    "Rock": 0,
    "Paper": 1,
    "Scissors": 2,
}

# Initialize variables
computer_choice = None
player_choice = None
result = None

# Function to generate computer's choice
def generate_computer_choice():
    global computer_choice
    computer_choice = random.choice(options)

# Function to handle user's choice button clicks
def user_choice(choice):
    global player_choice, result
    player_choice = choice
    generate_computer_choice()
    determine_winner()

# Function to determine the winner
def determine_winner():
    global computer_choice, player_choice, result
    computer_value = values[computer_choice]
    player_value = values[player_choice]

    if player_value == computer_value:
        result = "Tie!"
    elif (player_value + 1) % 3 == computer_value:
        result = "You win!"
    else:
        result = "Computer wins!"

    update_labels()

# Function to update labels with choices and result
def update_labels():
    global computer_choice, player_choice, result
    computer_label.config(text=f"Computer: {computer_choice}")
    player_label.config(text=f"You: {player_choice}")
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create labels for computer's choice, player's choice, and result
computer_label = tk.Label(root, text="Computer: ?")
computer_label.pack()
player_label = tk.Label(root, text="You: ?")
player_label.pack()
result_label = tk.Label(root, text="")
result_label.pack()

# Create buttons for player's choices
rock_button = tk.Button(root, text="Rock", command=lambda: user_choice("Rock"))
rock_button.pack()
paper_button = tk.Button(root, text="Paper", command=lambda: user_choice("Paper"))
paper_button.pack()
scissors_button = tk.Button(root, text="Scissors", command=lambda: user_choice("Scissors"))
scissors_button.pack()

# Start the main loop
root.mainloop()
