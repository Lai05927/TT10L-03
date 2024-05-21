from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import subprocess
root = tk.Tk()
root.title('Level 3')
root.geometry("1280x720")

# Load background image
image_story4 = ImageTk.PhotoImage(file=r"Level3\Image\storyline 4 background.png")
bg_image =image_story4

# Create canvas
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack(fill='both',expand=True)

# Display background image on canvas
canvas.create_image(0, 0, anchor='nw', image=bg_image)

txt = '\n\n\n\n\nYesterday Lucy and her colleagues Peter,Jart and Ava went camping\ntogether. That night, everyone got drunk...'
text_item = canvas.create_text(640,40, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        root.after(40, slider)

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
button=canvas.create_image(797,500, image=button_image)
canvas.tag_bind(button,"<Button-1>", show_message)

def open_Lucy_window(event):
    subprocess.Popen(["python", "Level3/Lucy.py"])
    root.destroy()

Lucy_button_image = ImageTk.PhotoImage(Image.open("Level3\Image\Lucy.png"))
lucy_button = canvas.create_image(890, 510, image=Lucy_button_image)
canvas.tag_bind(lucy_button, "<Button-1>", open_Lucy_window)
    
root.mainloop()