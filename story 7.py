import tkinter as tk
root = tk.Tk()
root.title("LEVEL 7")
root.geometry("300x150")

photo = tk.PhotoImage(file ="C:\Users\yilin\Downloads")
label = tk.label(root, image=photo,width=300,height=150,bg = "black",fg ="yellow")
label.pack()
root.mainloop()