from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess

truth = tk.Tk()
truth.title('Clues')

screen_height = truth.winfo_screenheight()
screen_width = truth.winfo_screenwidth()
truth.geometry(f"{screen_width}x{screen_height}")

bg_image = ImageTk.PhotoImage(file=r"Level3\Image\book(1).png")
canvas = tk.Canvas(truth, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_width / 2, screen_height / 2, anchor='center', image=bg_image)

shadow_image = ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
canvas.create_image(250 / 1536 * screen_width, 290/ 864 * screen_height, anchor="nw", image=shadow_image)

tittle_text= canvas.create_text(screen_width/2,330/864*screen_height,anchor='center',text='Truth',fill='white',font=('Arial',30,'bold'))

txt = "\n\n\n\n\nLucy hadn't been violated. Ava did everything because she\nliked Peter but Peter liked Lucy so she took off Lucy's\nclothes at midnight to make Peter give up on Lucy."
text_item = canvas.create_text(screen_width/2,325/864*screen_height, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        truth.after(40, slider)

slider()

def home(event):
    subprocess.Popen(["python","Index.py"])
    truth.destroy()

home_image = (Image.open("Level3\Image\Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(170/1536*screen_width, 110/864*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

truth.mainloop()