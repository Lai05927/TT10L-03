import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
from tkinter import messagebox


#answer background
board_image = Image.open("Level 1/Level 1 image/blank blackboard (1).jpg")
board_photo = ImageTk.PhotoImage(board_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2.3, anchor="center", image=board_photo)


question_txt = "5 + 5 x 5 + 5 = ?"
question_label = canvas.create_text(650, 240, text=question_txt, font=("Comic Sans MS", 35, "bold"), fill="WHITE")

#option1
def show_message(event):
    messagebox.showinfo("answer","ANSWER WRONG")

button_image= ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button (3).png"))
button=canvas.create_image(450,400, image=button_image)
canvas.tag_bind(button,"<Button-1>", show_message)


#option 3
def show_message(event):
    messagebox.showinfo("answer","ANSWER WRONG")

button_image3=ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button (4).png"))
button=canvas.create_image(890,400, image=button_image3)
canvas.tag_bind(button,"<Button-1>", show_message)

# option9
def show_message(event):
    messagebox.showinfo("answer","ANSWER CORRECT")

def navigate_to_answer_window3():
    subprocess.Popen(["python", "Level 1/answer3.py"])

    root.destroy() 

def show_message(event, is_correct):
    if is_correct:
        navigate_to_answer_window3()
    else:
        messagebox.showinfo("Answer", "Wrong Answer")
    
canvas.tag_bind(button, "<Button-1>", lambda event: show_message(event, True))




button_image2=ImageTk.PhotoImage(Image.open("Level 1/Level 1 image/button (5).png"))
button=canvas.create_image(670,400, image=button_image2)
canvas.tag_bind(button,"<Button-1>", show_message)








root.mainloop()
