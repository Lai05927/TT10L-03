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




question_txt = "Daughter have mentally problem ?"
question_count = 0
question_text = ""
question_label = canvas.create_text(600, 240, text=question_txt, font=("Comic Sans MS", 35, "bold"), fill="Brown")



def animate_text():
    global question_count, question_text
    if question_count < len(question_txt):
        question_text += question_txt[question_count]
        canvas.itemconfig(question_label, text=question_text)
        question_count += 1
        root.after(50, animate_text)  
    else:
        # Animation finished
        pass
animate_text()


#hints button
def get_hints(event):
    subprocess.Popen(['python','Level 1/minigame.py'])
    root.destroy()
   
get_hints_image1= Image.open("Level 1/Level 1 image/button_hint.png")
get_hints_photo1 = ImageTk.PhotoImage(get_hints_image1)
get_hints_button1 = canvas.create_image(800,400,image=get_hints_photo1)
canvas.tag_bind(get_hints_button1,"<Button-1>",get_hints)


#back button

def back(event):
    subprocess.Popen(['python','Level 1/clues.py'])
    root.destroy()
   
back_button_image1 = Image.open("Level 1/Level 1 image/button_back.png")
back_button_photo1 = ImageTk.PhotoImage(back_button_image1)
back_button1 = canvas.create_image(400,400,image=back_button_photo1)
canvas.tag_bind(back_button1,"<Button-1>",back)














root.mainloop()