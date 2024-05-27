import tkinter as tk
from PIL import Image, ImageTk

def proceed_to_minigame():
    global minigame_count
    minigame_count += 1
    if minigame_count <= 3:
        canvas.itemconfigure(text_items[minigame_count - 1], state='normal')

def proceed_to_mcq():
    pass

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

# Set background image on the canvas
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# Storyline text
storyline = "Recently, the Jellison family are having their family dinner. The next day, Baldric Jellison been found dead in his house."
canvas.create_text(screen_width/2, screen_height/4, text=storyline, font=("Arial", 16), fill="black", width=screen_width-100)

# Bottom left frame
bottom_left_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(0, screen_height/2, anchor='nw', window=bottom_left_frame)

# Texts to be displayed after mini-game
minigame_count = 0
text_items = []
for i in range(3):
    text_item = canvas.create_text(screen_width/4, screen_height/2 + (i * 30) + 50, text=f"Text {i+1}", font=("Arial", 24), fill="black", state='hidden')
    text_items.append(text_item)

# Minigame button
minigame_button = tk.Button(bottom_left_frame, text="Proceed to Minigame", command=proceed_to_minigame, font=("Arial", 18))
minigame_button.pack(side='bottom', pady=20)

# Bottom right frame
bottom_right_frame = tk.Frame(canvas, width=screen_width/2, height=screen_height/2, bg='', highlightthickness=0)
canvas.create_window(screen_width/2, screen_height/2, anchor='nw', window=bottom_right_frame)

# MCQ button
mcq_button = tk.Button(bottom_right_frame, text="Proceed to MCQ", command=proceed_to_mcq, font=("Arial", 18))
mcq_button.pack(side='bottom', pady=20)

# Keep a reference to the image to prevent garbage collection
canvas.image = bg_photo

note_window.mainloop()
