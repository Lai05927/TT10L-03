import tkinter as tk

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Character Script Box Example")

# Create Canvas
canvas = tk.Canvas(root, width=600, height=400, bg='lightgrey')
canvas.pack()

# Global variables to keep track of widgets
script_box = None
character_name_box = None
text_widget = None
selection_buttons = {}
return_button = None
back_button = None
character_name_text = None

# Initial texts and character names for buttons
button_data = {
    "Main": {
        "character_name": "Main Button",
        "initial_text": "Hello! This is a character script box for Main.",
        "options": ["Reynold", "Emberly", "Kiara"],
        "script_texts": {
            "Reynold": "I am Reynold",
            "Emberly": "I am Emberly, Reynold's sister.",
            "Kiara": "I am Kiara, Emberly's friend."
        }
    },
    "Sub": {
        "character_name": "Sub Button",
        "initial_text": "Hello! This is a character script box for Sub.",
        "options": ["Alice", "Bob", "Charlie"],
        "script_texts": {
            "Alice": "I am Alice",
            "Bob": "I am Bob, Alice's brother.",
            "Charlie": "I am Charlie, Bob's friend."
        }
    },
    "Third": {
        "character_name": "Third Button",
        "initial_text": "Hello! This is a character script box for Third.",
        "options": ["Rey", "Ember", "Kia"],
        "script_texts": {
            "Rey": "I am Rey",
            "Emberly": "I am Ember, Rey's sister.",
            "Kiara": "I am Kia, Ember's friend."
        }
    },
    # Add more buttons here with their respective data
}

def wrap_text(text, line_length):
    words = text.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= line_length:
            line += (word + " ")
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())
    return "\n".join(lines)

def create_script_box(canvas, character_name, text, x, y, width, height, padding=10):
    global script_box, character_name_box, text_widget, character_name_text
    
    # Draw the box
    script_box = canvas.create_rectangle(x, y, x + width, y + height, fill='white', outline='black', width=2, state='hidden')
    
    # Draw the character name box
    character_name_box = canvas.create_rectangle(x, y - 30, x + 100, y, fill='lightblue', outline='black', width=2, state='hidden')
    character_name_text = canvas.create_text(x + 50, y - 15, text=character_name, font=('Helvetica', 12), anchor='center', state='hidden')
    
    # Text wrapping and drawing text inside the box
    wrapped_text = wrap_text(text, (width - 2 * padding) // 10)  # Adjust 10 based on font size and box width
    text_widget = canvas.create_text(x + padding, y + padding, text=wrapped_text, anchor='nw', font=('Helvetica', 12), state='hidden')

def create_text_selection_buttons(canvas, options, x, y):
    buttons = []
    for i, option in enumerate(options):
        button = tk.Button(root, text=option, command=lambda opt=option: on_option_click(opt))
        button_window = canvas.create_window(x, y + i*30, anchor='nw', window=button, state='hidden')
        buttons.append(button_window)
    return buttons

def create_return_button(canvas, x, y):
    button = tk.Button(root, text="Return", command=on_return_click)
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def create_back_button(canvas, x, y):
    button = tk.Button(root, text="Back", command=on_back_click)
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def on_option_click(option):
    global selection_buttons, return_button, back_button
    # Update the text in the script box based on the selected option
    character_name = canvas.itemcget(character_name_text, 'text')
    script_texts = button_data[character_name]["script_texts"]
    new_text = script_texts.get(option, "")
    canvas.itemconfig(text_widget, text=wrap_text(new_text, 50))
    
    # Hide all selection buttons and back button
    for button in selection_buttons.values():
        canvas.itemconfig(button, state='hidden')
    
    # Show the return button
    canvas.itemconfig(return_button, state='normal')

def on_return_click():
    global selection_buttons, return_button, back_button
    # Restore the initial text
    character_name = canvas.itemcget(character_name_text, 'text')
    initial_text = button_data[character_name]["initial_text"]
    canvas.itemconfig(text_widget, text=wrap_text(initial_text, 50))
    
    # Hide the return button
    canvas.itemconfig(return_button, state='hidden')
    
    # Show the appropriate selection buttons
    character_options = button_data[character_name]["options"]
    for button in selection_buttons.values():
        if canvas.itemcget(button, 'text') in character_options:
            canvas.itemconfig(button, state='normal')
    
    # Show the back button
    canvas.itemconfig(back_button, state='normal')

def on_back_click():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons, back_button
    # Hide the back button
    canvas.itemconfig(back_button, state='hidden')
    
    # Hide the character name box, script box, and selection buttons
    canvas.itemconfig(character_name_box, state='hidden')
    canvas.itemconfig(character_name_text, state='hidden')  # Hide the character name text
    canvas.itemconfig(script_box, state='hidden')
    canvas.itemconfig(text_widget, state='hidden')
    for button in selection_buttons.values():
        canvas.itemconfig(button, state='hidden')

def on_button_click(button_name):
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons, back_button
    # Show the script box, character name box, and text widget
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=button_data[button_name]["character_name"], state='normal')
    
    # Show selection buttons for the button
    options = button_data[button_name]["options"]
    for button in selection_buttons[button_name]:
        canvas.itemconfig(button, state='normal')
    
    # Hide other selection buttons
    for other_button_name, other_buttons in selection_buttons.items():
        if other_button_name != button_name:
            for other_button in other_buttons:
                canvas.itemconfig(other_button, state='hidden')
    
    # Show back button
    canvas.itemconfig(back_button, state='normal')

    # Hide return button
    canvas.itemconfig(return_button, state='hidden')

    # Show initial text for button
    initial_text = button_data[button_name]["initial_text"]
    canvas.itemconfig(text_widget, text=wrap_text(initial_text, 50))

# Set positions for main, sub, and third buttons
button_positions = {
    "Main": (100, 130),
    "Sub": (170, 80),
    "Third": (220, 180),
}

# Create buttons based on button_data
for button_name, (x, y) in button_positions.items():
    button = tk.Button(root, text=button_name, command=lambda name=button_name: on_button_click(name))
    canvas.create_window(x, y, anchor='nw', window=button)
    selection_buttons[button_name] = create_text_selection_buttons(canvas, button_data[button_name]["options"], 400, 150)

# Create the script box and back/return buttons
create_script_box(canvas, "", "", 50, 300, 500, 80)
return_button = create_return_button(canvas, 400, 150)
canvas.itemconfig(return_button, state='hidden')
back_button = create_back_button(canvas, 400, 250)
canvas.itemconfig(back_button, state='hidden')

# Run the application
root.mainloop()