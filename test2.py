import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Initialize game variables
min_value = 1
max_value = 999
target_number = random.randint(min_value, max_value)

# Function to check the user's guess
def check_guess(event=None):
    global min_value, max_value, target_number
    
    try:
        guess = int(entry.get())
        
        if guess < min_value or guess > max_value:
            result_label.config(text=f"Please enter a number between {min_value} and {max_value}.")
        elif guess < target_number:
            min_value = guess
            label.config(text=f"Guess a number between {min_value} and {max_value}:")
            result_label.config(text=f"{guess} is too low. Try again!")
        elif guess > target_number:
            max_value = guess
            label.config(text=f"Guess a number between {min_value} and {max_value}:")
            result_label.config(text=f"{guess} is too high. Try again!")
        else:
            messagebox.showinfo("Congratulations!", f"Correct! The number was {target_number}.")
            exit_game()
            
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Function to exit the game
def exit_game():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Number Guesser Game")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

bg_image = Image.open("Level_5/Image/Note_bg.jpg").resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

# Create UI elements on the canvas
label = tk.Label(root, text=f"Guess a number between {min_value} and {max_value}:", font=("Arial", 14))
entry = tk.Entry(root, font=("Arial", 14))
guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 14))
result_label = tk.Label(root, text="", font=("Arial", 14))

label_window = canvas.create_window(screen_width/2, screen_height/2 - 100, anchor="center", window=label)
entry_window = canvas.create_window(screen_width/2, screen_height/2, anchor="center", window=entry)
guess_button_window = canvas.create_window(screen_width/2, screen_height/2 + 100, anchor="center", window=guess_button)
result_label_window = canvas.create_window(screen_width/2, screen_height/2 + 200, anchor="center", window=result_label)

# Bind <Return> key to entry widget
entry.bind("<Return>", check_guess)

# Run the Tkinter event loop
root.mainloop()


