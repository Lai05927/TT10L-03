import tkinter as tk
from tkinter import ttk

class SlideLabel(tk.Frame):
    def _init_(self, master, text):
        super()._init_(master)
        
        self.label = ttk.Label(self, text=text, style="TLabel")
        self.label.pack(fill='x')
        
        self.bind("<Enter>", self.slide_in)
        self.bind("<Leave>", self.slide_out)
        
        self.slide_direction = -1
        self.slide_length = 100
        self.slide_speed = 5

    def slide_in(self, event):
        self.slide_direction = 1
        self.after(self.slide_speed, self.animate_slide)

    def slide_out(self, event):
        self.slide_direction = -1
        self.after(self.slide_speed, self.animate_slide)

    def animate_slide(self):
        current_height = self.winfo_height()
        target_height = self.slide_length if self.slide_direction == 1 else 0
        
        if current_height == target_height:
            return
        
        new_height = current_height + self.slide_direction
        self.configure(height=new_height)
        self.update()
        
        self.after(self.slide_speed, self.animate_slide)


def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure("TLabel", background="white")
    
    button = ttk.Button(root, text="Hover Over Me")
    button.pack(pady=20)

    label_frame = SlideLabel(root, "I appear and disappear with slide animation")
    label_frame.pack(fill='x')

    root.mainloop()

if __name__ == "_main_":
    main()