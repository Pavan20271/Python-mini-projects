#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import filedialog, messagebox
import random

def generate_markov_chain(text, order=2):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])
        suffix = words[i+order]
        
        if prefix in markov_chain:
            markov_chain[prefix].append(suffix)
        else:
            markov_chain[prefix] = [suffix]
    
    return markov_chain

def generate_text(markov_chain, length=100):
    prefix = random.choice(list(markov_chain.keys()))
    text = list(prefix)
    
    while len(text) < length:
        if prefix in markov_chain:
            next_word = random.choice(markov_chain[prefix])
            text.append(next_word)
            prefix = tuple(text[-len(prefix):])
        else:
            break
    
    return ' '.join(text)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    else:
        messagebox.showwarning("Warning", "No file selected!")

def generate_and_display_text():
    text = text_entry.get('1.0', 'end-1c')
    if text:
        markov_chain = generate_markov_chain(text)
        generated_text = generate_text(markov_chain)
        generated_text_display.config(state='normal')
        generated_text_display.delete('1.0', 'end')
        generated_text_display.insert('1.0', generated_text)
        generated_text_display.config(state='disabled')
    else:
        messagebox.showwarning("Warning", "No text provided!")

# Create Tkinter window
window = tk.Tk()
window.title("Markov Chain Text Composer")

# Create widgets
load_button = tk.Button(window, text="Load Text File", command=load_file)
load_button.pack(pady=5)

text_entry_label = tk.Label(window, text="Or Enter Text:")
text_entry_label.pack()

text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

generate_button = tk.Button(window, text="Generate Text", command=generate_and_display_text)
generate_button.pack(pady=5)

generated_text_display = tk.Text(window, height=10, width=50, state='disabled')
generated_text_display.pack()

# Run the main event loop
window.mainloop()


# In[ ]:




