import tkinter as tk

root = tk.Tk()
root.title("LEVEL 7")
root.geometry("1280x720")





#background
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


#text animation
def animate_title():
    #这段代码的作用是逐步将 title_txt 中的字符添加到 title_text 中，并将 title_text 设置为 title_label 的文本内容，然后增加 title_count，直到 title_count 的值等于 title_txt 的长度为止。

    global title_count, title_text
    if title_count < len(title_txt):
        title_text += title_txt[title_count]#title_text += title_txt[title_count] 将 title_txt 中索引为 title_count 的字符添加到 title_text 中。这一行的意思是，每次执行时，将下一个字符附加到 title_text 的末尾。
        title_label.config(text=title_text)
        title_count += 1
        root.after(120, animate_title) #speed of animation
    else:
        # Start animating opening text after title is fully displayed
        slider()

def slider():
    global opening_count, opening_text
    if opening_count < len(opening_txt):
        opening_text += opening_txt[opening_count]
        opening_label.config(text=opening_text)
        opening_count += 1
        root.after(100, slider)
        

#button

    Question_btn=tk.Button(root,text="Question",font=('bold',24))
    Question_btn.place(x=1100,y=500)
    Answer_btn=tk.Button(root,text="Answer\n Question",font=('bold',24))
    Answer_btn.place(x=1100,y=580)
    



main_Frame=tk.Frame(root)


# Start animating title first
animate_title()



root.mainloop()