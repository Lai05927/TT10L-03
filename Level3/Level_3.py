from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess
Level_3 = tk.Tk()
Level_3.title('Level 3')
screen_width = Level_3.winfo_screenwidth()
screen_height = Level_3.winfo_screenheight()
Level_3.geometry(f"{screen_width}x{screen_height}")

# Load background image
image_story4 = ImageTk.PhotoImage(file=r"Level3\Image\storyline 4 background.png")
bg_image =image_story4

# Create canvas
canvas = tk.Canvas(Level_3, width=screen_width, height=screen_height)
canvas.pack(fill='both',expand=True)

# Display background image on canvas
canvas.create_image(screen_width/2, screen_height/2, anchor='center', image=bg_image)

txt = '\n\n\n\n\nYesterday Lucy and her colleagues Peter,Jart and Ava went camping\ntogether. That night, everyone got drunk...'
text_item = canvas.create_text(screen_width/2,50/864*screen_height, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

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

def show_message(event):
    messagebox.showinfo("Clue for Jart","1.He was the one who brought Lucy back to her tent after she got drunk.")

button_image= ImageTk.PhotoImage(Image.open("Level3\Image\Jart.png"))
button=canvas.create_image(355,518, image=button_image)
canvas.tag_bind(button,"<Button-1>", show_message)

def show_message(event):
    messagebox.showinfo("Clue for Peter","1.After he had drunk, he returned to his tent.\n2.He likes Lucy.")

button_image= ImageTk.PhotoImage(Image.open("Level3/Image/Peter.png"))
button=canvas.create_image(426,497, image=button_image)
canvas.tag_bind(button,"<Button-1>", show_message)

def show_message(event):
    messagebox.showinfo("Clue for Ava","1.She likes Peter")

button_image= ImageTk.PhotoImage(Image.open("Level3\Image\Ava.png"))
button=canvas.create_image(893/1536*screen_width,547/864*screen_height, image=button_image)
canvas.tag_bind(button,"<Button-1>", show_message)

def open_Lucy_window(event):
    subprocess.Popen(["python", "Level3/Lucy.py"])
    Level_3.destroy()

Lucy_button_image = ImageTk.PhotoImage(Image.open("Level3\Image\Lucy.png"))
lucy_button = canvas.create_image(987/1536*screen_width, 560/864*screen_height, image=Lucy_button_image)
canvas.tag_bind(lucy_button, "<Button-1>", open_Lucy_window)
    
def home(event):
    subprocess.Popen(["python","Index.py"])
    Level_3.destroy()

home_image = (Image.open("Level3\Image\Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(140/1536*screen_width, 80/864*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level3/Level_3.py"])
    Level_3.destroy()

back_image = (Image.open("Level3\Image\Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(200/1536*screen_width, 80/864*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

Level_3.mainloop()