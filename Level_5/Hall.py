import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import subprocess
hall_window = tk.Tk()
hall_window.title("Hall")
screen_width = hall_window.winfo_screenwidth()
screen_height = hall_window.winfo_screenheight()
hall_window.geometry(f"{screen_width}x{screen_height}")
hall_window.state('zoomed')

bg_image = Image.open("Level_5/Image/Hall 2.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(hall_window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        hall_window.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

def back(event):
    subprocess.Popen(["python","Level_5.py"])
    hall_window.destroy()

back_image = (Image.open("Image/Back.png")).resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

hall_window.mainloop()