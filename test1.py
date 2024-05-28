import tkinter as tk
from PIL import Image, ImageTk
import subprocess
note_window = tk.Tk()
note_window.title("Note")
screen_width = note_window.winfo_screenwidth()
screen_height = note_window.winfo_screenheight()
note_window.geometry(f"{screen_width}x{screen_height}")
note_window.state('zoomed')

bg_image = (Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height)))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(note_window, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

storyline = "Recently, the Jellison family are having their family dinner. The next day, Baldric Jellison been found dead in his house."
canvas.create_text(screen_width/2, screen_height/4, text=storyline, font=("Arial", 16), fill="black", width=screen_width-100)

bottom_left_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(0, screen_height/2, anchor='nw', window=bottom_left_frame)
minigame_count=0

texts = ['as', 'bi', 'cd']

# Initialize the global variable minigame_count
minigame_count = 0

def proceed_to_minigame():
    global minigame_count
    if minigame_count < len(texts):
        canvas.itemconfigure(text_items[minigame_count], state='normal')
        minigame_count += 1

text_items = []
for i, text in enumerate(texts):
    text_item = canvas.create_text(screen_width/4, screen_height/2 + (i * 50) + 50, text=text, font=("Arial", 24), fill="black", state='hidden')
    text_items.append(text_item)
    
minigame_button = tk.Button(bottom_left_frame, text="Proceed to Minigame", command=proceed_to_minigame, font=("Arial", 18))
minigame_button.pack(side='bottom', pady=20)

def proceed_to_mcq():
    #subprocess.Popen(["python", "Level_5/Mcq.py"])
    pass

bottom_right_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(screen_width/2, screen_height/2, anchor='nw', window=bottom_right_frame)

mcq_button = tk.Button(bottom_right_frame, text="Proceed to MCQ", command=proceed_to_mcq, font=("Arial", 18))
mcq_button.pack(side='bottom', pady=20)

note_window.mainloop()