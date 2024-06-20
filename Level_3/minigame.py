import random
import tkinter as tk
from tkinter import messagebox
import subprocess
import pygame

pygame.mixer.init()





def bg_sound():
    sound_file = r"Level_3\Image\let-the-mystery-unfold-122118.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)#play continuously 

# List of words to choose from
words = ["secret", "mystery", "victim", "puzzle", "quandary", "enigma", "murderer", "brainteaser", "challenge", "solve"]

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def start_game():
    global word, scrambled_word
    word = random.choice(words)
    scrambled_word = scramble_word(word)
    scrambled_label.config(text=f"Scrambled word: {scrambled_word}")

def check_guess():
    user_guess = guess_entry.get().strip().lower()
    if user_guess == word:
        messagebox.showinfo("Result", "Correct! Well done!")
        subprocess.Popen(["python", "Level_3/Clues.py"])
        root.destroy()
    else:
        messagebox.showinfo("Result", f"Sorry, that's incorrect. Try again.")
        guess_entry.delete(0, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Word Guessing")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

# Load the background image
bg_image = tk.PhotoImage(file=r"Level_3\Image\book(1).png")
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.create_image(screen_width / 2, screen_height / 2, anchor='center', image=bg_image)

# Create and place widgets on the canvas
title_label = tk.Label(root, text="Guess the word to get the hints", font=("Helvetica", 20, "bold"), bg="white")
canvas.create_window(screen_width / 2, 50, window=title_label)

scrambled_label = tk.Label(root, text="Scrambled word:", font=("Helvetica", 16), bg="white")
canvas.create_window(screen_width / 2, 300, window=scrambled_label)

guess_entry = tk.Entry(root, font=("Helvetica", 16))
canvas.create_window(screen_width / 2, 350, window=guess_entry)

guess_button = tk.Button(root, text="Guess", command=check_guess, font=("Helvetica", 16))
canvas.create_window(screen_width / 2, 400, window=guess_button)

# Start the game
start_game()

bg_sound()

# Run the main event loop
root.mainloop()

