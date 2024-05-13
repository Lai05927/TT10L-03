import tkinter as tk
from tkinter import PhotoImage 
root = tk.Tk()
root.title('Level 5')
root.geometry("1280x720")

image_path=PhotoImage(file=r"C:\CSP1123\Project\background storyline 5.png")
bg_image=image_path

canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack(fill='both',expand=True)

canvas.create_image(0, 0, anchor='nw', image=bg_image)

txt='\n\n\n\n\nChristina is an excellent Ophthalmologist who works at\n"Johns Hopkins Hospital", but one day she had a big argument\nwith her family and left home. It has been a year,she has not\nreturned home. Her mother is filled with sorrow and grief.\nOne day, her mother received an envelope. After reading its content,\nshe wept bitterly.'
text_item = canvas.create_text(640,350, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index=0

def slider():
    global index, txt
    
    if index > len(txt):
        index = -1
        txt =txt
    else:
        canvas.itemconfig(text_item, text=txt[:index])
        index += 1
        root.after(40, slider)

slider()

root.mainloop()
