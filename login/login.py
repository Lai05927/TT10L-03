import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os
import subprocess

# Filename where to store user data
USER_DATA_FILE = 'user_data.json'

# Load user data from file
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

# Save user data to file
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file)

# User data dictionary
user_data = load_user_data()

# Initialize main window for login/signup
root = tk.Tk()
root.title("Login System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')

bg_image = Image.open("Image\login.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(screen_width / 2, screen_height / 2, anchor="center", image=bg_photo)

# Frames for login and signup
login_frame = tk.Frame(canvas, bg="white", width=800, height=600)
signup_frame = tk.Frame(canvas, bg="white", width=800, height=600)

def show_frame(frame):
    frame.tkraise()

# Place frames on the canvas
login_window = canvas.create_window(screen_width / 2, screen_height / 2, window=login_frame, anchor="center")
signup_window = canvas.create_window(screen_width / 2, screen_height / 2, window=signup_frame, anchor="center")

# Update canvas to ensure frames are resized and displayed correctly
canvas.update_idletasks()


def update_current_user(username):
    user_data = load_user_data()
    user_data["current_user"] = username
    save_user_data(user_data)

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username in user_data and user_data[username]['password'] == password:
        level_num = user_data[username]['level']
        update_current_user(username)
        if level_num == 0:
            messagebox.showinfo("Login Successful", f"Welcome {username}! Before we start, let me briefly introduce our game.")
            root.destroy()
            subprocess.Popen(["python", "Tutorial/tutorial.py"])
        else:
            messagebox.showinfo("Login Successful", f"Welcome back {username}! You were on level {user_data[username]['level']}.")
            root.destroy()
            file_to_open = f"Level_{level_num}/Level_{level_num}.py"
            subprocess.Popen(["python", file_to_open, username])

    else:
        messagebox.showerror("Error", "User doesn't exist or wrong password")

def signup():
    username = new_username_entry.get().strip()
    password = new_password_entry.get().strip()

    if username in user_data:
        messagebox.showerror("Error", "User already exists")
    else:
        user_data[username] = {'password': password, 'level': 0}
        save_user_data(user_data)
        messagebox.showinfo("Signup Successful", "User created successfully! You can now login.")
        show_frame(login_frame)

# Login frame widgets
tk.Label(login_frame, text="Login", font=("Arial", 26)).pack(padx=40,pady=20)
tk.Label(login_frame, text="Username",font=("Arial",10)).pack(padx=40,pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(padx=40,pady=5)
tk.Label(login_frame, text="Password",font=("Arial",10)).pack(padx=40,pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(padx=40,pady=5)
tk.Button(login_frame, text="Login", command=login).pack(padx=40,pady=10)
tk.Button(login_frame, text="Sign Up", command=lambda: show_frame(signup_frame)).pack(padx=40,pady=10)

# Signup frame widgets
tk.Label(signup_frame, text="Sign Up", font=("Arial", 26)).pack(padx=40,pady=20)
tk.Label(signup_frame, text="Username",font=("Arial",10)).pack(padx=40,pady=5)
new_username_entry = tk.Entry(signup_frame)
new_username_entry.pack(padx=40,pady=5)
tk.Label(signup_frame, text="Password",font=("Arial",10)).pack(padx=40,pady=5)
new_password_entry = tk.Entry(signup_frame, show="*")
new_password_entry.pack(padx=40,pady=5)
tk.Button(signup_frame, text="Sign Up", command=signup).pack(padx=40,pady=10)
tk.Button(signup_frame, text="Back to Login", command=lambda: show_frame(login_frame)).pack(padx=40,pady=10)

# Start with login frame
show_frame(login_frame)

root.mainloop()






