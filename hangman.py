import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.words = ["python", "hangman", "programming", "computer", "keyboard", "mouse", "monitor", "software"]
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = set()
        
        self.create_widgets()
        self.draw_hangman()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=300, height=300)
        self.canvas.pack()
        
        self.word_label = tk.Label(self.master, text=self.display_word())
        self.word_label.pack()
        
        self.label = tk.Label(self.master, text=f"Guesses left: {self.guesses_left}")
        self.label.pack()
        
        self.entry = tk.Entry(self.master)
        self.entry.pack()
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()
        
    def draw_hangman(self):
        parts = [
            (50, 280, 250, 280),   # base
            (150, 50, 150, 280),   # pole
            (140, 50, 150, 70),    # beam
            (140, 70, 200, 70),    # rope
            (200, 70, 200, 100),   # head
            (200, 100, 200, 200),  # body
            (200, 125, 175, 100),  # left arm
            (200, 125, 225, 100),  # right arm
            (200, 200, 175, 250),  # left leg
            (200, 200, 225, 250)   # right leg
        ]
        
        self.parts_drawn = []
        for part in parts:
            self.parts_drawn.append(self.canvas.create_line(part, width=3))

    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.secret_word)
        
    def check_guess(self):
        guess = self.entry.get()
        
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single letter.")
        elif guess in self.guessed_letters:
            messagebox.showwarning("Warning", "You've already guessed this letter.")
        else:
            self.guessed_letters.add(guess)
            if guess not in self.secret_word:
                self.guesses_left -= 1
                self.label.config(text=f"Guesses left: {self.guesses_left}")
                self.draw_hangman_part(self.guesses_left)
                
                if self.guesses_left == 0:
                    messagebox.showinfo("Game Over", f"Sorry, you're out of guesses. The word was '{self.secret_word}'.")
                    self.reveal_word()
                    self.reset_game()
            else:
                self.word_label.config(text=self.display_word())
                if self.all_letters_guessed():
                    messagebox.showinfo("Congratulations", f"Congratulations! You've guessed the word '{self.secret_word}'.")
                    self.reset_game()
        
    def draw_hangman_part(self, part_index):
        if part_index < len(self.parts_drawn):
            self.canvas.itemconfig(self.parts_drawn[part_index], fill="black")
                
    def all_letters_guessed(self):
        return set(self.secret_word) == self.guessed_letters
        
    def reveal_word(self):
        self.word_label.config(text=self.secret_word)
        
    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guesses_left = 6
        self.guessed_letters = set()
        self.word_label.config(text=self.display_word())
        self.label.config(text=f"Guesses left: {self.guesses_left}")
        self.entry.delete(0, tk.END)
        for part in self.parts_drawn:
            self.canvas.itemconfig(part, fill="white")

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
