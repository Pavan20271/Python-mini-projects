import tkinter as tk
import random

def guess_number():
    guess = int(guess_entry.get())
    if guess == computer_number:
        result_label.config(text="You guessed it! Congratulations!")
    elif guess < computer_number:
        result_label.config(text="Too low. Try again.")
    else:
        result_label.config(text="Too high. Try again.")

root = tk.Tk()
root.title("Guess the Number")

computer_number = random.randint(1, 100)

instruction_label = tk.Label(root, text="I'm thinking of a number between 1 and 100. Guess it!")
instruction_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_number)
guess_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
