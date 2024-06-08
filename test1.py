import hashlib
import json
import tkinter as tk
from tkinter import messagebox

# Helper functions for user management
def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open('users.txt', 'a') as file:
        file.write(f"{username},{hashed_password}\n")

def user_exists(username):
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                stored_username, _ = line.strip().split(',')
                if stored_username == username:
                    return True
    except FileNotFoundError:
        return False
    return False

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
                if stored_username == username and stored_password == hashed_password:
                    return True
    except FileNotFoundError:
        pass
    return False

def save_user_data(username, data):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}

    user_data[username] = data

    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)

def load_user_data(username):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
            return user_data.get(username, {})
    except FileNotFoundError:
        return {}

# Tkinter GUI application
class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login System")
        
        self.username_label = tk.Label(root, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack()
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if user_exists(username):
            messagebox.showerror("Error", "Username already exists")
        else:
            register_user(username, password)
            messagebox.showinfo("Success", "User registered successfully")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if login_user(username, password):
            user_data = load_user_data(username)
            messagebox.showinfo("Success", f"Login successful! Your data: {user_data}")
            self.show_user_data_window(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_user_data_window(self, username):
        data_window = tk.Toplevel(self.root)
        data_window.title("User Data")

        data_label = tk.Label(data_window, text=f"Welcome {username}! Your data:")
        data_label.pack()

        self.data_entry = tk.Entry(data_window)
        self.data_entry.pack()

        save_button = tk.Button(data_window, text="Save Data", command=lambda: self.save_data(username))
        save_button.pack()

    def save_data(self, username):
        data = self.data_entry.get()
        save_user_data(username, data)
        messagebox.showinfo("Success", "User data saved successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()
