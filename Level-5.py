from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()
root.title("Level 1")
root.geometry("1280x720+0+0")

bg_image = Image.open("Level_1/Image/Background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

def open_hall_window(event):
    hall_window = tk.Toplevel(root)
    hall_window.title("Hall")
    hall_window.geometry(root.geometry())
    tk.Label(hall_window, text="This is a new window!").pack()

hall_button_image = ImageTk.PhotoImage(Image.open("Level_1/Image/Hall_Button.png"))
hall_button = canvas.create_image(687, 240, image=hall_button_image)
canvas.tag_bind(hall_button, "<Button-1>", open_hall_window)

def open_room_window(event):
    room_window = tk.Toplevel(root)
    room_window.title("Room")
    room_window.geometry(root.geometry())
    tk.Label(room_window, text="This is a new window!").pack()

room_button_image = ImageTk.PhotoImage(Image.open("Level_1/Image/Room_Button.png"))
room_button = canvas.create_image(243, 390, image=room_button_image)
canvas.tag_bind(room_button, "<Button-1>", open_room_window)

root.mainloop()