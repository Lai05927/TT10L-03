from PIL import Image, ImageTk
import tkinter as tk
import subprocess


def open_clues_window():
    # Function to open clues window
    pass

def go_to_home():
    # Function to return to home screen
    pass

root = tk.Tk()
root.title("LEVEL 7")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.state('zoomed')


#Main window background

bg_image = Image.open("Level 1/Level 1 image/story 1 background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

#new window
def open_clues_window():
    global clues_bg_photo
    new_window = tk.Toplevel(root)
    new_window.title("Clues")
    new_window.geometry(root.geometry())
    


    clues_bg_photo = tk.PhotoImage(file="Level 1/Level 1 image/clues_image.png")
    clues_background_Label = tk.Label(new_window, image=clues_bg_photo, width=1280, height=720)
    clues_background_Label.place(x=0, y=0, relwidth=1, relheight=1)
    clues_background_Label.image = clues_bg_photo


# Level 7 Title
title_txt = "Level 7 : The Half Bottle of Perfume"
title_count = 0
title_text = ""
#title_label = canvas.create_text(root, text=title_text, font=("Arial", 40, "bold"), bg="white", fg="black", highlightthickness=0)
title_label = canvas.create_text(600, 100, text=title_txt, font=("Arial", 40, "bold"), fill="yellow")
#title_label.pack(pady=100)



# Opening Text
opening_lines = [
    "Recently, my mother has been acting strangely. Not only did she secretly use my ",

    "perfume and wear my clothes, but she also goes out late at night.The other day, I",

    "couldn't help but confront her, and we got into an argument. In the heat of the moment,",

    "I accidentally pushed her to the ground. I rushed to help her up, but only to find my ",

    "hands covered in blood."]

opening_count = 0
opening_text = ""
opening_label = canvas.create_text(screen_width/2, screen_height/2, text=opening_text, font=("Arial", 20), fill="white")


def animate_text():
    global opening_count, opening_text
    if opening_count < len(opening_lines):
        opening_text += opening_lines[opening_count] + "\n"  # Add newline character to separate lines
        canvas.itemconfig(opening_label, text=opening_text)
        opening_count += 1
        root.after(600, animate_text)  # Adjust the speed of typing here
    else:
        # Animation finished
        pass

animate_text()






def home(event):
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)




#button

Question_btn=tk.Button(root, text="Question",font=('bold',24), command=open_clues_window)
Question_btn.place(x=1100,y=500)
Answer_btn=tk.Button(root,text="Answer\n Question",font=('bold',24))
Answer_btn.place(x=1100,y=580)
    



main_Frame=tk.Frame(root)


root.mainloop()