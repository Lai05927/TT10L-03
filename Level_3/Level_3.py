from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import os 
import sys
import pygame

pygame.mixer.init()

#Function to play sound
def play_button_click_sound():
    sound_file = "Level_3\Image\Yesterday Lucy and her co 3.wav"
    try:
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    except pygame.error as e:
        messagebox.showerror("Error", f"Cannot play sound: {e}")

def bird_sound():
    sound_file = r"Level_3\Image\the-voices-of-birds-in-the-forest-7715.mp3"
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(-1)#play continuously 
    except pygame.error as e:
        messagebox.showerror("Error", f"Cannot play sound: {e}")

# Ensure the script gets a username argument
user_name = "t"

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

update_user_level(user_name, 3) 

Level_3 = tk.Tk()
Level_3.title('Level 3')

screen_width = Level_3.winfo_screenwidth()
screen_height = Level_3.winfo_screenheight()
Level_3.geometry(f"{screen_width}x{screen_height}")

image_story4 = ImageTk.PhotoImage(file=r"Level_3\Image\storyline 4 background.png")
bg_image =image_story4
canvas = tk.Canvas(Level_3, width=screen_width, height=screen_height)
canvas.pack(fill='both',expand=True)
canvas.create_image(screen_width/2, screen_height/2, anchor='center', image=bg_image)

txt = '\n\n\n\n\nYesterday Lucy and her colleagues Peter,Jart and Ava went camping\ntogether. That night, everyone got drunk...'
text_item = canvas.create_text(screen_width/2,60/864*screen_height, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        Level_3.after(40, slider)

slider()

def open_clues_window(event):
    subprocess.Popen(["python", "Level_3/minigame.py"])
    Level_3.destroy()

button_image= ImageTk.PhotoImage(Image.open("Level_3\Image\Jart.png"))
button=canvas.create_image(355,518, image=button_image)
canvas.tag_bind(button,"<Button-1>", open_clues_window)

def open_clues_window(event):
    subprocess.Popen(["python", "Level_3/minigame.py"])
    Level_3.destroy()

button_image= ImageTk.PhotoImage(Image.open("Level_3/Image/Peter.png"))
button=canvas.create_image(426,497, image=button_image)
canvas.tag_bind(button,"<Button-1>", open_clues_window)

def open_clues_window(event):
    subprocess.Popen(["python", "Level_3/minigame.py"])
    Level_3.destroy()

button_image= ImageTk.PhotoImage(Image.open("Level_3\Image\Ava.png"))
button=canvas.create_image(893/1536*screen_width,547/864*screen_height, image=button_image)
canvas.tag_bind(button,"<Button-1>", open_clues_window)

def open_Lucy_window(event):
    subprocess.Popen(["python", "Level_3/minigame.py"])
    Level_3.destroy()

Lucy_button_image = ImageTk.PhotoImage(Image.open("Level_3\Image\Lucy.png"))
lucy_button = canvas.create_image(987/1536*screen_width, 560/864*screen_height, image=Lucy_button_image)
canvas.tag_bind(lucy_button, "<Button-1>", open_Lucy_window)

def answer(event):
    subprocess.Popen(["python","Level_3/answer.py"])
    Level_3.destroy()

answer_image = (Image.open(r"Level_3\Image\button_unravel-mysteries_3.png"))
answer_image_tk = ImageTk.PhotoImage(answer_image)
answer_button = canvas.create_image(1300/1536*screen_width, 720/864*screen_height, image=answer_image_tk)
canvas.tag_bind(answer_button, "<Button-1>", answer)

def home(event):
    subprocess.Popen(["python","Index.py"])
    Level_3.destroy()

home_image = (Image.open("Level_3\Image\Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(140/1536*screen_width, 80/864*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def logout(event):
    print(f"Logging out {user_name} and saving level 3")  # Debugging
    subprocess.Popen(["python","login/login.py"])
    Level_3.destroy()

logout_image = (Image.open("Level_3\Image\Logout.png")).resize((45,45))
logout_image_tk = ImageTk.PhotoImage(logout_image)
logout_button = canvas.create_image(210/1536*screen_width, 80/864*screen_height, image=logout_image_tk)
canvas.tag_bind(logout_button, "<Button-1>", logout)

def play_sound_button(event):
    play_button_click_sound()

sound_image = (Image.open("Level_3\Image\sound-button_275.png")).resize((45,45))
sound_button_image = ImageTk.PhotoImage(sound_image)
sound_button = canvas.create_image(270 / 1536 * screen_width, 80 / 864 * screen_height, image=sound_button_image)
canvas.tag_bind(sound_button, "<Button-1>", play_sound_button)

bird_sound()

Level_3.mainloop()