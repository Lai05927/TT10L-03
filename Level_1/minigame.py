import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
from tkinter import messagebox
import pygame

#background music
import background_music

background_music.play_music("Level 1/Level 1 image/Sakura-Girl-Motivation-chosic.com_.mp3")



#sound effect

pygame.mixer.init()
button_click_sound = pygame.mixer.Sound("Level 1/Level 1 image/mixkit-game-ball-tap-2073.wav")# Load sound effects

def play_sound(sound):
    pygame.mixer.Sound.play(sound) # Function to play sound effects




#answer background
board_image = Image.open("Level 1/Level 1 image/blank blackboard (1).jpg")
board_photo = ImageTk.PhotoImage(board_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2.3, anchor="center", image=board_photo)


question_txt = "6/2 (1+2) = ?"
question_label = canvas.create_text(650, 240, text=question_txt, font=("Comic Sans MS", 35, "bold"), fill="WHITE")


def handle_button_click(is_correct):
    if is_correct:
        messagebox.showinfo("Answer", "Answer Correct")
        navigate_to_answer_window3()
    else:
        messagebox.showinfo("Answer", "Wrong Answer,Can't get the hint")
        subprocess.Popen(["Python","Level 1/clues.py"])
        root.destroy()

#option1


button_image= ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button.png"))
button=canvas.create_image(450,400, image=button_image)
canvas.tag_bind(button,"<Button-1>", lambda event:handle_button_click(False))


#option 3


button_image3=ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button (2).png"))
button=canvas.create_image(890,400, image=button_image3)
canvas.tag_bind(button,"<Button-1>", lambda event:handle_button_click(False))

# option9


button_image2=ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button (1).png"))
button=canvas.create_image(670,400, image=button_image2)
canvas.tag_bind(button,"<Button-1>", lambda event:handle_button_click(True))





def navigate_to_answer_window3():
    play_sound(button_click_sound) 
    subprocess.Popen(["python", "Level 1/answer3.py"])

    root.destroy() 



root.mainloop()
