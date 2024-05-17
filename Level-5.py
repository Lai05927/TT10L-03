from PIL import Image, ImageTk
import tkinter as tk
import subprocess
root = tk.Tk()
root.title("Level 1")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

bg_image = Image.open("Level_5/Image/Background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

def open_hall_window(event):
    subprocess.Popen(["python", "Level_5/Hall.py"])
    root.destroy()

hall_button_image = ImageTk.PhotoImage(Image.open("Level_5/Image/Hall_Button.png"))
hall_button = canvas.create_image(655/1280*screen_width, 217/720*screen_height, image=hall_button_image)
canvas.tag_bind(hall_button, "<Button-1>", open_hall_window)

def open_room_window(event):
    subprocess.Popen(["python", "Level_5/Room.py"])
    root.destroy()

room_button_image = ImageTk.PhotoImage(Image.open("Level_5/Image/Room_Button.png"))
room_button = canvas.create_image(211/1280*screen_width, 367/720*screen_height, image=room_button_image)
canvas.tag_bind(room_button, "<Button-1>", open_room_window)

root.mainloop()