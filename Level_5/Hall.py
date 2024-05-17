import tkinter as tk
from PIL import Image, ImageTk
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

hall_window.mainloop()