from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import pygame
import json
import os
from tkinter import ttk
root = tk.Tk()
root.title("Level 5")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')


# Ensure the script gets a username argument
user_name = "yl"

# Filename where to store user data
USER_DATA_FILE = 'user_data.json'

# Load user data from file
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

# Save user data to file
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file)

# Update user level
#def update_user_level(username, level):
#    user_data = load_user_data()
#    user_data[username]['level'] = level
#    save_user_data(user_data)

def update_user_level(username, level):
    user_data = load_user_data()

    # Check if username exists in user_data
    if username in user_data:
        user_data[username]['level'] = level
    else:
        # If username doesn't exist, create a new entry with default data
        user_data[username] = {'password': '', 'level': level}  # Add default password if necessary

    save_user_data(user_data)

update_user_level(user_name, 5) 
bg_image = Image.open("Level_5/Image/Background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

# Show rules in a popup window
def show_rules_popup(event):
    popup = tk.Toplevel(root)
    popup.title("Rules Level 5")
    popup.geometry("700x350")
    popup.config(bg="Grey")

    rules_text = """
    1. For level 5, you are entrusted to solve a case.
    2. Click the "Note" button at the bottom right corner to get the background of the story.
    3. In "Note", you are required to play the minigames to get 3 extra hints.
    4. Explore the "Hall" and "Room" scenes to get more hints.
    5. When you have all the clues, heading to the "Note" to solve the case.

    Good Luck And Have Fun!
    """

    text_widget = tk.Text(popup, font=("Comic Sans MS", 14), bg="grey", fg="white", wrap="word", bd=0)
    text_widget.insert("1.0", rules_text)
    text_widget.config(state="disabled")  # Make the text widget read-only
    text_widget.pack(padx=20, pady=20, fill="both", expand=True)

    close_button = tk.Button(popup, text="Close", command=popup.destroy, bg="gray", fg="white")
    close_button.pack(pady=10)


hint_image = (Image.open("Image/hints btn.png")).resize((45,45))
hint_image_tk = ImageTk.PhotoImage(hint_image)
hint_button = canvas.create_image(90/1280*screen_width, 30/720*screen_height, image=hint_image_tk)
canvas.tag_bind(hint_button, "<Button-1>", show_rules_popup)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def create_glow_effect(image, glow_color=(200, 200, 200, 255), radius=15):
    image = image.convert("RGBA")
    mask = image.split()[3]
    glow = Image.new("RGBA", image.size, glow_color)
    glow.putalpha(mask)
    expanded_mask = mask.resize((mask.width + 2 * radius, mask.height + 2 * radius), Image.LANCZOS)
    blurred_mask = expanded_mask.filter(ImageFilter.GaussianBlur(radius))
    glow_image = Image.new("RGBA", (image.width + 2 * radius, image.height + 2 * radius), (0, 0, 0, 0))
    expanded_glow = glow.resize((image.width + 2 * radius, image.height + 2 * radius), Image.LANCZOS)
    glow_image.paste(expanded_glow, (0, 0), mask=blurred_mask)
    glow_image.paste(image, (radius, radius), mask=image)
    
    return glow_image

def open_hall_window(event):
    subprocess.Popen(["python", "Level_5/Hall.py"])
    root.destroy()

hall_image = Image.open("Level_5/Image/Hall_Button.png")
hall_glow_image = create_glow_effect(hall_image)
hall_button_image = ImageTk.PhotoImage(hall_glow_image)
hall_button = canvas.create_image(655/1280*screen_width, 217/720*screen_height, image=hall_button_image)
canvas.tag_bind(hall_button, "<Button-1>", open_hall_window)

hall_white_button_image = ImageTk.PhotoImage((Image.open("Level_5/Image/White Button.png")).resize((50,50)))
hall_white_button = canvas.create_image(705/1280*screen_width, 167/720*screen_height, image=hall_white_button_image)
canvas.tag_bind(hall_button, "<Button-1>", open_hall_window)
hall_white_text = canvas.create_text(705/1280*screen_width, 167/720*screen_height, text="Hall", fill="black", state='normal', font=("Helvetica", 16))
canvas.tag_bind(hall_white_button, "<Button-1>", open_hall_window)

def open_room_window(event):
    subprocess.Popen(["python", "Level_5/Room.py"])
    root.destroy()

room_image = Image.open("Level_5/Image/Room_Button.png")
room_glow_image = create_glow_effect(room_image)
room_button_image = ImageTk.PhotoImage(room_glow_image)
room_button = canvas.create_image(211/1280*screen_width, 367/720*screen_height, image=room_button_image)
canvas.tag_bind(room_button, "<Button-1>", open_room_window)

room_white_button_image = ImageTk.PhotoImage((Image.open("Level_5/Image/White Button.png")).resize((50,50)))
room_white_button = canvas.create_image(261/1280*screen_width, 317/720*screen_height, image=room_white_button_image)
canvas.tag_bind(room_button, "<Button-1>", open_room_window)
room_white_text = canvas.create_text(261/1280*screen_width, 317/720*screen_height, text="Room", fill="black", state='normal', font=("Helvetica", 16))
canvas.tag_bind(room_white_button, "<Button-1>", open_room_window)

def open_note_window(event):
    subprocess.Popen(["python", "Level_5/Note.py"])
    root.destroy()

note_image = (Image.open("Level_5/Image/Note.png").resize((255,170)))
note_button_image = ImageTk.PhotoImage(note_image)
note_button = canvas.create_image(1160/1280*screen_width, 590/720*screen_height, image=note_button_image)
canvas.tag_bind(note_button, "<Button-1>", open_note_window)

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
pygame.mixer.music.load("Level_5/Image/mp3 4.mp3")

mute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Muted.jpg")).resize((50, 50)))
unmute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Unmute.png")).resize((50, 50)))

muted = False
mute_button = canvas.create_image(1230, 30, image=unmute_icon)
canvas.tag_bind(mute_button, "<Button-1>", toggle_mute)

pygame.mixer.music.play(-1)

root.mainloop()