import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
root = tk.Tk()
root.title("")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')
import pygame

#background music
import background_music
background_music.play_music("Level_1\Level 1 image\dark-ambient-horror-cinematic-halloween-atmosphere-scary-118585.mp3")


#sound effect
pygame.mixer.init()
button_click_sound = pygame.mixer.Sound("Level_1/Level 1 image/mixkit-game-ball-tap-2073.wav")# Load sound effects

def play_sound(sound):
    pygame.mixer.Sound.play(sound) # Function to play sound effects





user_score = 0

# Function to update the score label
def update_score_label():
    score_label.config(text=f"Score: {user_score}")

# Function to display message box for correct answer and proceed to next question
def handle_correct_answer(next_question):
    global user_score
    user_score += 1
    messagebox.showinfo("Correct", "You have answered correctly!")
    update_score_label()
    next_question()

# Function to display message box for incorrect answer
def handle_incorrect_answer(next_question):
    global user_score
    user_score += -1
    messagebox.showerror("Incorrect", "Sorry, that's not the correct answer.")
    update_score_label()
    next_question()

# Function to handle option selection
def handle_option(option_number, next_question):
    if option_number == 1:
        handle_correct_answer(next_question)
    else:
        handle_incorrect_answer(next_question)

def question1():
    play_sound(button_click_sound) 
    global text_item, option_button_photo1, option_button_photo2, option_button_photo3
    ques_text = 'Q1. Who dresses her clothes and uses her perfume?'

    option_image1 = Image.open("Level_1/Level 1 image/button_herself (2).png")
    option_image2 = Image.open("Level_1/Level 1 image/button_mother.png")
    option_image3 = Image.open("Level_1/Level 1 image/button_nobody.png")

    option_button_photo1 = ImageTk.PhotoImage(option_image1)
    option_button_photo2 = ImageTk.PhotoImage(option_image2)
    option_button_photo3 = ImageTk.PhotoImage(option_image3)

    text_item = canvas.create_text(screen_width / 2, screen_height / 2.8, anchor='center', text=ques_text, fill='white', font=('Comic Sans MS', 24, 'bold'))

    option_button1 = canvas.create_image(350, 470, image=option_button_photo1, tags="option")# tags=delete previous option
    canvas.tag_bind(option_button1, "<Button-1>", lambda event: handle_option(1, question2))

    option_button2 = canvas.create_image(650, 470, image=option_button_photo2, tags="option")
    canvas.tag_bind(option_button2, "<Button-1>", lambda event: handle_option(2, question2))

    option_button3 = canvas.create_image(950, 470, image=option_button_photo3, tags="option")
    canvas.tag_bind(option_button3, "<Button-1>", lambda event: handle_option(3, question2))

def question2():
    play_sound(button_click_sound) 
    global text_item, option_button_photo4, option_button_photo5, option_button_photo6

    ques_text = 'Q2. Why did the daughter argue with her mother?'
    option_image4 = Image.open("Level_1/Level 1 image/button_mother-has-a-mental-problem.png")
    option_image5 = Image.open("Level_1/Level 1 image/button_cause-mother-use-her-perfume-and-clothes.png")
    option_image6 = Image.open("Level_1/Level 1 image/button_daughter-has-a-mental-problem.png")

    option_button_photo4 = ImageTk.PhotoImage(option_image4)
    option_button_photo5 = ImageTk.PhotoImage(option_image5)
    option_button_photo6 = ImageTk.PhotoImage(option_image6)

    canvas.itemconfig(text_item, text=ques_text)

    canvas.delete("option")

    option_button4 = canvas.create_image(630, 410, image=option_button_photo4, tags="option")
    canvas.tag_bind(option_button4, "<Button-1>", lambda event: handle_option(2, question3))

    option_button5 = canvas.create_image(650, 600, image=option_button_photo5, tags="option")
    canvas.tag_bind(option_button5, "<Button-1>", lambda event: handle_option(2, question3))

    option_button6 = canvas.create_image(630, 500, image=option_button_photo6, tags="option")
    canvas.tag_bind(option_button6, "<Button-1>", lambda event: handle_option(1, question3))

def question3():
    play_sound(button_click_sound) 
    global text_item, option_button_photo7, option_button_photo8, option_button_photo9

    ques_text = 'Q3. What did her daughter push?'
    option_image7 = Image.open("Level_1/Level 1 image/button_mirror.png")
    option_image8 = Image.open("Level_1/Level 1 image/button_her-mother.png")
    option_image9 = Image.open("Level_1/Level 1 image/button_her-mother.png")

    option_button_photo7 = ImageTk.PhotoImage(option_image7)
    option_button_photo8 = ImageTk.PhotoImage(option_image8)
    option_button_photo9 = ImageTk.PhotoImage(option_image9)

    canvas.itemconfig(text_item, text=ques_text) #更新

    canvas.delete("option")

    option_button7 = canvas.create_image(350, 470, image=option_button_photo7, tags="option")
    canvas.tag_bind(option_button7, "<Button-1>", lambda event: handle_option(1, question4))

    option_button8 = canvas.create_image(650, 470, image=option_button_photo8, tags="option")
    canvas.tag_bind(option_button8, "<Button-1>", lambda event: handle_option(2, question4))

    option_button9 = canvas.create_image(950, 470, image=option_button_photo9, tags="option")
    canvas.tag_bind(option_button9, "<Button-1>", lambda event: handle_option(2,question4 ))

def question4():
    play_sound(button_click_sound)
    global text_item, option_button_photo10, option_button_photo11, option_button_photo12, show_the_truth_btn, show_the_truth_image, question_4_answered
    ques_text = 'Q4. Whose blood is that?'

    option_image10 = Image.open("Level_1/Level 1 image/button_nobody.png")
    option_image11 = Image.open("Level_1/Level 1 image/button_her-mother.png")
    option_image12 = Image.open("Level_1/Level 1 image/button_herself (2).png")

    option_button_photo10 = ImageTk.PhotoImage(option_image10)
    option_button_photo11 = ImageTk.PhotoImage(option_image11)
    option_button_photo12 = ImageTk.PhotoImage(option_image12)
    canvas.itemconfig(text_item, text=ques_text)

    canvas.delete("option")
    option_button10 = canvas.create_image(350, 470, image=option_button_photo10, tags="option")
    canvas.tag_bind(option_button10, "<Button-1>", lambda event: handle_option(2, lambda: end_questions()))

    option_button11 = canvas.create_image(650, 470, image=option_button_photo11, tags="option")
    canvas.tag_bind(option_button11, "<Button-1>", lambda event: handle_option(2, lambda: end_questions()))

    option_button12 = canvas.create_image(950, 470, image=option_button_photo12, tags="option")
    canvas.tag_bind(option_button12, "<Button-1>", lambda event: handle_option(1, lambda: end_questions()))

    show_the_truth_image = Image.open("Level_1/Level 1 image/button_show-the-truth.png")
    show_the_truth_btn = ImageTk.PhotoImage(show_the_truth_image)
    show_the_truth_btn1 = canvas.create_image(1100, 600, image=show_the_truth_btn)
    canvas.tag_bind(show_the_truth_btn1, "<Button-1>", check_question_4_answered)

def check_question_4_answered(event):
    if question_4_answered:
        show_the_truth()
    else:
        messagebox.showwarning("Warning", "You must answer question 4 before viewing the truth.")

def show_the_truth():
    subprocess.Popen(["python", "Level_1/show_the_truth.py"])
    root.destroy()

def end_questions():
    global question_4_answered
    question_4_answered = True
    messagebox.showinfo("End", "End of questions")


# Create a label to display the user's score
score_label = tk.Label(root, text=f"Score: {user_score}", font=('Comic Sans MS', 18))
score_label.pack()

# Display question image and text
ques_image = Image.open("Level_1/Level 1 image/clues_image.png")
ques_photo = ImageTk.PhotoImage(ques_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width / 2, screen_height / 2, anchor="center", image=ques_photo)

shadow_image = ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
shadow = canvas.create_image(screen_width / 10, screen_height / 4.5, anchor="nw", image=shadow_image)



# Start with the first question
question1()



def home(event):
    play_sound(button_click_sound)
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)


def back(event):
    play_sound(button_click_sound)
    subprocess.Popen(['python','Level_1/Level_1.py'])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_photo = ImageTk.PhotoImage(back_image)
back_btn = canvas.create_image(120,52,image=back_photo)
canvas.tag_bind(back_btn,"<Button-1>",back)


root.mainloop()
