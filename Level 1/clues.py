import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()

def open_clues_window():
    global clues_bg_photo, back_photo
    new_window = tk.Toplevel(root)
    new_window.title("Clues")
    new_window.geometry(root.geometry())


    clues_bg_photo = tk.PhotoImage(file="Level 1/Level 1 image/level 1 hints bcg.png")
    clues_background_Label = tk.Label(new_window, image=clues_bg_photo, width=1280, height=720)
    clues_background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    clues_background_Label.image = clues_bg_photo


    back_image = Image.open("index image/Back.png")
    back_image = back_image.resize((100, 50), Image.ANTIALIAS)
    back_photo = ImageTk.PhotoImage(back_image)
    back_btn = tk.Button(new_window, image=back_photo, command=new_window.destroy,borderwidth=0)
    back_btn.place(x=110, y=50)
    
    

    mom_btn = tk.Button(new_window, text="Is mom dead", font=(24))
    mom_btn.place(x=100, y=50)

open_clues_btn = tk.Button(root, text="Open Clues Window", command=open_clues_window)
open_clues_btn.pack()
    

    

   
root.mainloop()