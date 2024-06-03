from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess

Clues = tk.Tk()
Clues.title('Clues')
screen_height = Clues.winfo_screenheight()
screen_width = Clues.winfo_screenwidth()
Clues.geometry(f"{screen_width}x{screen_height}")

bg_image = ImageTk.PhotoImage(file=r"Level3\Image\book(1).png")
canvas = tk.Canvas(Clues, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_width / 2, screen_height / 2, anchor='center', image=bg_image)

shadow_image = ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
canvas.create_image(250 / 1536 * screen_width, 100 / 864 * screen_height, anchor="nw", image=shadow_image)

shadow_2_image = ImageTk.PhotoImage(Image.open("Image/Shadow (2).png"))
canvas.create_image(250 / 1536 * screen_width, 400 / 864 * screen_height, anchor="nw", image=shadow_2_image)

initial_text = '\n\n\n\nWhen Lucy woke up in the morning, she found herself not\nwearing any clothes. She was very distraught, she felt\nviolated by someone else.'
text_item = canvas.create_text(screen_width / 2, 130 / 864 * screen_height, anchor='center', text="", fill='white', font=('Arial', 24, 'bold'))

# Function to animate text display
def slider(text, item, index=0):
    if index <= len(text):
        canvas.itemconfig(item, text=text[:index])
        Clues.after(40, lambda: slider(text, item, index + 1))

# Animate initial text
slider(initial_text, text_item)

# Function to handle button click and display animated text
def on_button_click(event, text):
    for button in buttons:
        canvas.delete(button)
    display_text_animation(text)
    create_back_to_buttons_button()

# Function to animate text on the canvas
def display_text_animation(text):
    global text_anim, anim_index, anim_text
    anim_index = 0
    anim_text = text
    text_anim = canvas.create_text(screen_width / 2, 500 / 864 * screen_height, text="", fill='white', font=('Arial', 24, 'bold'))
    slider(anim_text, text_anim)

# Function to create "Back to Buttons" button
def create_back_to_buttons_button():
    global back_button_id, back_button_image_tk
    back_button_image = Image.open(r"Level3\Image\button_back.png")
    back_button_image_tk = ImageTk.PhotoImage(back_button_image)
    back_button_id = canvas.create_image(680, 640, image=back_button_image_tk, anchor='nw')
    canvas.tag_bind(back_button_id, "<Button-1>", back_to_buttons)

# Function to handle "Back to Buttons" action
def back_to_buttons(event):
    global text_anim, back_button_id
    canvas.delete(text_anim)
    canvas.delete(back_button_id)
    create_buttons()

# Data for buttons
button_data = [
    {"image_path": r"Level3\Image\button_ava.png", "text": "1.She likes Peter."},
    {"image_path": r"Level3\Image\button_jart.png", "text": "1.He was the one who brought Lucy back to\nher tent after she got drunk."},
    {"image_path": r"Level3\Image\button_peter.png", "text": "1.After he had drunk, he returned to his tent.\n2.He likes Lucy."}
]

horizontal_spacing = 300
initial_x = 450
initial_y = 500

# Lists to store button IDs and images to prevent garbage collection
buttons = []
button_images = []

# Function to create buttons
def create_buttons():
    global buttons, button_images
    for button in buttons:
        canvas.delete(button)
    buttons.clear()
    button_images.clear()
    for i, button_info in enumerate(button_data):
        image_path = button_info["image_path"]
        text = button_info["text"]
        image = Image.open(image_path)
        bttn_image = ImageTk.PhotoImage(image)
        button_images.append(bttn_image)
        button_x = initial_x + i * horizontal_spacing
        button_y = initial_y
        button_photo = canvas.create_image(button_x, button_y, image=bttn_image)
        buttons.append(button_photo)
        canvas.tag_bind(button_photo, "<Button-1>", lambda event, text=text: on_button_click(event, text))

# Create initial buttons
create_buttons()

def home(event):
    subprocess.Popen(["python", "Index.py"])
    Clues.destroy()

home_image = (Image.open("Level3\Image\Home.png")).resize((45, 45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(170 / 1536 * screen_width, 110 / 864 * screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python", "Level3/Level_3.py"])
    Clues.destroy()

back_image = (Image.open("Level3\Image\Back.png")).resize((45, 45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(230 / 1536 * screen_width, 110 / 864 * screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

Clues.mainloop()
