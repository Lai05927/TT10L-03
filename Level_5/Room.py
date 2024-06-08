import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import subprocess
room_window = tk.Tk()
room_window.title("Room")
screen_width = room_window.winfo_screenwidth()
screen_height = room_window.winfo_screenheight()
room_window.geometry(f"{screen_width}x{screen_height}")
room_window.state('zoomed')

bg_image = Image.open("Level_5/Image/Room 2.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(room_window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        room_window.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level_5.py"])
    room_window.destroy()

back_image = (Image.open("Image/Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

script_box = None
character_name_box = None
text_widget = None
back_button = None
character_name_text = None
selection_buttons_smith = []
selection_buttons_baldric = []
return_button = None

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

initial_text_medicine = "The bottle packaging says it contains a PDE5 inhibitor, but it actually contains olanzapine."
character_name_medicine = "Medicine Bottle"

initial_text_cctv = "There is no surveillance at the estate."
character_name_cctv = "CCTV"

initial_text_scene = "There is no sign of a fight at the scene."
character_name_scene = "Scene"

initial_text_smith = "I'm Smith, a butler in the family."
character_name_smith = "Mr. Smith"

initial_text_baldric = "Chalk outline of Baldric"
character_name_baldric = "Baldric"

def Medicine(event):
    global script_box, character_name_box, text_widget, character_name_text, back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_medicine, state='normal')
    
    for button in selection_buttons_smith+selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')

    canvas.itemconfig(back_button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_medicine, 100))

def CCTV(event):
    global script_box, character_name_box, text_widget, character_name_text, back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_cctv, state='normal')
    
    for button in selection_buttons_smith+selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')

    canvas.itemconfig(back_button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_cctv, 100))

def Scene(event):
    global script_box, character_name_box, text_widget, character_name_text, back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_scene, state='normal')
    
    for button in selection_buttons_smith+selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')

    canvas.itemconfig(back_button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_scene, 100))

def Smith(event):
    global script_box, character_name_box, text_widget, character_name_text, back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_smith, state='normal')
    
    for button in selection_buttons_smith:
        canvas.itemconfig(button, state='normal')

    for button in selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_smith, 100))

def Baldric(event):
    global script_box, character_name_box, text_widget, character_name_text, back_button
    canvas.itemconfig(script_box, state='normal')
    canvas.itemconfig(character_name_box, state='normal')
    canvas.itemconfig(text_widget, state='normal')
    canvas.itemconfig(character_name_text, text=character_name_baldric, state='normal')
    
    for button in selection_buttons_baldric:
        canvas.itemconfig(button, state='normal')

    for button in selection_buttons_smith:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(back_button, state='normal')

    canvas.itemconfig(text_widget, text=wrap_text(initial_text_baldric, 100))

def on_hover_medicine(event):
    canvas.itemconfig(medicine_white_text, state='normal')

def on_leave_medicine(event):
    canvas.itemconfig(medicine_white_text, state='hidden')

medicine_image = ImageTk.PhotoImage(Image.open("Level_5/Image/Medicine_bottle.png").resize((70, 70)))
medicine_button = canvas.create_image(770/1280*screen_width, 465/720*screen_height, anchor="center", image=medicine_image)
canvas.tag_bind(medicine_button, "<Button-1>", Medicine)
medicine_white_text = canvas.create_text(770/1280*screen_width, 465/720*screen_height, text="Medicine", fill="black", state='hidden', font=("Helvetica", 16))
canvas.tag_bind(medicine_button, '<Enter>', on_hover_medicine)
canvas.tag_bind(medicine_button, '<Leave>', on_leave_medicine)

def on_hover_cctv(event):
    canvas.itemconfig(cctv_white_text, state='normal')

def on_leave_cctv(event):
    canvas.itemconfig(cctv_white_text, state='hidden')

cctv_image = ImageTk.PhotoImage((Image.open("Level_5/Image/White Button.png")).resize((50,50)))
cctv_button = canvas.create_image(1100/1280*screen_width, 100/720*screen_height, anchor="center", image=cctv_image)
canvas.tag_bind(cctv_button, "<Button-1>", CCTV)
cctv_white_text = canvas.create_text(1100/1280*screen_width, 100/720*screen_height, text="CCTV", fill="black", state='hidden', font=("Helvetica", 16))
canvas.tag_bind(cctv_button, '<Enter>', on_hover_cctv)
canvas.tag_bind(cctv_button, '<Leave>', on_leave_cctv)

def on_hover_scene(event):
    canvas.itemconfig(scene_white_text, state='normal')

def on_leave_scene(event):
    canvas.itemconfig(scene_white_text, state='hidden')

scene_image = ImageTk.PhotoImage((Image.open("Level_5/Image/White Button.png")).resize((50,50)))
scene_button = canvas.create_image(300/1280*screen_width, 350/720*screen_height, anchor="center", image=scene_image)
canvas.tag_bind(scene_button, "<Button-1>", Scene)
scene_white_text = canvas.create_text(300/1280*screen_width, 350/720*screen_height, text="Scene", fill="black", state='hidden', font=("Helvetica", 16))
canvas.tag_bind(scene_button, '<Enter>', on_hover_scene)
canvas.tag_bind(scene_button, '<Leave>', on_leave_scene)

smith_image = ImageTk.PhotoImage((Image.open("Level_5/Image/Smith.png")).resize((250, 444)))
smith_button = canvas.create_image(150/1280*screen_width,460/720*screen_height, anchor="center", image=smith_image)
canvas.tag_bind(smith_button, "<Button-1>", Smith)

baldric_image = ImageTk.PhotoImage((Image.open("Level_5/Image/Baldric.png")).resize((250, 170)))
baldric_button = canvas.create_image(1030/1280*screen_width,610/720*screen_height, anchor="center", image=baldric_image)
canvas.tag_bind(baldric_button, "<Button-1>", Baldric)

def on_option_click(option):
    global selection_buttons_smith, selection_buttons_baldric, return_button
    if option in ["Marriage between Baldric and Heidi","Whereabouts of Chandra","Call records"]:
        if option == "Marriage between Baldric and Heidi":
            new_text = "Heidi recently consulted the family lawyer about divorce."
        elif option == "Whereabouts of Chandra":
            new_text = "Chandra left the manor on the morning of the incident."
        else:
            new_text = "His phone call records were found, showing that he had recently been in frequent contact with an unknown number, but the call content had been deleted."
    else:
        if option == "Physical condition":
            new_text = "On the night of the incident, Baldric Jellison told his butler Mr. Smith that he felt unwell and asked him for medicine, but refused to seek medical help."
        elif option == "Temperament and habits":
            new_text = "He was extremely promiscuous and a long-term alcoholic."
        else:
            new_text = "Two diagnostic reports were found in his desk cabinet, one for sexual dysfunction and the other for schizophrenia."

    canvas.itemconfig(text_widget, text=wrap_text(new_text, 100))
    
    for button in selection_buttons_smith+selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')
    
    canvas.itemconfig(return_button, state='normal')

    canvas.itemconfig(back_button, state='hidden')

def create_script_box(canvas, character_name, text, x, y, width, height, padding=25):
    global script_box, character_name_box, text_widget, character_name_text
    
    script_box = canvas.create_rectangle(x, y, x + width, y + height, fill='white', outline='black', width=2, state='hidden')
    
    character_name_box = canvas.create_rectangle(x, y - 45, x + 200, y, fill='lightblue', outline='black', width=2, state='hidden')
    character_name_text = canvas.create_text(x + 100, y - 22, text=character_name, font=('Helvetica', 15), anchor='center', state='hidden')
    
    wrapped_text = wrap_text(text, (width - 2 * padding) // 10)
    text_widget = canvas.create_text(x + padding, y + padding, text=wrapped_text, anchor='nw', font=('Helvetica', 15), state='hidden')

create_script_box(canvas, character_name_scene, initial_text_scene, 100, screen_height/4*3, screen_width-200, screen_height/4-50)

def create_text_selection_buttons(canvas, options, x, y):
    buttons = []
    for i, option in enumerate(options):
        button = tk.Button(room_window, text=option, command=lambda opt=option: on_option_click(opt), font=('Helvetica', 12))
        button_window = canvas.create_window(x, y + i*40, anchor='nw', window=button, state='hidden')
        buttons.append(button_window)
    return buttons

def create_back_button(canvas, x, y):
    button = tk.Button(room_window, text="Back", command=on_back_click, font=('Helvetica', 12))
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def on_back_click():
    global script_box, character_name_box, text_widget, character_name_text, back_button, selection_buttons_smith, selection_buttons_baldric
    
    canvas.itemconfig(back_button, state='hidden')
    
    canvas.itemconfig(character_name_box, state='hidden')
    canvas.itemconfig(script_box, state='hidden')
    canvas.itemconfig(text_widget, state='hidden')
    canvas.itemconfig(character_name_text, text=character_name_scene, state='hidden')

    for button in selection_buttons_smith+selection_buttons_baldric:
        canvas.itemconfig(button, state='hidden')

def create_return_button(canvas, x, y):
    button = tk.Button(room_window, text="Return", command=on_return_click, font=('Helvetica', 12))
    button_window = canvas.create_window(x, y, anchor='nw', window=button, state='hidden')
    return button_window

def on_return_click():
    global selection_buttons_smith, selection_buttons_baldric, return_button
    
    if canvas.itemcget(character_name_text, 'text') == character_name_smith:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_smith, 100))
    elif canvas.itemcget(character_name_text, 'text') == character_name_baldric:
        canvas.itemconfig(text_widget, text=wrap_text(initial_text_baldric, 100))
    else:
        pass

    canvas.itemconfig(return_button, state='hidden')

    canvas.itemconfig(back_button, state='normal')
    
    if canvas.itemcget(character_name_text, 'text') == character_name_smith:
        for button in selection_buttons_smith:
            canvas.itemconfig(button, state='normal')
    elif canvas.itemcget(character_name_text, 'text') == character_name_baldric:
        for button in selection_buttons_baldric:
            canvas.itemconfig(button, state='normal')
    else:
        pass

back_button = create_back_button(canvas, 850, 450)
canvas.itemconfig(back_button, state='hidden')

return_button = create_return_button(canvas,  850, 300)
canvas.itemconfig(return_button, state='hidden')

selection_buttons_smith = create_text_selection_buttons(canvas, ["Marriage between Baldric and Heidi","Whereabouts of Chandra","Call records"], 850, 300)
selection_buttons_baldric = create_text_selection_buttons(canvas, ["Physical condition","Temperament and habits","Diagnostic reports"], 850, 300)


room_window.mainloop()