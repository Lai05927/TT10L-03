from PIL import Image, ImageTk
import tkinter as tk
import subprocess
import pyttsx3
import threading
import time


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


# Level  Title
title_txt = "Level 1 : The Half Bottle of Perfume"
title_count = 0
title_text = ""
title_label = canvas.create_text(600, 100, text=title_txt, font=("Comic Sans MS", 40, "bold"), fill="yellow")




# Opening Text
opening_lines = [
    "Recently, my mother has been acting strangely. Not only did she secretly use my perfume and wear my clothes, but she also goes out late at night. The other day,I couldn't help but confront her, and we got into an argument. In the heat of the moment,I accidentally pushed her to the ground. I rushed to help her up, but only to find my hands covered in blood."]

opening_count = 0
opening_text = ""
opening_label = canvas.create_text(screen_width/2, screen_height/2, text=opening_text, font=("Comic Sans MS", 20), fill="white", width=screen_width-100)


# Text to speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)#v1 is girl sound


def speak_text(text):
    print("Speaking:", text)
    engine.setProperty('rate', 150)  # Adjust the speaking rate (words per minute)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    time.sleep(0.5)
    engine.runAndWait()



#animate_text()
def animate_text():
    global opening_count, opening_text
    if opening_count < len(opening_lines):
        line = opening_lines[opening_count]
        if len(opening_text) < len(line):
            opening_text += line[len(opening_text)]
            canvas.itemconfig(opening_label, text=opening_text)
            root.after(100, animate_text)  # Adjust the speed of typing here
        else:
            t = threading.Thread(target=speak_text, args=(line,))
            t.start()
            opening_count += 1
            root.after(1000, animate_text)  # Adjust the pause between lines here
    else:
        # Animation finished
        pass







def start_animation():
    animate_text()
# Call start_animation() after main window is displayed
root.after(110, start_animation)




















def home(event):
    subprocess.Popen(["python","Index.py"])
    root.destroy()

home_image = (Image.open("Image/Home.png")).resize((45,45))
home_image_tk = ImageTk.PhotoImage(home_image)
home_button = canvas.create_image(30/1280*screen_width, 30/720*screen_height, anchor="nw", image=home_image_tk)
canvas.tag_bind(home_button, "<Button-1>",home)


#button


def open_clues_window(event):
    subprocess.Popen(["python","Level 1/clues.py"])
    root.destroy()

Question_btn = tk.Button(root, text="Question", font=('bold', 24))
Question_btn.place(x=1100, y=500)
Question_btn.bind("<Button-1>", open_clues_window)

Answer_btn=tk.Button(root,text="Answer\n Question",font=('bold',24))
Answer_btn.place(x=1100,y=580)
main_Frame=tk.Frame(root)
root.mainloop()