import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.lower_bound = 1
        self.upper_bound = 100
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.guesses_left = 10
        
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess the number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
    def check_guess(self):
        guess = self.entry.get()
        
        try:
            guess = int(guess)
            if guess < self.lower_bound or guess > self.upper_bound:
                messagebox.showwarning("Warning", f"Please enter a number between {self.lower_bound} and {self.upper_bound}.")
            else:
                self.guesses_left -= 1
                if guess == self.secret_number:
                    messagebox.showinfo("Congratulations", f"Correct! You guessed the number {self.secret_number}!")
                    self.reset_game()
                else:
                    if self.guesses_left == 0:
                        messagebox.showinfo("Game Over", f"Sorry, you've run out of guesses. The correct number was {self.secret_number}.")
                        self.reset_game()
                    else:
                        message = f"Wrong!{' Higher' if guess < self.secret_number else ' Lower'}. Guesses left: {self.guesses_left}."
                        messagebox.showinfo("Incorrect Guess", message)
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")
            
    def reset_game(self):
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.guesses_left = 10
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
