from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

def createconnection() :

    global conn, cursor
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()

def mainwindow() :

    global mainframe
    
    root = tk.Tk()
    w = 800
    h = 600 
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w, h, x, y))
    root.config(bg = '#5A3AC2')
    root.title("| Order Shop |")
    root.option_add('*font', "Calibri 18 bold")
    root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1) 
    root.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1) 

    mainframe = Frame(root, bg= '#5A3AC2')
    mainframe.grid(row = 0, column = 0, columnspan = 5, rowspan = 6, sticky = 'news')

    return root


def loginlayout() :

    global mainframe
    global userentry, pwdentry, loginBtn, registBtn
    
    mainframe.destroy()

    loginframe = Frame(root, bg = '#8EA3D2')
    loginframe.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1)
    loginframe.columnconfigure((0, 1, 2, 3), weight = 1)
    loginframe.grid(row = 2, column = 2, columnspan = 2, rowspan = 3, sticky = 'news')

    Label(loginframe, image = images_logo, bg = '#8EA3D2').grid(row = 0 , column = 0, columnspan = 7, sticky = 'news')
    Label(loginframe, text = 'Username :', font = 'Calibri 25 ', fg = '#ffffff', bg = '#8EA3D2').grid(row = 1, column = 1, columnspan = 2, sticky = 'e')
    Label(loginframe, text = 'Password :', font = 'Calibri 25 ', fg = '#ffffff', bg = '#8EA3D2').grid(row = 2, column = 1, columnspan = 2,  sticky = 'e')

    userentry = Entry(loginframe, bg = '#e4fbff', width = 20,  textvariable = userinfo)
    userentry.grid(row = 1, column = 3, padx = 10, sticky = 'e',)
    pwdentry = Entry(loginframe, bg = '#e4fbff', width = 20, show = '*', textvariable = pwdinfo)
    pwdentry.grid(row = 2, column = 3, padx = 10, sticky = 'e',)

    loginBtn = tk.Button(loginframe, text = "Login", width = 10, command = loginclick, bg = '#5067EC', fg = '#000000')
    loginBtn.grid(row = 3, column = 3, pady=15,padx=20,ipady=2)
    loginBtn.bind("<Enter>", lambda event: loginBtn.config(bg='#0044FF'))
    loginBtn.bind("<Leave>", lambda event: loginBtn.config(bg='#5067EC'))

    registText = Label(loginframe, text = "Don't have account?", width = 20,  bg = '#8EA3D2', bd=0, highlightbackground = "#8EA3D2" )
    registText.grid(row = 5, column = 2, pady = 15, padx = 5, ipady = 2)
    registBtn = Button(loginframe, text = "Create Account", width = 10, bg = '#8EA3D2', fg = '#ffffff', bd=0, highlightbackground = "#8EA3D2", command = registlayout)
    registBtn.grid(row = 5, column = 3, pady = 15, padx = 25, ipady = 2)
    registBtn.bind("<Enter>", lambda event: registBtn.config(fg = '#0044FF'))
    registBtn.bind("<Leave>", lambda event: registBtn.config(fg = '#ffffff'))
    
def loginclick() :
 
    global user_result
    
    user = userinfo.get()
    pwd = pwdinfo.get()

    if userentry.get() == "" or pwdentry.get() == "":

        messagebox.showwarning("Caution", "Enter username/password first.")
        userentry.focus_force()

    else :

        sql = "SELECT * FROM login WHERE username=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()

        if result :

            sql = "SELECT * FROM login WHERE username=? AND password=? "
            cursor.execute(sql, [user,pwd])   
            user_result = cursor.fetchone()

            if user_result :

                messagebox.showinfo(" ", "Login Successfully")
                print(user_result)
                userinfo.set("") 
                pwdinfo.set("")  
                welcomepage()

            else :

                messagebox.showwarning(" ", "Username or Password is invalid.")
                pwdentry.delete(0, END)
                pwdentry.focus_force()
        else :

            messagebox.showerror(" ", "Username not found\n Please register before Login.")
            userentry.delete(0, END)
            userentry.focus_force()

def welcomepage() :

    global mainframe
    
    root.title("Welcome to : " + user_result[1] + ' ' + user_result[2])
    root.option_add('*font', "Calibri 18 bold")

    mainframe.destroy() 
    mainframe = Frame(root, bg = '#6377D7')
    mainframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight = 1)
    mainframe.columnconfigure((0, 1, 2, 3, 4), weight = 1)
    mainframe.grid(row = 0, column = 0, columnspan = 6, rowspan = 7, sticky = 'news')
    
    Label(mainframe, image = images_profilem, bg = '#6377D7').grid(row = 0, column = 0, columnspan = 6)
    Label(mainframe, text = 'Student ID : ', font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 1, column = 1, sticky = 'e')
    Label(mainframe, text = str(user_result[0]), font='Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 1, column = 2, sticky = 'w')
    Label(mainframe, text = 'Name : ', font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 2,column = 1, sticky = 'e')
    Label(mainframe, text = user_result[1] + ' ' + user_result[2],font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 2, column = 2, sticky = 'w')
    Label(mainframe, text = 'Gender : ', font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 3, column = 1, sticky = 'e')
    Label(mainframe, text = user_result[3], font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 3, column = 2, sticky = 'w')
    Label(mainframe, text = 'Year : ', font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 4, column = 1, sticky = 'e')
    Label(mainframe, text = user_result[4], font = 'Calibri 20 ', fg = '#000000', bg = '#6377D7').grid(row = 4, column = 2, sticky = 'w')
    
    Button(mainframe, text = "Log out", width = 10, height = 1, command = loginlayout).grid(row = 7, column = 0, columnspan = 6)

def registlayout() :

    global mainframe
    global student_id,firstname,lastname,gender_male,gender_female,gender_other,year,newuser,newpwd,cfpwd

    userinfo.set("") 
    pwdinfo.set("")  

    root.title("Welcome to User Registration : ")
    root.option_add('*font',"Calibri 18 bold")

    registframe = Frame(root, bg = '#8EA3D2')
    registframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), weight = 1)
    registframe.columnconfigure((0,1,2,3),weight=1)
    registframe.grid(row = 1, column = 2, columnspan = 2, rowspan = 5, sticky = 'news')

    Label(registframe, text = 'Registration Form', font = 'Garamond 26 bold', fg = '#e4fbff', image = images_profile, compound = LEFT,bg = '#1687a7').grid(row = 0, column = 0, columnspan = 4, sticky = 'news')
    Label(registframe, text = 'Student ID : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 1, column = 1, sticky = 'e')
    student_id = Entry(registframe, width = 15, bg = '#d3e0ea')
    student_id.grid(row = 1, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'First Name : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 2, column = 1, sticky = 'e')
    firstname = Entry(registframe, width = 15, bg = '#d3e0ea')
    firstname.grid(row = 2, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Last Name : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 3, column = 1, sticky = 'e')
    lastname = Entry(registframe, width = 15, bg = '#d3e0ea')
    lastname.grid(row = 3, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Gender : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 4, column = 1, sticky = 'e')
    gender_male = Radiobutton(registframe, text = 'Male', value = "Male", variable = gender_info, font = 'Garamond 15 bold ', fg = '#e4fbff', width = 15, bg = '#8EA3D2', anchor = 'w')
    gender_male.grid(row = 4, column=2,sticky='w',padx=15)
    gender_female = Radiobutton(registframe,text = 'Female', value = "Female", variable = gender_info, font = 'Garamond 15 bold ', fg = '#e4fbff', width = 15, bg = '#8EA3D2', anchor = 'w')
    gender_female.grid(row = 5, column = 2, sticky = 'w', padx = 15)
    gender_other = Radiobutton(registframe, text = 'Other', value = "Other", variable = gender_info, font = 'Garamond 15 bold ', fg = '#e4fbff', width = 15, bg = '#8EA3D2', anchor = 'w')
    gender_other.grid(row = 6, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Year : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 7, column = 1, sticky = 'e')
    year = Spinbox(registframe,from_=1,to=10,width=10 , justify='left')
    year.grid(row=7,column=2,sticky='w',padx=15)

    Label(registframe, text = 'Username : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 8, column = 1, sticky = 'e')
    newuser = Entry(registframe, width = 15, bg = '#d3e0ea')
    newuser.grid(row = 8, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Password : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 9, column = 1, sticky = 'e')
    newpwd = Entry(registframe,width=15,show='*',bg='#d3e0ea')
    newpwd.grid(row=9,column=2,sticky='w',padx=15)

    Label(registframe, text = 'Confirm Password : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#8EA3D2').grid(row = 10, column = 1, sticky = 'e')
    cfpwd = Entry(registframe, width = 15, show = '*', bg = '#d3e0ea')
    cfpwd.grid(row = 10, column = 2, sticky = 'w', padx = 15)

    backBtn = Button(registframe, text = "Cancel", command = registframe.destroy)
    backBtn.grid(row = 11, column = 0, ipady = 5, ipadx = 5, pady = 5, sticky = 'e', padx = 10)
    submitBtn = Button(registframe, text = "Register now", command = registration, bg = '#4b778d', fg = '#e4fbff')
    submitBtn.grid(row = 11, column = 3, ipady = 5, ipadx = 5, pady = 5, sticky = 'w')
    student_id.focus_force()


createconnection()
root = mainwindow()

userinfo = StringVar() 
pwdinfo = StringVar()
gender_info = StringVar()

images_login = PhotoImage(file = 'images/login.png').subsample(6, 6)
images_profile = PhotoImage(file = 'images/profile_f.png').subsample(3, 3)
images_profilem = PhotoImage(file = 'images/profile.png').subsample(2, 2)
images_logo = PhotoImage(file = 'images/logo1.png')

loginlayout()
root.mainloop()

cursor.close() 
conn.close()


