from PIL import Image, ImageTk
import tkinter as tk
import subprocess

main = tk.Tk()
main.title("Night Trail Chronicle")
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
main.geometry(f"{screen_width}x{screen_height}")
main.state('zoomed')

bg_image = Image.open("Image/Cover3.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
canvas = tk.Canvas(main, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2, screen_height/2, anchor="center", image=bg_photo)

shadow_image=ImageTk.PhotoImage(Image.open("Image/Shadow.png"))
shadow=canvas.create_image(screen_width/2, screen_height/3, anchor="center", image=shadow_image)
title_image=ImageTk.PhotoImage(Image.open("Image/Title.png"))
title=canvas.create_image(screen_width/2, screen_height/3, anchor="center", image=title_image)

level_image_file=["Image/Level_1.png","Image/Level_2.png","Image/Level_3.png",
                  "Image/Level_4.png","Image/Level_5.png","Image/Level_6.png",
                  "Image/Level_7.png"]
level_images = [ImageTk.PhotoImage(Image.open(img)) for img in level_image_file]
positions=  [(screen_width/4, screen_height/3), (screen_width/2, screen_height/3),
             (screen_width/4*3, screen_height/3), (screen_width/5, screen_height/3*2),
             (screen_width/5*2, screen_height/3*2), (screen_width/5*3, screen_height/3*2),
             (screen_width/5*4, screen_height/3*2)]

def start_level_1():
    subprocess.Popen(["python","Level_1.py"])
    main.destroy()

def start_level_2():
    subprocess.Popen(["python","Level_2.py"])
    main.destroy()

def start_level_3():
    subprocess.Popen(["python","Level3/Level_3.py"])
    main.destroy()

def start_level_4():
    subprocess.Popen(["python","Level_4.py"])
    main.destroy()

def start_level_5():
    subprocess.Popen(["python","Level_5.py"])
    main.destroy()

def start_level_6():
    subprocess.Popen(["python","Level_6.py"])
    main.destroy()

def start_level_7():
    subprocess.Popen(["python","Level_7.py"])
    main.destroy()

command=[start_level_1, start_level_2, start_level_3, start_level_4, 
         start_level_5, start_level_6, start_level_7]

def start(event=None):
    canvas.delete(shadow)
    canvas.delete(title)
    canvas.delete(start_button)

    for i, (img, cmd) in enumerate(zip(level_images, command)):
        button = canvas.create_image(positions[i][0], positions[i][1], anchor="center", image=img)
        canvas.tag_bind(button, "<Button-1>", lambda event, command=cmd: command())

start_image=ImageTk.PhotoImage(Image.open("Image/Start.png"))
start_button=canvas.create_image(screen_width/2, screen_height/3*2, anchor="center", image=start_image)
canvas.tag_bind(start_button, "<Button-1>", start)

main.mainloop()