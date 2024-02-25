import tkinter as tk

# Define story and placeholders
story = """Once upon a time, there was a brave **adjective** knight called **name**. He lived in a **adjective** kingdom ruled by a wise **adjective** king. One day, a **adjective** dragon attacked the kingdom. The knight, armed with his trusty **noun** and his **adjective** shield, set out to defeat the dragon.

The battle was long and hard, but the knight was determined. He used his **adjective** skills to dodge the dragon's fire, and his **adjective** sword to strike at its weak spots. Finally, with one **adjective** blow, the knight slayed the dragon and saved the kingdom.

The people cheered for their hero, and the king rewarded him with a feast and a **noun**. The knight lived happily ever after, known throughout the land as the bravest knight in the kingdom."""

placeholders = {
    "adjective": ["brave", "wise", "adjective"],
    "name": "Vikram",
    "noun": ["sword", "shield", "noun"],
}


def generate_story():
    # Retrieve user input from entry fields
    user_inputs = {}
    for placeholder, options in placeholders.items():
        user_inputs[placeholder] = entry_widgets[placeholder].get()

    # Validate input
    for placeholder, value in user_inputs.items():
        if placeholder == "adjective" and value not in placeholders[placeholder]:
            error_label.config(text=f"Invalid input for {placeholder}.")
            return
        elif value not in placeholders[placeholder]:
            error_label.config(text=f"Invalid input for {placeholder}.")
            return


    # Replace placeholders and display completed story
    completed_story = story
    for placeholder, value in user_inputs.items():
        completed_story = completed_story.replace(placeholder, value)
    story_label.config(text=completed_story)
    error_label.config(text="")



# Create the main window
root = tk.Tk()
root.title("Mad Libs Generator")

# Add labels and entry fields for each placeholder
entry_widgets = {}
for placeholder, options in placeholders.items():
    label = tk.Label(root, text=f"{placeholder}:")
    label.pack()
    entry = tk.Entry(root, width=20)
    entry.pack()
    entry_widgets[placeholder] = entry

# Add a button to generate the story
generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack()

# Add a label to display the completed story
story_label = tk.Label(root, text="")
story_label.pack()

# Add an error label for invalid input
error_label = tk.Label(root, text="")
error_label.pack()

# Start the event loop
root.mainloop()
