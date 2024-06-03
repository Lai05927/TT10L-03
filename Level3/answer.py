from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess

Answer = tk.Tk()
Answer.title('Clues')
screen_height = Answer.winfo_screenheight()
screen_width = Answer.winfo_screenwidth()
Answer.geometry(f"{screen_width}x{screen_height}")

bg_image = ImageTk.PhotoImage(file=r"Level3\Image\book(1).png")
canvas = tk.Canvas(Answer, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_width / 2, screen_height / 2, anchor='center', image=bg_image)

shadow_image = ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
canvas.create_image(250 / 1536 * screen_width, 100 / 864 * screen_height, anchor="nw", image=shadow_image)

shadow_2_image = ImageTk.PhotoImage(Image.open("Image/Shadow (2).png"))
canvas.create_image(250 / 1536 * screen_width, 400 / 864 * screen_height, anchor="nw", image=shadow_2_image)

txt = '\n\n\n\n\nWas Lucy really violated? Who is it?!!\ni. No\nii. Yes,Peter\niii. Yes,Jart'
text_item = canvas.create_text(screen_width/2,110/864*screen_height, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        Answer.after(40, slider)

slider()

def show_message(event):
    messagebox.showinfo("Correct!!!","You are right!!Congrat!!")

button_image_i= ImageTk.PhotoImage(Image.open(r"Level3\Image\button_i.png"))
button_i=canvas.create_image(500,500, image=button_image_i)
canvas.tag_bind(button_i,"<Button-1>", show_message)

def show_message(event):
    messagebox.showinfo("Wrong..","You are wrong.Try again!!")

button_image_ii= ImageTk.PhotoImage(Image.open(r"Level3/Image/button_ii.png"))
button_ii=canvas.create_image(750,500, image=button_image_ii)
canvas.tag_bind(button_ii,"<Button-1>", show_message)

def show_message(event):
    messagebox.showinfo("Wrong..","You are wrong.Try again!!")

button_image_iii= ImageTk.PhotoImage(Image.open(r"Level3/Image/button_iii.png"))
button_iii=canvas.create_image(1000,500, image=button_image_ii)
canvas.tag_bind(button_iii,"<Button-1>", show_message)

def next_level(event):
    subprocess.Popen(["python","Level4/story5.py"])
    Answer.destroy()

next_image = (Image.open(r"Level3\Image\button_next-level.png"))
next_image_tk = ImageTk.PhotoImage(next_image)
next_button = canvas.create_image(1300/1536*screen_width, 720/864*screen_height, image=next_image_tk)
canvas.tag_bind(next_button, "<Button-1>", next_level)

def home(event):
    subprocess.Popen(["python", "Index.py"])
    Answer.destroy()

home_image = (Image.open("Level3\Image\Home.png")).resize((45, 45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(170 / 1536 * screen_width, 110 / 864 * screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python", "Level3/Level_3.py"])
    Answer.destroy()

back_image = (Image.open("Level3\Image\Back.png")).resize((45, 45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(230 / 1536 * screen_width, 110 / 864 * screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

Answer.mainloop()