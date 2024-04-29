import tkinter as tk

def on_enter(event):
    button.config(bg='blue')

def on_leave(event):
    button.config(bg='red')

root = tk.Tk()

button = tk.Button(root, text="ปุ่ม")
button.pack(pady=20)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()

def cleardata ():

    student_id.delete(0, END)
    firstname.delete(0, END)
    lastname.delete(0, END)
    gender_info.set(None)
    year.delete(0, END)
    year.insert(0, 1)
    newuser.delete(0, END)
    newpwd.delete(0, END)
    cfpwd.delete(0, END)