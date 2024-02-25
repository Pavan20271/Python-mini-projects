import tkinter as tk
from tkinter import messagebox

class BinarySearch:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Search")
        
        self.label = tk.Label(master, text="Enter a sorted list of numbers:")
        self.label.pack()

        self.entry = tk.Entry(master, width=30)
        self.entry.pack()

        self.search_label = tk.Label(master, text="Enter the number to search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(master, width=15)
        self.search_entry.pack()

        self.button = tk.Button(master, text="Search", command=self.search)
        self.button.pack()

    def search(self):
        try:
            numbers = list(map(int, self.entry.get().split()))
            target = int(self.search_entry.get())
            result = self.binary_search(numbers, target)
            if result != -1:
                messagebox.showinfo("Result", f"Number {target} found at index {result}.")
            else:
                messagebox.showinfo("Result", f"Number {target} not found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid list of numbers.")

    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

def main():
    root = tk.Tk()
    app = BinarySearch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
