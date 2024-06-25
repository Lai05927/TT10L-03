import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
import pygame

import background_music

background_music.play_music("Level_1/Level 1 image/mixkit-melodic-bonus-collect-1938.wav")

#sound effect
pygame.mixer.init()
button_click_sound = pygame.mixer.Sound("Level_1/Level 1 image/mixkit-game-ball-tap-2073.wav")# Load sound effects

def play_sound(sound):
    pygame.mixer.Sound.play(sound) # Function to play sound effects


#answer background
board_image = Image.open("Level_1/Level 1 image/blackboard.jpeg")
board_photo = ImageTk.PhotoImage(board_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2.3, anchor="center", image=board_photo)


# answer1
answer1_txt = "  YES.Mom is dead  "
answer1_count = 0
answer1_text = ""
answer1_label = canvas.create_text(600, 300, text=answer1_txt, font=("Comic Sans MS", 40, "bold"), fill="brown")


def animate_text():
    global answer1_count, answer1_text
    if answer1_count < len(answer1_txt):
        answer1_text += answer1_txt[answer1_count]
        canvas.itemconfig(answer1_label, text=answer1_text)
        answer1_count += 1
        root.after(50, animate_text)  
    else:
        # Animation finished
        pass

animate_text()

def home(event):
    play_sound(button_click_sound) 
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)


def back(event):
    play_sound(button_click_sound) 
    subprocess.Popen(['python','Level_1/Level_1.py'])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_photo = ImageTk.PhotoImage(back_image)
back_btn = canvas.create_image(120,52,image=back_photo)
canvas.tag_bind(back_btn,"<Button-1>",back)






def back_to_clues(event):
    play_sound(button_click_sound) 
    subprocess.Popen(["python","Level_1/clues.py"])
    root.destroy()

back_to_clues_image=Image.open("Image/button_back-to-clues (4).png")
back_to_clues_photo=ImageTk.PhotoImage(back_to_clues_image)
back_to_clues_btn=canvas.create_image(600,590,image=back_to_clues_photo)
canvas.tag_bind(back_to_clues_btn,"<Button-1>",back_to_clues)



root.mainloop()