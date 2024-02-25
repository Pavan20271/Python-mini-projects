import tkinter as tk
from tkinter import messagebox
import random

class Minesweeper:
    def __init__(self, master, rows, cols, mines):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False

        self.generate_mines()
        self.calculate_numbers()

        for i in range(rows):
            for j in range(cols):
                self.buttons[i][j] = tk.Button(master, text="", width=2, height=1,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def generate_mines(self):
        count = 0
        while count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                count += 1

    def calculate_numbers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    continue
                for r in range(max(0, i - 1), min(self.rows, i + 2)):
                    for c in range(max(0, j - 1), min(self.cols, j + 2)):
                        if self.board[r][c] == -1:
                            self.board[i][j] += 1

    def on_button_click(self, row, col):
        if self.game_over or self.flags[row][col]:
            return
        if self.board[row][col] == -1:
            self.game_over = True
            self.reveal_board()
            messagebox.showinfo("Game Over", "You hit a mine! Game Over.")
        elif self.board[row][col] == 0:
            self.reveal_empty_cells(row, col)
        else:
            self.buttons[row][col].config(text=str(self.board[row][col]))

    def reveal_empty_cells(self, row, col):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols or self.board[row][col] != 0:
            return
        if self.buttons[row][col]['state'] == 'normal':
            self.buttons[row][col].config(text=str(self.board[row][col]))
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    self.reveal_empty_cells(r, c)

    def reveal_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == -1:
                    self.buttons[i][j].config(text="*")

def main():
    root = tk.Tk()
    minesweeper = Minesweeper(root, rows=8, cols=8, mines=10)
    root.mainloop()

if __name__ == "__main__":
    main()
