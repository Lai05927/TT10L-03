from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()
root.title("Level 1")
root.geometry("1280x720+0+0")

bg_image = Image.open("Image/Level_1/Background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

def open_hall_window():
    hall_window = tk.Toplevel(root)
    hall_window.title("Hall")
    hall_window.geometry(root.geometry())
    tk.Label(hall_window, text="This is a new window!").pack()

hall_button_image = Image.open("Image/Level_1/Hall_Button.png")
hall_button_photo = ImageTk.PhotoImage(hall_button_image)
hall_button = tk.Button(root, image=hall_button_photo, command=open_hall_window)
hall_button.photo = hall_button_photo
hall_button.place(x=540, y=150)

def open_room_window():
    room_window = tk.Toplevel(root)
    room_window.title("Room")
    room_window.geometry(root.geometry())
    tk.Label(room_window, text="This is a new window!").pack()

room_button_image = Image.open("Image/Level_1/Room_Button.png")
room_button_photo = ImageTk.PhotoImage(room_button_image)
room_button = tk.Button(root, image=room_button_photo, command=open_room_window)
room_button.photo = room_button_photo
room_button.place(x=20, y=200)

root.mainloop()