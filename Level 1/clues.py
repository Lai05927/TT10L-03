import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

clues_image = Image.open("Level 1\Level 1 image\clues_image.png")
clues_photo = ImageTk.PhotoImage(clues_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=clues_photo)


def back(event):
    subprocess.Popen(['python','Level 1/story 7.py'])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_photo = ImageTk.PhotoImage(back_image)
back_btn = canvas.create_image(90,50,image=back_photo)
canvas.tag_bind(back_btn,"<Button-1>",back)
    
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/answer.py'])
    root.destroy()
   
#Question1    
hint_button_image1 = Image.open("Image/button_is-mom-dead (2).png")
hint_button_photo1 = ImageTk.PhotoImage(hint_button_image1)
hint_button1 = canvas.create_image(320,150,image=hint_button_photo1)
canvas.tag_bind(hint_button1,"<Button-1>",open_hints_window)


#question 2
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/answer2.py'])
    root.destroy()
   
hint_button_image2 = Image.open("Image/button_did-mom-go-out-at-night (3).png")
hint_button_photo2 = ImageTk.PhotoImage(hint_button_image2)
hint_button2 = canvas.create_image(960,150,image=hint_button_photo2)
canvas.tag_bind(hint_button2,"<Button-1>",open_hints_window)


#question 3
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/gethits.py'])
    root.destroy()
   
hint_button_image3 = Image.open("Image/button_is-the-daughter-a-murderer (4).png")
hint_button_photo3 = ImageTk.PhotoImage(hint_button_image3)
hint_button3 = canvas.create_image(970,300,image=hint_button_photo3)
canvas.tag_bind(hint_button3,"<Button-1>",open_hints_window)


#Question 4
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/answer4.py'])
    root.destroy()
   
hint_button_image4 = Image.open("Image/button_daughter-really-push-it-to-her-mother (2).png")
hint_button_photo4 = ImageTk.PhotoImage(hint_button_image4)
hint_button4 = canvas.create_image(600,450,image=hint_button_photo4)
canvas.tag_bind(hint_button4,"<Button-1>",open_hints_window)


#Question 5
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/answer5.py'])
    root.destroy()
   
hint_button_image5 = Image.open("Image/button_daughter-have-mentally-problem (2).png")
hint_button_photo5= ImageTk.PhotoImage(hint_button_image5)
hint_button5 = canvas.create_image(320,300,image=hint_button_photo5)
canvas.tag_bind(hint_button5,"<Button-1>",open_hints_window)

#Question 6
def open_hints_window(event):
    subprocess.Popen(['python','Level 1/answer6.py'])
    root.destroy()
   
hint_button_image6 = Image.open("Image/button_did-mother-wear-her-daughters-dress-and-use-her-perfume (1).png")
hint_button_photo6 = ImageTk.PhotoImage(hint_button_image6)
hint_button6 = canvas.create_image(600,590,image=hint_button_photo6)
canvas.tag_bind(hint_button6,"<Button-1>",open_hints_window)

root.mainloop()