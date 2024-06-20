import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import tkinter.messagebox as messagebox
import pygame
from tkinter import ttk
note_window = tk.Tk()
note_window.title("Note")
screen_width = note_window.winfo_screenwidth()
screen_height = note_window.winfo_screenheight()
note_window.geometry(f"{screen_width}x{screen_height}")
note_window.state('zoomed')

bg_image = (Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height)))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(note_window, width=screen_width, height=screen_height)
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

def back(event):
    subprocess.Popen(["python","Level_5/Level_5.py"])
    note_window.destroy()

back_image = (Image.open("Image/Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        note_window.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

storyline = "Recently, the Jellison family are having their family dinner. The next day, Baldric Jellison been found dead in his house."
canvas.create_text(screen_width/2, screen_height/5, text=storyline, font=("Arial", 16), fill="black", width=screen_width-150)
storyline1 = "According to forensic verification, the cause of death was the sequelae of long-term alcoholism and taking PDE5 inhibitors (drugs for sexual dysfunction), coupled with the interaction between olanzapine (antipsychotic drug) and PDE5 inhibitors (drugs for sexual dysfunction), which caused a sharp drop in blood pressure and led to sudden death."
canvas.create_text(screen_width/2, screen_height/5+100, text=storyline1, font=("Arial", 16), fill="black", width=screen_width-200)

bottom_left_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(0, screen_height/2, anchor='nw', window=bottom_left_frame)
minigame_count=0
texts = ['The interests of the family can never be affected by personal choices, even if you are unhappy.', 'Emberly seems to be planning to start her own business.', 'Not all clues are true, be careful to distinguish them.']

def proceed_to_minigame():
    subprocess.Popen(["python", "Level_5/Minigame.py"])
    global minigame_count
    if minigame_count < len(texts):
        canvas.itemconfigure(text_items[minigame_count], state='normal')
        minigame_count += 1

text_items = []
for i, text in enumerate(texts):
    text_item = canvas.create_text(80, screen_height/5*3 + (i * 70) + 50, text=text, font=("Arial", 14), fill="black", state='hidden', width=screen_width/2-100, anchor='nw')
    text_items.append(text_item)

minigame_button = tk.Button(bottom_left_frame, text="Extra 3 hints", command=proceed_to_minigame, font=("Arial", 18))
minigame_button.pack(side='bottom', pady=20)

def proceed_to_mcq():
    subprocess.Popen(["python", "Level_5/Mcq.py"])
    pass

bottom_right_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(screen_width/2, screen_height/2, anchor='nw', window=bottom_right_frame)

mcq_button = tk.Button(bottom_right_frame, text="Solve the case", command=proceed_to_mcq, font=("Arial", 18))
mcq_button.pack(side='bottom', pady=20)

note_window.mainloop()