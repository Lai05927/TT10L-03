import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import subprocess
import pygame
from tkinter import ttk
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

def toggle_mute(event):
    global muted
    muted = not muted
    if muted:
        canvas.itemconfig(mute_button, image=mute_icon)
        pygame.mixer.music.set_volume(0)
    else:
        canvas.itemconfig(mute_button, image=unmute_icon)
        pygame.mixer.music.set_volume(1)

pygame.mixer.init()
pygame.mixer.music.load("Level_5/Image/mp3 5.mp3")

mute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Muted.jpg")).resize((50, 50)))
unmute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Unmute.png")).resize((50, 50)))

muted = False
mute_button = canvas.create_image(screen_width-50, 30, image=unmute_icon)
canvas.tag_bind(mute_button, "<Button-1>", toggle_mute)

pygame.mixer.music.play(-1)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        hall_window.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level_5/Level_5.py"])
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

initial_text_emberly = "I'm Emberly, the second daughter among three siblings, and I'm Baldric's sister."
character_name_emberly = "Emberly Jellison"

initial_text_chandra = "I'm Chandra, Reynold's wife."
character_name_chandra = "Chandra Jellison"

initial_text_heidi = "I am Heidi, Baldric's wife."
character_name_heidi = "Heidi Jellison"

initial_text_reynold = "I am Reynold, the youngest among three siblings, and I'm Baldric's brother."
character_name_reynold = "Reynold Jellison"

initial_text_kiara = "I am Kiara, Baldric's concubine."
character_name_kiara = "Kiara Jellison"

initial_text_jane = "I am Jane, a servant in the family."
character_name_jane = "Jane"

initial_text_mary = "I am Mary, a servant in the family."
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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_emberly, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_chandra, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_heidi, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_reynold, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_kiara, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_jane, 100))

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

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_mary, 100))

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
    if option in ["Family Business", "Encrypted email", "Emberly's call records"]:
        if option == "Family Business":
            new_text = "Emberly Jellison's notebook contained a detailed financial plan, which included important information about the company's internal business, indicating that she was secretly planning a huge investment recently, but the last page of the plan was deliberately torn off."
        elif option == "Encrypted email":
            new_text = "An encrypted email was found in Emberly's computer, which expressed her dissatisfaction with Baldric Jellison and her doubts about the family's current situation."
        elif option == "Emberly's call records":
            new_text = "Her phone call records were found, showing that she had recently frequently contacted an unknown number, but the content of the call had been deleted."
    elif option in ["Dispute on that night", "Chandra's call records", "Suicide case many years ago"]:
        if option == "Dispute on that night":
            new_text = "At the dinner party that night, Chandra had a fierce quarrel with Baldric, and then Baldric said he was not feeling well and went back to his room to rest."
        elif option == "Chandra's call records":
            new_text = "Chandra's mobile phone call records showed that she had spoken to Heidi several times on the night of the incident. According to her, the content of the call involved Heidi's health and family affairs."
        elif option == "Suicide case many years ago":
            new_text = "After investigation, the police found that Chandra's sister Isadora committed suicide by jumping off a building many years ago, and she had a dispute with Baldric before her death."
    elif option in ["Heidi's dispute", "Heidi's diary", "Medication"]:
        if option == "Heidi's dispute":
            new_text = "Heidi had a quarrel with Baldric the night before the crime."
        elif option == "Heidi's diary":
            new_text = "Her diary recorded her dissatisfaction with Baldric and her disappointment in marriage."
        elif option == "Medication":
            new_text = "Heidi suffers from depression and frequently takes antipsychotics."
    elif option in ["Dissatisfaction", "Reynold's diary", "Alibi"]:
        if option == "Dissatisfaction":
            new_text = "Family members' confessions mentioned that Reynold often expressed dissatisfaction with Baldric, and even quarreled with him frequently."
        elif option == "Reynold's diary":
            new_text = "Reynold's diary recorded his love and praise for Chandra, but each page ended with a same word 'sadly'."
        elif option == "Alibi":
            new_text = "He and Chandra were about to go to bed at the time of the crime."
    elif option in ["Dispute", "Private text messages", "Cell phone records"]:
        if option == "Dispute":
            new_text = "The night before the incident, Kiara did hear Heidi and Baldric arguing, and said that this was not the first time they had quarreled, and they quarreled almost every two or three days."
        elif option == "Private text messages":
            new_text = "A private text message record between her and Baldric was found, which showed her dissatisfaction with Baldric and her expectations for the future."
        elif option == "Cell phone records":
            new_text = "Kiara Jellison's cell phone records showed that she had frequent contact with a strange man recently, but the content was unknown."
    elif option in ["Miss Chandra", "Master Baldric", "Empty medicine bottle"]:
        if option == "Miss Chandra":
            new_text = "Miss Chandra is a very gentle person. It is rare for her to quarrel with Master Baldric like yesterday. She is really standing up for Miss Heidi."
        elif option == "Master Baldric":
            new_text = "Master Baldric is a pervert. He often speaks and behaves inappropriately to girls, which makes people feel uncomfortable. He is not often at home and only comes back occasionally for family dinners."
        elif option == "Empty medicine bottle":
            new_text = "When throwing away the garbage, the garbage bag was not tied tightly and an empty medicine bottle fell out."
    else:
        if option == "Witness":
            new_text = "Miss Heidi was witnessed entering Master Baldric's room at noon on the day of the crime."
        elif option == "Master Reynold and Miss Chandra":
            new_text = "Miss Chandra is an orphan, and their marriage was not blessed by the Earl and Countess. Their relationship is very strange; you can always feel that they love each other, but there is always some kind of obstacle separating them."
        elif option == "Mobile phone records":
            new_text = "Mary's mobile phone records show that she has had frequent contact with a strange man recently, but the content is unknown."
    
    canvas.itemconfig(text_widget, text=wrap_text(new_text, 100))
    
    for button in selection_buttons_emberly + selection_buttons_chandra + selection_buttons_heidi + selection_buttons_reynold + selection_buttons_kiara + selection_buttons_jane + selection_buttons_mary:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(return_button, state='normal')

    canvas.itemconfig(back_button, state='hidden')

def on_return_click():
    global selection_buttons_emberly, selection_buttons_chandra, selection_buttons_heidi, selection_buttons_reynold, selection_buttons_kiara, selection_buttons_jane, selection_buttons_mary, return_button
    
    if canvas.itemcget(character_name_text, 'text') == character_name_emberly:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_emberly, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_chandra:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_chandra, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_heidi:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_heidi, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_reynold:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_reynold, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_kiara:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_kiara, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_jane:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_jane, 100))
    else:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_mary, 100))
    
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
selection_buttons_emberly = create_text_selection_buttons(canvas, ["Family Business", "Encrypted email", "Emberly's call records"], 850, 300)
selection_buttons_chandra = create_text_selection_buttons(canvas, ["Dispute on that night","Chandra's call records","Suicide case many years ago"], 850, 300)
selection_buttons_heidi = create_text_selection_buttons(canvas, ["Heidi's dispute", "Heidi's diary", "Medication"],  850, 300)
selection_buttons_reynold = create_text_selection_buttons(canvas, ["Dissatisfaction", "Reynold's diary", "Alibi"],  850, 300)
selection_buttons_kiara = create_text_selection_buttons(canvas, ["Dispute", "Private text messages", "Cell phone records"],  850, 300)
selection_buttons_jane = create_text_selection_buttons(canvas, ["Miss Chandra", "Master Baldric", "Empty medicine bottle"],  850, 300)
selection_buttons_mary = create_text_selection_buttons(canvas, ["Witness", "Master Reynold and Miss Chandra", "Mobile phone records"],  850, 300)

return_button = create_return_button(canvas,  850, 300)
canvas.itemconfig(return_button, state='hidden')

back_button = create_back_button(canvas, 850, 450)
canvas.itemconfig(back_button, state='hidden')

hall_window.mainloop()