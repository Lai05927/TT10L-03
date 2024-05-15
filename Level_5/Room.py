import tkinter as tk
from PIL import Image, ImageTk
room_window = tk.Tk()
room_window.title("Room")
room_window.geometry("1280x720+0+0")

bg_image = Image.open("Level_5/Image/Room 4.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(room_window, width=1280, height=720)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

room_window.mainloop()