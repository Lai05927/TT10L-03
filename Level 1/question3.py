import tkinter as tk
from PIL import Image, ImageTk
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')
from tkinter import messagebox

ques_image = Image.open("Level 1\Level 1 image\clues_image.png")
ques_photo = ImageTk.PhotoImage(ques_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=ques_photo)

shadow_image=ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
shadow=canvas.create_image(screen_width/10, screen_height/3.5, anchor="nw", image=shadow_image)
ques_text=' Q3. What her daughter pushed ?'
text_item=canvas.create_text(screen_width/2,screen_height/2.4, anchor='center', text=ques_text, fill='white', font=('Comic Sans MS', 24, 'bold'))
index = 0

def slider():
    global index,ques_text 
    
    if index > len(ques_text):
        index = -1
        ques_text =ques_text
    else:
        canvas.itemconfig(text_item, text=ques_text[:index])
        index += 1
        root.after(40, slider)


    
slider()




def handle_correct_answer():
    messagebox.showinfo("Correct","You have answered correctly!")
    subprocess.Popen(['python','Level 1/question3.py'])
    root.destroy()

def handle_incorrect_answer():
    messagebox.showerror("Incorrect", "Sorry, that's not the correct answer.")

def handle_option(option_number):
    if option_number==1:
        handle_correct_answer()
    else:
        handle_incorrect_answer()


#1
def ques_opions(event):
    subprocess.Popen(['python','Level 1/final answer.py'])
    root.destroy()
   
ques_image1 = Image.open("Level 1/Level 1 image/button_mirror.png")
ques_button_photo1 = ImageTk.PhotoImage(ques_image1)
ques_button1= canvas.create_image(350,500,image=ques_button_photo1)
canvas.tag_bind(ques_button1,"<Button-1>",lambda event:handle_option(1) )

#2
def ques_opions(event):
    subprocess.Popen(['python','Level 1/question4.py'])
    root.destroy()
   
ques_image2 = Image.open("Level 1/Level 1 image/button_her-mother.png")
ques_button_photo2= ImageTk.PhotoImage(ques_image2)
ques_button2= canvas.create_image(650,500,image=ques_button_photo2)
canvas.tag_bind(ques_button2,"<Button-1>",lambda event:handle_option(2) )


#3
def ques_opions(event):
    subprocess.Popen(['python','Level 1/question4.py'])
    root.destroy()
   
ques_image3 = Image.open("Level 1/Level 1 image/button_nobody (1).png")
ques_button_photo3= ImageTk.PhotoImage(ques_image3)
ques_button3= canvas.create_image(950,500,image=ques_button_photo3)
canvas.tag_bind(ques_button3,"<Button-1>",lambda event:handle_option(2) )




root.mainloop()