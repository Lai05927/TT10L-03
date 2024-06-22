import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')
import pygame



#background music
import background_music
background_music.play_music("Level_1/Level 1 image/dark-ambient-horror-cinematic-halloween-atmosphere-scary-118585.mp3")






board_image = Image.open("Level_1/Level 1 image/give me a blank blac.jpg")
board_photo = ImageTk.PhotoImage(board_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=board_photo)

story_txt=" My mother passed away a few days ago,and her death has hit me hard.\n\n I've been experiencing hallucinations and sleepwalking. \n\n At night, in a sleepwalking state,I wear the beautiful clothes my mother \n bought me during her lifetime and spray the perfume she gave me before \n she passed away.I go to her grave and talk to her.\n\n That day, when I looked in the mirror, I saw my reflection as my mother,\n and I started arguing with it. \n\n Accidentally, I pushed the mirror, and it shattered on the ground. \n I quickly tried to pick up the broken pieces,cutting my hand on the glass,\n and blood started to flow."


current_text_index=0
display_txt=""
text_item=canvas.create_text(screen_width/2, screen_height/2 , anchor="center" , text=story_txt[current_text_index],fill='white', font=('Comic Sans MS', 18, 'bold'), width=screen_width-100)

def animate_text():
    global current_text_index , display_txt 
    if current_text_index < len(story_txt) : #少过就显示字 
        display_txt +=story_txt[current_text_index] #显示storytext 后再去 看现在的 currenttext
        canvas.itemconfig(text_item, text=display_txt) #更新桌面text 
        current_text_index +=1
        root.after(10, animate_text)  # Adjust the delay as needed

animate_text()

def show_full_text(event):
    global display_txt, current_text_index
    display_txt = story_txt
    current_text_index = len(story_txt)
    canvas.itemconfig(text_item, text=display_txt)

# Bind the Enter key to show the full text
root.bind('<Return>', show_full_text)

def home(event):
    
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(screen_width/30, screen_height/40, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)


def back(event):

    subprocess.Popen(['python','Level_1/Level_1.py'])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_photo = ImageTk.PhotoImage(back_image)
back_btn = canvas.create_image(124,43,image=back_photo)
canvas.tag_bind(back_btn,"<Button-1>",back)



def next_story(event):
    
    subprocess.Popen(['python','Level_3/Level_3.py'])
    root.destroy()
   
next_story_button_image1 = Image.open("Level_1/Level 1 image/button_next-story (1).png")
next_story_photo1 = ImageTk.PhotoImage(next_story_button_image1)
next_story_button1 = canvas.create_image(1120,640,image=next_story_photo1)
canvas.tag_bind(next_story_button1,"<Button-1>",next_story)





root.mainloop()