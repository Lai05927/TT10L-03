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
answer6_txt = "  NO  "
answer6_count = 0
answer6_text = ""
answer6_label = canvas.create_text(600, 300, text=answer6_txt, font=("Comic Sans MS", 40, "bold"), fill="brown")


def animate_text():
    global answer6_count, answer6_text
    if answer6_count < len(answer6_txt):
        answer6_text += answer6_txt[answer6_count]
        canvas.itemconfig(answer6_label, text=answer6_text)
        answer6_count += 1
        root.after(100, animate_text)  
    else:
        # Animation finished
        pass

animate_text()

def home(event):
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)


def back(event):
    subprocess.Popen(['python','Level 1/story 7.py'])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_photo = ImageTk.PhotoImage(back_image)
back_btn = canvas.create_image(120,52,image=back_photo)
canvas.tag_bind(back_btn,"<Button-1>",back)


def back_to_clues(event):
    subprocess.Popen(["python","Level 1/clues.py"])
    root.destroy()

back_to_clues_image=Image.open("Image/button_back-to-clues (4).png")
back_to_clues_photo=ImageTk.PhotoImage(back_to_clues_image)
back_to_clues_btn=canvas.create_image(600,590,image=back_to_clues_photo)
canvas.tag_bind(back_to_clues_btn,"<Button-1>",back_to_clues)






root.mainloop()




root.mainloop()



root.mainloop()