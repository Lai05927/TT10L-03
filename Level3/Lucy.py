from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess

Lucy= tk.Tk()
Lucy.title('Lucy ')
screen_height = Lucy.winfo_screenheight()
screen_width = Lucy.winfo_screenwidth()
screen_height = Lucy.winfo_screenheight()
Lucy.geometry(f"{screen_width}x{screen_height}")

image_story4 = ImageTk.PhotoImage(file=r"Level3\Image\book(1).png")
bg_image =image_story4
canvas = tk.Canvas(Lucy, width=1280, height=720)
canvas.pack(fill='both',expand=True)
canvas.create_image(screen_width/2, screen_height/2, anchor='center', image=bg_image)

shadow_image=ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
shadow=canvas.create_image(250/1536*screen_width, 190/864*screen_height, anchor="nw", image=shadow_image)

txt = '\n\n\n\n\nWhen Lucy woke up in the morning, she found herself not\nwearing any clothes.She was very distraught, she felt\nviolated by someone else.'
text_item = canvas.create_text(screen_width/2,200/864*screen_height, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        Lucy.after(40, slider)
slider()

def home(event):
    subprocess.Popen(["python","Index.py"])
    Lucy.destroy()

home_image = (Image.open("Level3\Image\Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(170/1536*screen_width, 110/864*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level3/Level_3.py"])
    Lucy.destroy()

back_image = (Image.open("Level3\Image\Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(230, 110/864*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

Lucy.mainloop()