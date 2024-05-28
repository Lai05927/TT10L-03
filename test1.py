import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Initialize main window
note_window = tk.Tk()
note_window.title("Note")
screen_width = note_window.winfo_screenwidth()
screen_height = note_window.winfo_screenheight()
note_window.geometry(f"{screen_width}x{screen_height}")
note_window.state('zoomed')

# Load and set background image
bg_image = Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)

# Create main canvas
canvas = tk.Canvas(note_window, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

# Storyline text
storyline = "Recently, the Jellison family are having their family dinner. The next day, Baldric Jellison been found dead in his house."
canvas.create_text(screen_width/2, screen_height/4, text=storyline, font=("Arial", 16), fill="black", width=screen_width-100)

# Initialize frames
bottom_left_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(0, screen_height/2, anchor='nw', window=bottom_left_frame)

bottom_right_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(screen_width/2, screen_height/2, anchor='nw', window=bottom_right_frame)

# Initialize minigame count and text items
minigame_count = 0
text_items = []

for i in range(3):
    text_item = canvas.create_text(screen_width/4, screen_height/2 + (i * 50) + 50, text=f"Text {i+1}", font=("Arial", 24), fill="black", state='hidden')
    text_items.append(text_item)

# Function to proceed to minigame
def proceed_to_minigame():
    global minigame_count
    minigame_count += 1
    if minigame_count <= 3:
        canvas.itemconfigure(text_items[minigame_count - 1], state='normal')
    note_window.destroy()
    subprocess.run(["python", "Level_5/Minigame.py"])
    reopen_note_window()

# Function to proceed to MCQ
def proceed_to_mcq():
    note_window.destroy()
    subprocess.run(["python", "Level_5/Mcq.py"])

# Minigame button
minigame_button = tk.Button(bottom_left_frame, text="Proceed to Minigame", command=proceed_to_minigame, font=("Arial", 18))
minigame_button.pack(side='bottom', pady=20)

# MCQ button
mcq_button = tk.Button(bottom_right_frame, text="Proceed to MCQ", command=proceed_to_mcq, font=("Arial", 18))
mcq_button.pack(side='bottom', pady=20)

# Function to reopen the note window
def reopen_note_window():
    global note_window, canvas, text_items

    note_window = tk.Tk()
    note_window.title("Note")
    screen_width = note_window.winfo_screenwidth()
    screen_height = note_window.winfo_screenheight()
    note_window.geometry(f"{screen_width}x{screen_height}")
    note_window.state('zoomed')

    bg_image = Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height))
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(note_window, width=screen_width, height=screen_height)
    canvas.pack(fill='both', expand=True)
    canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

    storyline = "Recently, the Jellison family are having their family dinner. The next day, Baldric Jellison been found dead in his house."
    canvas.create_text(screen_width/2, screen_height/4, text=storyline, font=("Arial", 16), fill="black", width=screen_width-100)

    bottom_left_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
    canvas.create_window(0, screen_height/2, anchor='nw', window=bottom_left_frame)

    bottom_right_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
    canvas.create_window(screen_width/2, screen_height/2, anchor='nw', window=bottom_right_frame)

    global text_items
    text_items = []
    for i in range(3):
        text_item = canvas.create_text(screen_width/4, screen_height/2 + (i * 50) + 50, text=f"Text {i+1}", font=("Arial", 24), fill="black", state='hidden')
        text_items.append(text_item)

    minigame_button = tk.Button(bottom_left_frame, text="Proceed to Minigame", command=proceed_to_minigame, font=("Arial", 18))
    minigame_button.pack(side='bottom', pady=20)

    mcq_button = tk.Button(bottom_right_frame, text="Proceed to MCQ", command=proceed_to_mcq, font=("Arial", 18))
    mcq_button.pack(side='bottom', pady=20)

    canvas.image = bg_photo

    note_window.mainloop()

# Main entry point
if __name__ == "__main__":
    reopen_note_window()
