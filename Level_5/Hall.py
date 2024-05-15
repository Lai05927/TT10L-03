import tkinter as tk
from PIL import Image, ImageTk
hall_window = tk.Tk()
hall_window.title("Hall")
hall_window.geometry("1280x720+0+0")

bg_image = Image.open("Level_5/Image/Hall 2.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(hall_window, width=1280, height=720)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

hall_window.mainloop()