import tkinter as tk
import random
from PIL import Image, ImageTk
import subprocess
import tkinter.messagebox as messagebox
import pygame
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("MCQ")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

bg_image = Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

def toggle_mute(event):
    global muted
    muted = not muted
    if muted:
        canvas.itemconfig(mute_button, image=mute_icon)
        pygame.mixer.music.set_volume(0)
    else:
        canvas.itemconfig(mute_button, image=unmute_icon)
        pygame.mixer.music.set_volume(1)

pygame.mixer.init()
pygame.mixer.music.load("Level_5/Image/mp3 6.mp3")

mute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Muted.jpg")).resize((50, 50)))
unmute_icon = ImageTk.PhotoImage((Image.open("Level_5/Image/Unmute.png")).resize((50, 50)))

muted = False
mute_button = canvas.create_image(1230, 30, image=unmute_icon)
canvas.tag_bind(mute_button, "<Button-1>", toggle_mute)

pygame.mixer.music.play(-1)

def back(event):
    subprocess.Popen(["python","Level_5.py"])
    root.destroy()

back_image = Image.open("Image/Back.png").resize((45,45))
back_image_tk = ImageTk.PhotoImage(back_image)
back_button = canvas.create_image(80/1280*screen_width, 30/720*screen_height, image=back_image_tk)
canvas.tag_bind(back_button, "<Button-1>", back)

def home(event):
    if messagebox.askokcancel("Confirm", "Do you want to proceed to the home page? Your progress will not be saved."):
        subprocess.Popen(["python", "Index.py"])
        root.destroy()

home_image = Image.open("Image/Home.png").resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>", home)

# Questions and answers
questions = [
    ("Murder method and plan?", "Manipulating medication", ["Accidental death", "Poison", "Hired killers"]),
    ("Is this a personal crime or a organized gang crime?", "Gang crime, one mastermind, one accomplice and one cover-up", ["Gang crime, one mastermind and one accomplice", "Gang crime, one mastermind and one cover-up", "Individual crime, only one mastermind"]),
    ("Who is the mastermind?", "Chandra", ["Emberly", "Heidi", "Kiara", "Reynold"]),
    ("What is the motion of Chandra", "Hatred towards Baldric", ["Revenge for past grievances", "Family pressure or influence", "Financial gain"]),
    ("Who is the accomplice?", "Heidi", ["Mary", "Emberly", "Kiara","Mr. Smith"]),
    ("What is the motion of Heidi", "Resentment towards Baldric", ["Psychological instability", "Family pressure or influence", "Resolving internal family conflicts"]),
    ("Who is the cover-up?", "Reynold", ["Mary", "Kiara", "Mr. Smith", "Jane"]),
    ("What is the motion of Reynold", "Protecting family members", ["Jealousy or rivalry", "Inheritance disputes", "Revenge for past grievances"]),
]

question_index = 0
score = 0

# Function to display the question
def display_question():
    global question_index, var
    if question_index < len(questions):
        q, a, options = questions[question_index]
        options = [a] + options
        random.shuffle(options)
        question_text.set(q)
        for i, btn in enumerate(option_buttons):
            btn.config(text=options[i], value=options[i])
        var.set("")
    else:
        end_quiz()

# Function to check the answer
def check_answer():
    global question_index, score
    selected_answer = var.get()
    correct_answer = questions[question_index][1]
    if selected_answer == correct_answer:
        score += 1
        question_index += 1
        display_question()
        messagebox.showinfo("Correct", "Well done! You are one step closer to solving the mystery.")
    else:
        messagebox.showwarning("Incorrect", "That's not the correct answer. Try again! Kindly return back to check the hints again.")

# Function to end the quiz
def end_quiz():
    messagebox.showinfo("Quiz Finished", f"Your score: {score}/{len(questions)}")
    root.quit()

# Create a Tkinter Label widget for the question
question_text = tk.StringVar()
question_label = tk.Label(root, textvariable=question_text, font=("Arial", 14), wraplength=600)
question_label.place(relx=0.5, rely=0.25, anchor="center")

# Set initial question text
question_text.set("")

# Create widgets on the canvas
options_frame = tk.Frame(root)
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_answer)

canvas.create_window(screen_width / 2, screen_height / 2, window=options_frame)
canvas.create_window(screen_width / 2, screen_height * 3 / 4, window=submit_button)

# Create option buttons inside the options frame
var = tk.StringVar()
option_buttons = [tk.Radiobutton(options_frame, text="", font=("Arial", 14), variable=var, value="") for _ in range(4)]
for btn in option_buttons:
    btn.pack(anchor="w")

# Display the first question
display_question()

# Start the Tkinter event loop
root.mainloop()
