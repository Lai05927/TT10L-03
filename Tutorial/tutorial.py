from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import pyttsx3
import threading
import pygame


#background music
import background_music
background_music.play_music("Level 1/Level 1 image/walk-alone-dark-cinematic-music-horror-music-153445.mp3")



def read_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) >= 2:
        engine.setProperty('voice', voices[1].id)  # Use index 1 for the second voice (assuming it's a female voice)
    else:
        print("Not enough voices available.")
    engine.say(text)
    engine.runAndWait()


def show_next_text(event):
    global current_text_index
    if current_text_index < len(texts) - 1:
        current_text_index += 1
        canvas.itemconfig(text_item, text=texts[current_text_index])
        threading.Thread(target=read_text, args=(texts[current_text_index],)).start()
    else:
        root.unbind("<Button-1>")
        root.unbind("<Return>")
        show_choose_story_button()


def show_choose_story_button():
    choose_story_image = Image.open("Level 1/Level 1 image/button_choose-story.png")
    choose_story_image_tk = ImageTk.PhotoImage(choose_story_image)
    choose_story_button = canvas.create_image(screen_width / 3, screen_height / 1.2, anchor="nw", image=choose_story_image_tk)
    canvas.tag_bind(choose_story_button, "<Button-1>", choose_story)
    canvas.image = choose_story_image_tk  # Prevent image from being garbage collected


def choose_story(event):
    subprocess.Popen(["python", "Index.py"])
    root.destroy()



root = tk.Tk()
root.title("Night Trail Chronicle")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')





# Main window background
bg_image = Image.open("Image/Cover3.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width / 2, screen_height / 2, anchor="center", image=bg_photo)



# Shadow
shadow_image = ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
shadow = canvas.create_image(screen_width / 30, screen_height / 2.5, anchor="nw", image=shadow_image)



# Character
character_image = Image.open("Level 1/Level 1 image/file (3).png").resize((500, 500))
character_image_tk = ImageTk.PhotoImage(character_image)
character_button = canvas.create_image(screen_width / 1.6, screen_height / 3.7, anchor="nw", image=character_image_tk)



# Rules text
texts = [
    "\n Oh! hi,there \n",
    "Welcome to the Night Trail Chronicle",
    "Have you ever heard of a situation puzzle?",
    "For a situation puzzle, you'll be presented\n with a short story with very little details.",
    
    "Some levels require to playing minigames to get hints",
    "Then, it's up to you to ask questions \nin order to  figure out what's going on.",
    "You can only ask yes or no questions.",
    "For Level 2,you,ll be presented with a scene. ",
    "And you wanted to click each character to get hints .",
    "Then,you could answerd the MCQ Question.",
    "For Level 3,you'll be presented by 3 button.",
    "Which is Room , Hall and Note.",
    "In the scene of room and hall you can click\n the character or items that you are curious. ",
    "Then will comes out the scriot box\n and give the hints note."

]

current_text_index = 0
text_item = canvas.create_text(screen_width / 2.5, screen_height / 1.9, anchor='center', text=texts[current_text_index], fill='white', font=('Comic Sans MS', 24, 'bold'))

# Start reading the first text
threading.Thread(target=read_text, args=(texts[current_text_index],)).start()

root.bind("<Button-1>", show_next_text)
root.bind("<Return>", show_next_text)

root.mainloop()
