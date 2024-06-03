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

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level_5.py"])
    hall_window.destroy()

back_image = (Image.open("Image/Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

character_image_file=["Level_5/Image/Emberly.png","Level_5/Image/Chandra.png","Level_5/Image/Heidi.png",
                  "Level_5/Image/Reynold.png","Level_5/Image/Kiara.png","Level_5/Image/Jane.png",
                  "Level_5/Image/Mary.png"]
level_images = [ImageTk.PhotoImage(Image.open(img).resize((125, 222))) for img in character_image_file]
positions=  [(500/1280*screen_width, 450/720*screen_height), (420/1280*screen_width, 550/720*screen_height), 
             (690/1280*screen_width, 450/720*screen_height), (350/1280*screen_width, 550/720*screen_height), 
             (760/1280*screen_width, 450/720*screen_height), (900/1280*screen_width, 550/720*screen_height), 
             (1000/1280*screen_width, 550/720*screen_height), ]

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

initial_text_emberly = "I am Emberly"
character_name_emberly = "Emberly Jellison"

initial_text_chandra = "I am Chandra"
character_name_chandra = "Chandra Jellison"

initial_text_heidi = "I am Heidi"
character_name_heidi = "Heidi Jellison"

initial_text_reynold = "I am Reynold"
character_name_reynold = "Reynold Jellison"

initial_text_kiara = "I am Kiara"
character_name_kiara = "Kiara Jellison"

initial_text_jane = "I am Jane"
character_name_jane = "Jane"

initial_text_mary = "I am Mary"
character_name_mary = "Mary"

def Emberly():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_emberly, state='normal')
    
    for button in selection_buttons_emberly:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_emberly, 50))

def Chandra():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_chandra, state='normal')
    
    for button in selection_buttons_chandra:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_chandra, 50))

def Heidi():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_heidi, state='normal')
    
    for button in selection_buttons_heidi:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_heidi, 50))

def Reynold():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_reynold, state='normal')
    
    for button in selection_buttons_reynold:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_reynold, 50))

def Kiara():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_kiara, state='normal')
    
    for button in selection_buttons_kiara:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_kiara, 50))

def Jane():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_jane, state='normal')
    
    for button in selection_buttons_jane:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_jane, 50))

def Mary():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary,back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_mary, state='normal')
    
    for button in selection_buttons_mary:
        canvas.itemconfig(button, state='normal')
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_mary, 50))

command=[Emberly, Chandra, Heidi, Reynold, Kiara, Jane, Mary]

for i, (img, cmd) in enumerate(zip(level_images, command)):
        button = canvas.create_image(positions[i][0], positions[i][1], anchor="center", image=img)
        canvas.tag_bind(button, "<Button-1>", lambda event, command=cmd: command())

def create_script_box(canvas, character_name, text, x, y, width, height, padding=25):
    global script_box, character_name_box, text_widget, character_name_text
    
    script_box = canvas.create_rectangle(x, y, x + width, y + height, fill='white', outline='black', width=2, state='hidden')
    
    character_name_box = canvas.create_rectangle(x, y - 45, x + 200, y, fill='lightblue', outline='black', width=2, state='hidden')
    character_name_text = canvas.create_text(x + 100, y - 22, text=character_name, font=('Helvetica', 15), anchor='center', state='hidden')
    
    wrapped_text = wrap_text(text, (width - 2 * padding) // 10)
    text_widget = canvas.create_text(x + padding, y + padding, text=wrapped_text, anchor='nw', font=('Helvetica', 15), state='hidden')

def create_text_selection_buttons(canvas, options, x, y):
    buttons = []
    for i, option in enumerate(options):
        button = tk.Button(hall_window, text=option, command=lambda opt=option: on_option_click(opt), font=('Helvetica', 12))
        button_window = canvas.create_window(x, y + i*40, anchor='nw', window=button, state='hidden')
        buttons.append(button_window)
    return buttons

def create_return_button(canvas, x, y):
    button = tk.Button(hall_window, text="Return", command=on_return_click, font=('Helvetica', 12))
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def create_back_button(canvas, x, y):
    button = tk.Button(hall_window, text="Back", command=on_back_click, font=('Helvetica', 12))
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def on_option_click(option):
    global selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary, return_button
    if option in ["Relation with Baldric", "Where were you when the incident happened?", "Kiara"]:
        if option == "Relation with Baldric":
            new_text = "I am Reynold"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Emberly, Reynold's sister."
        elif option == "Kiara":
            new_text = "I am Kiara, Emberly's friend"
    elif option in ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"]:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    elif option in ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"]:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    elif option in ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"]:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    elif option in ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"]:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    elif option in ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"]:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    else:
        if option == "Relation with Baldric":
            new_text = "I am Relation with Baldric"
        elif option == "Where were you when the incident happened?":
            new_text = "I am Where were you when the incident happened?, Relation with Baldric's brother."
        elif option == "Charlie":
            new_text = "I am Charlie, Where were you when the incident happened?'s friend"
    
    canvas.itemconfig(text_widget, text=wrap_text(new_text, 50))
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(return_button, state='normal')

    canvas.itemconfig(back_button, state='hidden')

def on_return_click():
    global selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary, return_button
    
    if canvas.itemcget(character_name_text, 'text') == character_name_emberly:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_emberly, 50))
    elif canvas.itemcget(character_name_text, 'text') == character_name_chandra:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_chandra, 50))
    elif canvas.itemcget(character_name_text, 'text') == character_name_heidi:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_heidi, 50))
    elif canvas.itemcget(character_name_text, 'text') == character_name_reynold:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_reynold, 50))
    elif canvas.itemcget(character_name_text, 'text') == character_name_kiara:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_kiara, 50))
    elif canvas.itemcget(character_name_text, 'text') == character_name_jane:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_jane, 50))
    else:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_mary, 50))
    
    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(back_button, state='normal')
    
    if canvas.itemcget(character_name_text, 'text') == character_name_emberly:
        for button in selection_buttons_emberly:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_chandra:
        for button in selection_buttons_chandra:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_heidi:
        for button in selection_buttons_heidi:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_reynold:
        for button in selection_buttons_reynold:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_kiara:
        for button in selection_buttons_kiara:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_jane:
        for button in selection_buttons_jane:
            canvas.itemconfig(button, state='normal')
    else:
        for button in selection_buttons_mary:
            canvas.itemconfig(button, state='normal')

def on_back_click():
    global script_box, character_name_box, text_widget, character_name_text, selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary, back_button
    
    canvas.itemconfig(back_button, state='hidden')
    
    canvas.itemconfig(character_name_box, state='hidden')
    canvas.itemconfig(script_box, state='hidden')
    canvas.itemconfig(text_widget, state='hidden')
    canvas.itemconfig(character_name_text, text=character_name_emberly, state='hidden')
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')

create_script_box(canvas, character_name_emberly, initial_text_emberly, 100, screen_height/4*3, screen_width-200, screen_height/4-50)
selection_buttons_emberly = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Kiara"], 850, 300)
selection_buttons_chandra = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"], 850, 300)
selection_buttons_heidi = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"],  850, 300)
selection_buttons_reynold = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"],  850, 300)
selection_buttons_kiara = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"],  850, 300)
selection_buttons_jane = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"],  850, 300)
selection_buttons_mary = create_text_selection_buttons(canvas, ["Relation with Baldric", "Where were you when the incident happened?", "Charlie"],  850, 300)

return_button = create_return_button(canvas,  850, 300)
canvas.itemconfig(return_button, state='hidden')

back_button = create_back_button(canvas, 850, 450)
canvas.itemconfig(back_button, state='hidden')

hall_window.mainloop()