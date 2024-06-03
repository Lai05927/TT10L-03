import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import subprocess

hall_window = tk.Tk()
hall_window.title("Hall")
screen_width = hall_window.winfo_screenwidth()
screen_height = hall_window.winfo_screenheight()
hall_window.geometry(f"{screen_width}x{screen_height}")
hall_window.state('zoomed')

bg_image = Image.open("Level_5/Image/Hall 3.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(hall_window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        hall_window.destroy()

home_image = (Image.open("Image/Home.png")).resize((45, 45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python", "Level_5.py"])
    hall_window.destroy()

back_image = (Image.open("Image/Back.png")).resize((45, 45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

character_image_files = ["Level_5/Image/Emberly.png", "Level_5/Image/Chandra.png", "Level_5/Image/Heidi.png",
                         "Level_5/Image/Reynold.png", "Level_5/Image/Kiara.png", "Level_5/Image/Jane.png",
                         "Level_5/Image/Mary.png"]
level_images = [ImageTk.PhotoImage(Image.open(img).resize((125, 222))) for img in character_image_files]
positions = [(500/1280*screen_width, 450/720*screen_height), (420/1280*screen_width, 550/720*screen_height),
             (690/1280*screen_width, 450/720*screen_height), (350/1280*screen_width, 550/720*screen_height),
             (760/1280*screen_width, 450/720*screen_height), (900/1280*screen_width, 550/720*screen_height),
             (1000/1280*screen_width, 550/720*screen_height)]

character_portrait_files = ["Level_5/Image/Emberly_Jellison.png", "Level_5/Image/Chandra_Jellison.png", "Level_5/Image/Heidi_Jellison.png",
                            "Level_5/Image/Reynold_Jellison.png", "Level_5/Image/Kiara_Jellison.png", "Level_5/Image/Jane_Scott.png",
                            "Level_5/Image/Mary_Scott.png"]
character_portraits = {name: ImageTk.PhotoImage(Image.open(img).resize((125, 222))) for name, img in zip(
    ["Emberly", "Chandra", "Heidi", "Reynold", "Kiara", "Jane", "Mary"], character_portrait_files)}

script_box = None
character_name_box = None
text_widget = None
selection_buttons_emberly = []
selection_buttons_chandra = []
selection_buttons_heidi = []
selection_buttons_reynold = []
selection_buttons_kiara = []
selection_buttons_jane = []
selection_buttons_mary = []
return_button = None
back_button = None
character_name_text = None
character_portrait = None

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

initial_texts = {
    "Emberly": "I am Emberly",
    "Chandra": "I am Chandra",
    "Heidi": "I am Heidi",
    "Reynold": "I am Reynold",
    "Kiara": "I am Kiara",
    "Jane": "I am Jane",
    "Mary": "I am Mary"
}

def update_character(name):
    global script_box, character_name_box, text_widget, character_name_text, character_portrait
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=name, state='normal')
    
    canvas.itemconfig(character_portrait, image=character_portraits[name], state='normal')
    canvas.coords(character_portrait, 100, 300)  # Update position if needed
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    if name == "Emberly":
        for button in selection_buttons_emberly:
            canvas.itemconfig(button, state='normal')
    elif name == "Chandra":
        for button in selection_buttons_chandra:
            canvas.itemconfig(button, state='normal')
    elif name == "Heidi":
        for button in selection_buttons_heidi:
            canvas.itemconfig(button, state='normal')
    elif name == "Reynold":
        for button in selection_buttons_reynold:
            canvas.itemconfig(button, state='normal')
    elif name == "Kiara":
        for button in selection_buttons_kiara:
            canvas.itemconfig(button, state='normal')
    elif name == "Jane":
        for button in selection_buttons_jane:
            canvas.itemconfig(button, state='normal')
    else:
        for button in selection_buttons_mary:
            canvas.itemconfig(button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_texts[name], 50))

command_functions = {
    "Emberly": lambda: update_character("Emberly"),
    "Chandra": lambda: update_character("Chandra"),
    "Heidi": lambda: update_character("Heidi"),
    "Reynold": lambda: update_character("Reynold"),
    "Kiara": lambda: update_character("Kiara"),
    "Jane": lambda: update_character("Jane"),
    "Mary": lambda: update_character("Mary")
}

for i, (img, name) in enumerate(zip(level_images, command_functions.keys())):
    button = canvas.create_image(positions[i][0], positions[i][1], anchor="center", image=img)
    canvas.tag_bind(button, "<Button-1>", command_functions[name])

def create_script_box(canvas, character_name, text, x, y, width, height, padding=15):
    global script_box, character_name_box, text_widget, character_name_text
    
    script_box = canvas.create_rectangle(x, y, x + width, y + height, fill='white', outline='black', width=2, state='hidden')
    
    character_name_box = canvas.create_rectangle(x, y - 45, x + 200, y, fill='lightblue', outline='black', width=2, state='hidden')
    character_name_text = canvas.create_text(x + 100, y - 22, text=character_name, font=('Helvetica', 12), anchor='center', state='hidden')
    
    wrapped_text = wrap_text(text, (width - 2 * padding) // 10)  # Adjust 10 based on font size and box width
    text_widget = canvas.create_text(x + padding, y + padding, text=wrapped_text, anchor='nw', font=('Helvetica', 12), state='hidden')

def create_text_selection_buttons(canvas, options, x, y):
    buttons = []
    for i, option in enumerate(options):
        button = tk.Button(hall_window, text=option, command=lambda opt=option: on_option_click(opt))
        button_window = canvas.create_window(x, y + i*30, anchor='nw', window=button, state='hidden')
        buttons.append(button_window)
    return buttons

def create_return_button(canvas, x, y):
    button = tk.Button(hall_window, text="Return", command=on_return_click)
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def create_back_button(canvas, x, y):
    button = tk.Button(hall_window, text="Back", command=on_back_click)
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def on_option_click(option):
    global selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary, return_button, back_button
    
    print(f"Option clicked: {option}")
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')

    canvas.itemconfig(return_button, state='normal')
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(text_widget, text=wrap_text(option, 50))

def on_return_click():
    global return_button, back_button
    canvas.itemconfig(return_button, state='hidden')
    canvas.itemconfig(back_button, state='hidden')
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='normal')

def on_back_click():
    global script_box, character_name_box, text_widget, character_portrait
    canvas.itemconfig(script_box, state='hidden')
    canvas.itemconfig(character_name_box, state='hidden')
    canvas.itemconfig(text_widget, state='hidden')
    canvas.itemconfig(character_portrait, state='hidden')

script_box_x = 120
script_box_y = screen_height - 200
script_box_width = screen_width - 240
script_box_height = 150

create_script_box(canvas, "", "", script_box_x, script_box_y, script_box_width, script_box_height)

selection_buttons_emberly = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_chandra = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_heidi = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_reynold = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_kiara = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_jane = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)
selection_buttons_mary = create_text_selection_buttons(canvas, ["Option 1", "Option 2", "Option 3"], 120, screen_height - 50)

return_button = create_return_button(canvas, screen_width - 200, screen_height - 50)
back_button = create_back_button(canvas, screen_width - 100, screen_height - 50)

character_portrait = canvas.create_image(0, 0, anchor='nw', state='hidden')

hall_window.mainloop()
