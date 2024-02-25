import tkinter as tk

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")

        self.board = [[tk.Entry(master, width=2) for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.board[i][j].grid(row=i, column=j)
                self.board[i][j].bind('<Key>', lambda event, row=i, col=j: self.on_key(event, row, col))

        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.grid(row=9, columnspan=9)

    def on_key(self, event, row, col):
        if not event.char.isdigit():
            return "break"
        self.board[row][col].delete(0, tk.END)
        self.board[row][col].insert(0, event.char)

    def solve(self):
        grid = [[int(self.board[i][j].get()) if self.board[i][j].get() else 0 for j in range(9)] for i in range(9)]
        if self.solve_sudoku(grid):
            self.update_board(grid)
        else:
            print("No solution exists for the given Sudoku puzzle.")

    def solve_sudoku(self, grid):
        empty_cell = self.find_empty_cell(grid)
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return True
                grid[row][col] = 0
        return False

    def find_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return None

    def is_valid_move(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def update_board(self, grid):
        for i in range(9):
            for j in range(9):
                self.board[i][j].delete(0, tk.END)
                self.board[i][j].insert(0, str(grid[i][j]))

def main():
    root = tk.Tk()
    sudoku_solver = SudokuSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
