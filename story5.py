import tkinter 
from tkinter import PhotoImage 
root = tkinter.Tk()
root.title('Level 4')
root.geometry("1280x720")
image_path=PhotoImage(file=r"C:\CSP1123\Project\background storyline 5.png")
bg_image=tkinter.Label(root,image=image_path )
bg_image.pack()

root.mainloop()
