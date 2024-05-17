import tkinter as tk
from PIL import Image, ImageTk
room_window = tk.Tk()
room_window.title("Room")
screen_width = room_window.winfo_screenwidth()
screen_height = room_window.winfo_screenheight()
room_window.geometry(f"{screen_width}x{screen_height}")
room_window.state('zoomed')

bg_image = Image.open("Level_5/Image/Room 4.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(room_window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

room_window.mainloop()