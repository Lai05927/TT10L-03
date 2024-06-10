from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import pygame
root = tk.Tk()
root.title("LEVEL 1")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')


#background music
import background_music
background_music.play_music("Level 1/Level 1 image/creepy-music-box-halloween-music-horror-scary-spooky-dark-ambient-118577.mp3")



#sound effect
pygame.mixer.init()
button_click_sound = pygame.mixer.Sound("Level 1/Level 1 image/mixkit-game-ball-tap-2073.wav")

def play_sound(sound):
    pygame.mixer.Sound.play(sound)






#Main window background

bg_image = Image.open("Level 1/Level 1 image/story 1 background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)



# Level  Title
title_txt = "Level 1 : The Half Bottle of Perfume"
title_count = 0
title_text = ""
title_label = canvas.create_text(600, 100, text=title_txt, font=("Comic Sans MS", 40, "bold"), fill="yellow")




# Opening Text
opening_lines = ["Recently, my mother has been acting strangely. Not only did she secretly use my perfume and wear my clothes, but she also goes out late at night. The other day,I couldn't help but confront her, and we got into an argument. In the heat of the moment,I accidentally pushed her to the ground. I rushed to help her up, but only to find my hands covered in blood."]


opening_count = 0
opening_text = ""
opening_label = canvas.create_text(screen_width/2, screen_height/2, text=opening_text, font=("Comic Sans MS", 27), fill="white", width=screen_width-100)






#animate_text()
def animate_text():
    global opening_count, opening_text
    if opening_count < len(opening_lines):
        line = opening_lines[opening_count]
        if len(opening_text) < len(line):
            opening_text += line[len(opening_text)]
            canvas.itemconfig(opening_label, text=opening_text)
            root.after(50, animate_text)  # Adjust the speed of typing here
        else:
            
           
            opening_count += 1
            root.after(1000, animate_text)  # Adjust the pause between lines here
    else:
        # Animation finished
        pass



def start_animation():
    animate_text()
# Call start_animation() after main window is displayed
root.after(100, start_animation)






#button

def home(event):
    play_sound(button_click_sound)  
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)



def question_btn(event):
    play_sound(button_click_sound)  
    subprocess.Popen(['python','Level 1/clues.py'])
    root.destroy()
   
question_button_image1 = Image.open("Level 1/Level 1 image/button_question (1).png")
question_photo1 = ImageTk.PhotoImage(question_button_image1)
question_button1 = canvas.create_image(1100,555,image=question_photo1)
canvas.tag_bind(question_button1,"<Button-1>",question_btn)





def answer_question(event):
    play_sound(button_click_sound)  
    subprocess.Popen(['python','Level 1/question.py'])
    root.destroy()
   
answer_question_button_image1 = Image.open("Level 1/Level 1 image/button_answer-question.png")
answer_question_photo1 = ImageTk.PhotoImage(answer_question_button_image1)
answer_question_button1 = canvas.create_image(1100,640,image=answer_question_photo1)
canvas.tag_bind(answer_question_button1,"<Button-1>",answer_question)
root.mainloop()









root.mainloop()