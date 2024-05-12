import tkinter as tk
root = tk.Tk()
root.title("LEVEL 7")
root.geometry("1280x720")

photo = tk.PhotoImage(file ="2mcUd3NLTfKfvnhkylY4rw.png")
background_Label = tk.Label(root, image=photo,width=1280,height=720)
background_Label.place(x=0,y=0 ,relwidth=1,relheight=1)
# Level 7 Title
title_txt = "Level 7 : The Half Bottle of Perfume"
title_count = 0
title_text = ""
title_label = tk.Label(root, text=title_text, font=("Arial", 40, "bold"), bg="white", fg="black", highlightthickness=0)
title_label.pack(pady=100)
# Opening Text
opening_txt = ("Recently, my mother has been acting strangely. Not only did she secretly use my perfume and wear my "
               "clothes, but she also goes out late at night. The other day, I couldn't help but confront her, and we "
               "got into an argument. In the heat of the moment, I accidentally pushed her to the ground. I rushed "
               "to help her up, but only to find my hands covered in blood.\n")
opening_count = 0
opening_text = ""
opening_label = tk.Label(root, text=opening_text, font=("Arial", 20), bg="white", fg="black",wraplength=1000)
opening_label.pack()

def slider():
    global title_count, title_text, opening_count, opening_text

    # Update title
    if title_count < len(title_txt):
        title_text += title_txt[title_count]
        title_label.config(text=title_text)
        title_count += 1

    # Update opening text
    if opening_count < len(opening_txt):
        opening_text += opening_txt[opening_count]
        opening_label.config(text=opening_text)
        opening_count += 1

    if title_count < len(title_txt) or opening_count < len(opening_txt):
        root.after(200, slider)

slider()

root.mainloop()