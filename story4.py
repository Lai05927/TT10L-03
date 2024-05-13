import tkinter as tk

root = tk.Tk()
root.title('Level 4')
root.geometry("1280x720")

# Load background image
image_path = "C:/CSP1123/Project/background storyline 4(3).png"
bg_image = tk.PhotoImage(file=image_path)

# Create canvas
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack(fill='both',expand=True)

# Display background image on canvas
canvas.create_image(0, 0, anchor='nw', image=bg_image)

txt = '\n\n\n\n\nYesterday Lucy and her colleagues Peter,Jart and Ava went camping\ntogether. That night, she got drunk.When she woke up in the morning,\nshe found herself not wearing any clothes.She was very distraught,\nshe felt violated by someone else.The following is their statement:\n\nPeter: " I went back to my tent after drinking with them."\nAva: "Jart was the one who brought Lucy into her tent."\nJart: "I went back to my tent after bringing Lucy back to her tent.”'
text_item = canvas.create_text(640,300, anchor='center', text=txt, fill='white', font=('Arial', 24, 'bold'))

index = 0

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