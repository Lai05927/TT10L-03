import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


#answer background
board_image = Image.open("Level 1/Level 1 image/blackboard.jpeg")
board_photo = ImageTk.PhotoImage(board_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2.3, anchor="center", image=board_photo)


# answer1
answer1_txt = "       YES.Mom is dead     "
answer1_count = 0
answer1_text = ""
answer1_label = canvas.create_text(600, 300, text=answer1_txt, font=("Comic Sans MS", 40, "bold"), fill="brown")


def animate_text():
    global answer1_count, answer1_text
    if answer1_count < len(answer1_txt):
        answer1_text += answer1_txt[answer1_count]
        canvas.itemconfig(answer1_label, text=answer1_text)
        answer1_count += 1
        root.after(100, animate_text)  
    else:
        # Animation finished
        pass


animate_text()




root.mainloop()