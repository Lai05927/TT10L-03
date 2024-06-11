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








board_image = Image.open("Level 1/Level 1 image/give me a blank blac.jpg")
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










root.mainloop()