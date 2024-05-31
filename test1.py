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
selection_buttons_main = []
selection_buttons_sub = []
return_button = None
back_button = None
character_name_text = None

# Initial text and character name for Main and Sub
initial_text_main = "Hello! This is a character script box for Main."
character_name_main = "Main Button"

initial_text_sub = "Hello! This is a character script box for Sub."
character_name_sub = "Sub Button"

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
    global selection_buttons_main, selection_buttons_sub, return_button, back_button
    # Update the text in the script box based on the selected option
    if option in ["Reynold", "Emberly", "Kiara"]:
        if option == "Reynold":
            new_text = "I am Reynold"
        elif option == "Emberly":
            new_text = "I am Emberly, Reynold's sister."
        elif option == "Kiara":
            new_text = "I am Kiara, Emberly's friend"
    else:
        if option == "Alice":
            new_text = "I am Alice"
        elif option == "Bob":
            new_text = "I am Bob, Alice's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Bob's friend"
    
    canvas.itemconfig(text_widget, text=wrap_text(new_text, 50))
    
    # Hide all selection buttons and back button
    for button in selection_buttons_main + selection_buttons_sub + [back_button]:
        canvas.itemconfig(button, state='hidden')
    
    # Show the return button
    canvas.itemconfig(return_button, state='normal')

def on_return_click():
    global selection_buttons_main, selection_buttons_sub, return_button, back_button
    # Restore the initial text
    if canvas.itemcget(character_name_text, 'text') == character_name_main:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_main, 50))
    else:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_sub, 50))
    
    # Hide the return button
    canvas.itemconfig(return_button, state='hidden')
    
    # Show the appropriate selection buttons
    if canvas.itemcget(character_name_text, 'text') == character_name_main:
        for button in selection_buttons_main:
            canvas.itemconfig(button, state='normal')
    else:
        for button in selection_buttons_sub:
            canvas.itemconfig(button, state='normal')
    
    # Show the back button
    canvas.itemconfig(back_button, state='normal')

def on_back_click():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_main, selection_buttons_sub, back_button
    # Hide the back button
    canvas.itemconfig(back_button, state='hidden')
    
    # Hide the character name box, script box, and selection buttons
    canvas.itemconfig(character_name_box, state='hidden')
    canvas.itemconfig(character_name_text, state='hidden')  # Hide the character name text
    canvas.itemconfig(script_box, state='hidden')
    canvas.itemconfig(text_widget, state='hidden')
    for button in selection_buttons_main + selection_buttons_sub:
        canvas.itemconfig(button, state='hidden')

def on_main_click():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_main, selection_buttons_sub, back_button
    # Show the script box, character name box, and text widget
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_main, state='normal')
    
    # Show main selection buttons
    for button in selection_buttons_main:
        canvas.itemconfig(button, state='normal')
    
    # Hide sub selection buttons
    for button in selection_buttons_sub:
        canvas.itemconfig(button, state='hidden')
    
    # Show back button
    canvas.itemconfig(back_button, state='normal')

    # Hide return button
    canvas.itemconfig(return_button, state='hidden')

    # Show initial text for Main
    canvas.itemconfig(text_widget, text=wrap_text(initial_text_main, 50))

def on_sub_click():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_main, selection_buttons_sub, back_button
    # Show the script box, character name box, and text widget
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_sub, state='normal')
    
    # Show sub selection buttons
    for button in selection_buttons_sub:
        canvas.itemconfig(button, state='normal')
    
    # Hide main selection buttons
    for button in selection_buttons_main:
        canvas.itemconfig(button, state='hidden')
    
    # Show back button
    canvas.itemconfig(back_button, state='normal')

    # Hide return button
    canvas.itemconfig(return_button, state='hidden')

    # Show initial text for Sub
    canvas.itemconfig(text_widget, text=wrap_text(initial_text_sub, 50))

# Create the Main button
main_button = tk.Button(root, text="Main", command=on_main_click)
canvas.create_window(200, 200, anchor='nw', window=main_button)

# Create the Sub button
sub_button = tk.Button(root, text="Sub", command=on_sub_click)
canvas.create_window(300, 200, anchor='nw', window=sub_button)

# Create the initial script box and selection buttons for Main
create_script_box(canvas, character_name_main, initial_text_main, 50, 300, 500, 80)
selection_buttons_main = create_text_selection_buttons(canvas, ["Reynold", "Emberly", "Kiara"], 400, 150)

# Create the initial script box and selection buttons for Sub
selection_buttons_sub = create_text_selection_buttons(canvas, ["Alice", "Bob", "Charlie"], 400, 150)

# Create the return button but hide it initially
return_button = create_return_button(canvas, 400, 150)
canvas.itemconfig(return_button, state='hidden')

# Create the back button but hide it initially
back_button = create_back_button(canvas, 400, 250)
canvas.itemconfig(back_button, state='hidden')

# Run the application
root.mainloop()