################################
### Import TKINTER , SQLITE ###
##############################

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3

#########################
### Database Connect ###
#######################

def createconnection() :

    global conn, cursor
    conn = sqlite3.connect('Project/database/data.db')
    cursor = conn.cursor()

#############
### Main ###
###########

def mainwindow() :

    global mainframe
    
    root = tk.Tk()
    w = 800
    h = 600 
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w, h, x, y))
    root.config(bg = '#A38FE6')
    root.title("| Order Shop |")
    root.option_add('*font', "Calibri 18 bold")
    root.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1) 
    root.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1) 
    root.resizable(False, False)
    mainframe = Frame(root, bg = '#9764b9')
    mainframe.grid(row = 0, column = 0, columnspan = 5, rowspan = 6, sticky = 'news')

    return root

###################
### Login Page ###
#################

def loginlayout() :

    global mainframe
    global userentry, pwdentry, loginBtn, registBtn
    
    mainframe.destroy()

    loginframe = Frame(root, bg = '#ece0f4')
    loginframe.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1)
    loginframe.columnconfigure((0, 1, 2, 3), weight = 1)
    loginframe.grid(row = 2, column = 2, columnspan = 2, rowspan = 3, sticky = 'news')

    Label(loginframe, image = images_logo, bg = '#ece0f4').grid(row = 0 , column = 0, columnspan = 7, sticky = 'news')
    Label(loginframe, text = 'Username :', font = 'Calibri 25 ',fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = 1, columnspan = 3, sticky = 'w')
    Label(loginframe, text = 'Password :', font = 'Calibri 25 ',fg = '#3b204b', bg = '#ece0f4').grid(row = 2, column = 1, columnspan = 3,  sticky = 'w')

    userentry = Entry(loginframe, bg = '#e4fbff', width = 36,  textvariable = userinfo)
    userentry.grid(row = 1, column = 1, columnspan = 3, padx = 30, sticky = 'e')
    pwdentry = Entry(loginframe, bg = '#e4fbff', width = 36, show = '*', textvariable = pwdinfo)
    pwdentry.grid(row = 2, column = 1, columnspan = 3, padx = 30, sticky = 'e')

    loginBtn = tk.Button(loginframe, text = "LOGIN", width = 10, command = loginclick, bg = '#6d4584', fg = '#FFFFFF')
    loginBtn.grid(row = 3, column = 1, columnspan = 3, pady = 15, padx = 20, ipady = 2)
    loginBtn.bind("<Enter>", lambda event: loginBtn.config(bg = '#320BB4'))
    loginBtn.bind("<Leave>", lambda event: loginBtn.config(bg = '#522AD3'))

    registText = Label(loginframe, text = "Don't have account?", width = 20,  bg = '#ece0f4', bd = 0, highlightbackground = "#ece0f4" )
    registText.grid(row = 5, column = 1, pady = 15, padx = 5, ipady = 2)
    registBtn = Button(loginframe, text = "Create Account", width = 20, bg = '#ece0f4', fg = '#3b204b', bd = 0, highlightbackground = "#ece0f4", command = registlayout)
    registBtn.grid(row = 5, column = 3, pady = 15, padx = 25, ipady = 2)
    registBtn.bind("<Enter>", lambda event: registBtn.config(fg = '#320BB4'))
    registBtn.bind("<Leave>", lambda event: registBtn.config(fg = '#3b204b'))

####################
### Login Check ###
##################

def loginclick() :
    global user_result
    
    user = userinfo.get()
    pwd = pwdinfo.get()

    if userentry.get() == "" or pwdentry.get() == "" :
        messagebox.showwarning("Caution!", "Please enter username/password first.")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM login WHERE username = ?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result :
            sql = "SELECT * FROM login WHERE username = ? AND password = ? "
            cursor.execute(sql, [user, pwd])   
            user_result = cursor.fetchone()
            if user_result :
                messagebox.showinfo("", "Login Successfully")
                print(user_result)
                userinfo.set("") 
                pwdinfo.set("")  
                welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
            else :
                messagebox.showwarning("Caution!", "Username or Password is invalid.")
                pwdentry.delete(0, END)
                pwdentry.focus_force()
        else :
            messagebox.showerror("Caution!", "Username not found\n Please register before Login.")
            userentry.delete(0, END)
            userentry.focus_force()

######################        
### Register Page ###
####################

def registlayout() :

    global mainframe
    global firstname, lastname, gender_male, gender_female, newuser, newpwd, cfpwd, phone, email
    global backBtn, submitBtn

    userinfo.set("") 
    pwdinfo.set("")  

    root.title("Welcome to User Registration")
    root.option_add('*font', "Calibri 18 bold")

    global registframe
    registframe = Frame(root, bg = '#ece0f4')
    registframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), weight = 1)
    registframe.columnconfigure((0, 1, 2, 3), weight = 1)
    registframe.grid(row = 1, column = 2, columnspan = 2, rowspan = 5, sticky = 'news')
    Label(registframe, text = 'Registration Form', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#5A37CE').grid(row = 0, column = 0, columnspan = 4, sticky = 'news')
    Label(registframe, text = 'Student ID : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 1, column = 1, sticky = 'e')
    student_id = Entry(registframe, width = 15, bg = '#d3e0ea')
    student_id.grid(row = 1, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'First Name : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 1, column = 1, sticky = 'e')
    firstname = Entry(registframe, width = 15, bg = '#d3e0ea')
    firstname.grid(row = 1, column = 2, sticky = 'w', padx = 15, pady = 10)

    Label(registframe, text = 'Last Name : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 2, column = 1, sticky = 'e')
    lastname = Entry(registframe, width = 15, bg = '#d3e0ea')
    lastname.grid(row = 2, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Gender : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 3, column = 1, sticky = 'e')
    gender_male = Radiobutton(registframe, text = 'Male', value = "Male", variable = gender_info, font = 'Garamond 15 bold ', fg = '#000000', width = 15, bg = '#ece0f4', anchor = 'w')
    gender_male.grid(row = 3, column = 2, sticky = 'w', padx = 15)
    gender_female = Radiobutton(registframe,text = 'Female', value = "Female", variable = gender_info, font = 'Garamond 15 bold ', fg = '#000000', width = 15, bg = '#ece0f4', anchor = 'w')
    gender_female.grid(row = 4, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Username : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 5, column = 1, sticky = 'e')
    newuser = Entry(registframe, width = 15, bg = '#d3e0ea')
    newuser.grid(row = 5, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Password : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 6, column = 1, sticky = 'e')
    newpwd = Entry(registframe,width = 15, show = '*', bg = '#d3e0ea')
    newpwd.grid(row = 6, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Confirm Password : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 7, column = 1, sticky = 'e')
    cfpwd = Entry(registframe, width = 15, show = '*', bg = '#d3e0ea')
    cfpwd.grid(row = 7, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Phone Number : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 8, column = 1, sticky = 'e')
    phone = Entry(registframe, width = 15, bg = '#d3e0ea')
    phone.grid(row = 8, column = 2, sticky = 'w', padx = 15)

    Label(registframe, text = 'Email : ', font = 'Garamond 15 bold ', fg = '#e4fbff', bg = '#ece0f4').grid(row = 9, column = 1, sticky = 'e')
    email = Entry(registframe, width = 15, bg = '#d3e0ea')
    email.grid(row = 9, column = 2, sticky = 'w', padx = 15)

    backBtn = tk.Button(registframe, text = "Cancel",bg = '#3b204b', command = registframe.destroy)
    backBtn.grid(row = 11, column = 0, ipady = 5, ipadx = 5, pady = 5, sticky = 'e', padx = 10)
    backBtn.bind("<Enter>", lambda event: backBtn.config(bg = '#818181'))
    backBtn.bind("<Leave>", lambda event: backBtn.config(bg = '#3b204b'))

    submitBtn = Button(registframe, text = "Register now", command = registration, bg = '#5730D8', fg = '#e4fbff')
    submitBtn.grid(row = 11, column = 3, ipady = 5, ipadx = 5, pady = 5, sticky = 'w')
    submitBtn.bind("<Enter>", lambda event: submitBtn.config(bg = '#320BB4'))
    submitBtn.bind("<Leave>", lambda event: submitBtn.config(bg = '#5730D8'))

    student_id.focus_force()

###################
### Main Page  ###
#################

def welcomepage() :

    global welcomeframe
    global menuBth, cartBth, reqBth, profBth, credBth, logoutBth

    welcomeframe = Frame(root, bg = '#ece0f4')
    welcomeframe.rowconfigure((0), weight = 1)
    welcomeframe.rowconfigure((1, 2), weight = 2)
    welcomeframe.columnconfigure((0, 1, 2), weight = 1)
    # Label(welcomeframe, text = 'Welcome to Order Shop', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 3 , sticky = 'news')
    Label(welcomeframe, image = images_logo, bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 3 , sticky = 'news')

    menuBtn = Button(welcomeframe, text="MENU", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:menu().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))    
    menuBtn.grid(row = 1, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    menuBtn.bind("<Enter>", lambda event: menuBtn.config(bg = '#612388'))
    menuBtn.bind("<Leave>", lambda event: menuBtn.config(bg = '#8150a0'))

    cartBtn = Button(welcomeframe, text="CART", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:cart().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    cartBtn.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    cartBtn.bind("<Enter>", lambda event: cartBtn.config(bg = '#612388'))
    cartBtn.bind("<Leave>", lambda event: cartBtn.config(bg = '#8150a0'))

    reqBtn = Button(welcomeframe, text="SUPPORT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:support().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    reqBtn.grid(row = 1, column = 2, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    reqBtn.bind("<Enter>", lambda event: reqBtn.config(bg = '#612388'))
    reqBtn.bind("<Leave>", lambda event: reqBtn.config(bg = '#8150a0'))

    profBtn = Button(welcomeframe, text="PROFILE", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:profile().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    profBtn.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    profBtn.bind("<Enter>", lambda event: profBtn.config(bg = '#612388'))
    profBtn.bind("<Leave>", lambda event: profBtn.config(bg = '#8150a0'))

    credBtn = Button(welcomeframe, text="CREDIT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:credit().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    credBtn.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    credBtn.bind("<Enter>", lambda event: credBtn.config(bg = '#612388'))
    credBtn.bind("<Leave>", lambda event: credBtn.config(bg = '#8150a0'))

    logoutBtn = Button(welcomeframe, text="LOGOUT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = logoutclick)
    logoutBtn.grid(row = 2, column = 2, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    logoutBtn.bind("<Enter>", lambda event: logoutBtn.config(bg = '#612388'))
    logoutBtn.bind("<Leave>", lambda event: logoutBtn.config(bg = '#8150a0'))

    return welcomeframe
    # print("Hello welcome page")

#######################
### Register Check ###
#####################

def registration() :

    if newuser.get() == "": ### check newuser ###

        messagebox.showwarning("Caution!", "Plese enter username")
        newuser.focus_force()

    elif newpwd.get() == "": ### check newpwd ###

        messagebox.showwarning("Caution!", "Plese enter password")
        newpwd.focus_force()

    elif firstname.get() == "" : ### check firstname ###

        messagebox.showwarning("Caution!", "Plese enter firstname")
        firstname.focus_force()

    elif lastname.get() == "": ### check lastname ###

        messagebox.showwarning("Caution!", "Plese enter lastname")
        lastname.focus_force()

    elif gender_info.get() == "" : ### check gender ###

        messagebox.showwarning("Caution!", "Please select gender")

    elif phone.get() == "": ### check lastname ###

        messagebox.showwarning("Caution!", "Plese enter email")
        phone.focus_force()

    elif email.get() == "": ### check lastname ###

        messagebox.showwarning("Caution!", "Plese enter email")
        email.focus_force()

    elif cfpwd.get() == "" : ### check cfpwd ###

        messagebox.showwarning("Caution!", "Plese confirm password")
        cfpwd.focus_force()

    elif newpwd.get() != cfpwd.get(): ### check The username is already exists ###

        messagebox.showwarning("Caution!", "Incorrect confirm password")
        newpwd.focus_force()
   
    else :

        checksql = "Select * from login where username = ?"
        cursor.execute(checksql, [newuser.get()])
        result = cursor.fetchall()

        if result :

            messagebox.showwarning("Caution!", "Username is already in use")
            newuser.select_range(0,END)
            newuser.focus_force
        else :

            ins_sql = "INSERT INTO login (username,password,fname,lname,sex,phoneno,email) VALUES(?, ?, ?, ?, ?, ?, ?)"
            param = [newuser.get(), newpwd.get(), firstname.get(), lastname.get(), gender_info.get(), phone.get(), email.get()]
            cursor.execute(ins_sql, param)
            conn.commit()
            retrivedata()
            messagebox.showinfo("Admin", "Registration successfully")
            registframe.destroy()
            loginlayout() ### back to login page ###

#####################
### Logout Click ###
###################

def logoutclick() :
    
    welcomeframe.destroy()
    messagebox.showinfo("Logout", "Logout Successfully")
    loginlayout()

###############################
### Get Data From register ###
#############################

def retrivedata() :

    sql = "SELECT * FROM login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ", len(result))
    for i, data in enumerate(result) :
        print("Row#", i + 1, data)

#####################
### Product Menu ###
###################

def menu() : ### Meat&Butchery , Processed Food , Vegetable , Fruit , Snack&Sweet , Beverage ###

    menuframe = Frame(root, bg = '#ece0f4')
    menuframe.rowconfigure((0, 1), weight = 1)
    menuframe.rowconfigure((2, 3), weight = 2)
    menuframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    menuframe.option_add('*font', "Garamond 11 bold")

    Label(menuframe, text = 'Menu', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(menuframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, sticky = 'news')

    cartmenuBtn = Button(menuframe, text = 'Cart', font = 'Garamond 10 bold', width = 3, height = 1, fg = '#000000',bg = '#C9C9C9', command = lambda:cart().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    cartmenuBtn.grid(row = 0, column = 5, padx = 10, pady = 20, sticky = 'new')
    cartmenuBtn.bind("<Enter>", lambda event: cartmenuBtn.config(bg = '#A8A8A8'))
    cartmenuBtn.bind("<Leave>", lambda event: cartmenuBtn.config(bg = '#C9C9C9'))
    
    meatBtn = Button(menuframe, text = "Meat&Butchery", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meat(menuframe).grid(column = 0, row = 2, rowspan = 3, columnspan = 6, sticky = 'news'))
    meatBtn.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    meatBtn.bind("<Enter>", lambda event: meatBtn.config(bg = '#612388'))
    meatBtn.bind("<Leave>", lambda event: meatBtn.config(bg = '#8150a0'))
    
    procBtn = Button(menuframe, text = "Processed Food", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:processed(menuframe).grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    procBtn.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    procBtn.bind("<Enter>", lambda event: procBtn.config(bg = '#612388'))
    procBtn.bind("<Leave>", lambda event: procBtn.config(bg = '#8150a0'))
    
    veggieBtn = Button(menuframe, text = "Vegetable", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:vegetable(menuframe).grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    veggieBtn.grid(row = 1, column = 2, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    veggieBtn.bind("<Enter>", lambda event: veggieBtn.config(bg = '#612388'))
    veggieBtn.bind("<Leave>", lambda event: veggieBtn.config(bg = '#8150a0'))
    
    fruitBtn = Button(menuframe, text = "Fruit", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:fruit(menuframe).grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    fruitBtn.grid(row = 1, column = 3, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    fruitBtn.bind("<Enter>", lambda event: fruitBtn.config(bg = '#612388'))
    fruitBtn.bind("<Leave>", lambda event: fruitBtn.config(bg = '#8150a0'))
    
    snsStn = Button(menuframe, text = "Snack&Sweet", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:snack(menuframe).grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    snsStn.grid(row = 1, column = 4, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    snsStn.bind("<Enter>", lambda event: snsStn.config(bg = '#612388'))
    snsStn.bind("<Leave>", lambda event: snsStn.config(bg = '#8150a0'))
    
    bevBtn = Button(menuframe, text = "Beverage", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:beverage(menuframe).grid(column=0, row=2, columnspan=6, rowspan=3, sticky='news'))
    bevBtn.grid(row = 1, column = 5, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    bevBtn.bind("<Enter>", lambda event: bevBtn.config(bg = '#612388'))
    bevBtn.bind("<Leave>", lambda event: bevBtn.config(bg = '#8150a0'))
    
    return menuframe

#####################
### Profile Edit ###
###################

def profile() :

    profileframe = Frame(root, bg = '#ece0f4')
    profileframe.rowconfigure((0), weight = 1)
    profileframe.rowconfigure((1), weight = 4)
    profileframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    profileframe.option_add('*font', "Garamond 11 bold")

    Label(profileframe, text = 'Profile', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(profileframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, sticky = 'news')

    backkkBtn = Button(profileframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0')) 

    return profileframe

#####################
### Support Page ###
###################

def support() : 

    supportframe = Frame(root, bg = '#ece0f4')
    supportframe.rowconfigure((0, 1, 2, 3 , 4, 5, 6), weight = 1)
    supportframe.columnconfigure((0, 1, 2, 3), weight = 1)
    supportframe.option_add('*font', "Garamond 11 bold")

    Label(supportframe, text = 'Support', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 4, sticky = 'news')
    Label(supportframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, sticky = 'news')

    backkkBtn = Button(supportframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0')) 

    Label(supportframe, text = 'Name : ', fg = '#000000', bg = '#ece0f4', width = 5, height = 2).grid(row = 1, column = 1, padx = 10, pady = 5, sticky = 'wn')
    Label(supportframe, text = 'Description : ', fg = '#000000', bg = '#ece0f4').grid(row = 3, column = 1,padx = 5, pady = 5, sticky = 'wn')

    nameEnt = Entry(supportframe, fg = '#000000', bg = '#e4fbff', width = 30)
    nameEnt.grid(row = 2, column = 1, sticky = 'wen', columnspan = 2, ipady = 3)
    descEnt = Entry(supportframe, fg = '#000000', bg = '#e4fbff', width = 30)
    descEnt.grid(row = 4, column = 1, sticky = 'ewn', ipadx = 10 , ipady = 75, columnspan = 2, rowspan = 2)

    suppsubBth = Button(supportframe, text = 'Submit', bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    suppsubBth.grid(row = 6, column = 1, padx = 20, pady = 20, sticky = 'ew')
    suppsubBth.bind("<Enter>", lambda event: suppsubBth.config(bg = '#612388'))
    suppsubBth.bind("<Leave>", lambda event: suppsubBth.config(bg = '#8150a0'))

    return supportframe

##################
### Cart Page ###
################

def cart() :

    cartframe = Frame(root, bg = '#ece0f4')
    return cartframe

####################
### Credit Page ###
##################

def credit() :

    creditframe = Frame(root, bg = '#ece0f4')
    return creditframe

############################
### Meat&Butchery Goods ###
##########################

def meat(frame) :
    data = fetchmenu("Meat&Butchery")
    meatframe = Frame(frame, bg = '#ece0f4')
    meatframe.rowconfigure((0, 1, 2), weight = 1)
    meatframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    meatframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(meatframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1, borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10, sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    for i in range(4) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(meatframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(meatframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(meatframe, text = f'{data[i][1]}\n {data[i][4]} THB : 1 KG\nQuantity : 25', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        porksh = Spinbox(meatframe, from_ = 0, to = 25, width = 8)
        porksh.grid(row = 2, column = i, padx = 50, sticky = 'news')
        porksh.configure(justify = CENTER, state = 'readonly')

    # Label(meatframe, image = images_porkleg, compound = LEFT,bg = '#ece0f4').grid(row = 0, column = 1, sticky = 'news')
    # Label(meatframe, text = 'Pork Leg\n 150 THB : 1 KG\nQuantity : 25', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = 1, padx = 50, sticky = 'nws')
    # porklg = Spinbox(meatframe, from_ = 0, to = 25, width = 8)
    # porklg.grid(row = 2, column = 1, padx = 50 , sticky = 'news')
    # porklg.configure(justify = CENTER, state = 'readonly')

    # Label(meatframe, image = images_sausage, compound = LEFT,bg = '#ece0f4').grid(row = 0, column = 2, sticky = 'news')
    # Label(meatframe, text = 'Sausage\n 30 THB\nQuantity : 25', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = 2, padx = 50, sticky = 'nws')
    # sausage = Spinbox(meatframe, from_ = 0, to = 25, width = 8)
    # sausage.grid(row = 2, column = 2, padx = 50 , sticky = 'news')
    # sausage.configure(justify = CENTER, state = 'readonly')

    # Label(meatframe, image = images_picanha, compound = LEFT,bg = '#ece0f4').grid(row = 0, column = 3, sticky = 'news')
    # Label(meatframe, text = 'Picanha\n 400 THB : 1 KG\nQuantity : 25', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = 3,padx = 50, sticky = 'nws')
    # picanha = Spinbox(meatframe, from_ = 0, to = 25, width = 8)
    # picanha.grid(row = 2, column = 3, padx = 50 , sticky = 'news')
    # picanha.configure(justify = CENTER, state = 'readonly')

    # nextBtn = Button(meatframe, text = "Next", bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    # nextBtn.grid(row = 4, column = 3,padx = 30 , sticky = 'news')
    # nextBtn.bind("<Enter>", lambda event: nextBtn.config(bg = '#612388'))
    # nextBtn.bind("<Leave>", lambda event: nextBtn.config(bg = '#8150a0'))

    return meatframe

#############################
### Processed Food Goods ###
###########################

def processed(frame) :

    processedframe = Frame(frame, bg = '#ece0f4')
    processedframe.rowconfigure((0, 1, 2), weight = 1)
    processedframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    processedframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(processedframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))


    return processedframe

#####################
### Veggie Goods ###
###################

def vegetable(frame) :

    vegetableframe = Frame(frame, bg = '#ece0f4')
    vegetableframe.rowconfigure((0, 1, 2), weight = 1)
    vegetableframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    vegetableframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(vegetableframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    return vegetableframe

####################
### Fruit Goods ###
##################

def fruit(frame) :

    fruitframe = Frame(frame, bg = '#ece0f4')
    fruitframe.rowconfigure((0,1,2), weight = 1)
    fruitframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    fruitframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(fruitframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    return fruitframe

##########################
### Snack&Sweet Goods ###
########################

def snack(frame) :

    snackframe = Frame(frame, bg = '#ece0f4')
    snackframe.rowconfigure((0,1,2), weight = 1)
    snackframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    snackframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(snackframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    return snackframe

#######################
### Beverage Goods ###
#####################

def beverage(frame) :

    beverageframe = Frame(frame, bg = '#ece0f4')
    beverageframe.rowconfigure((0,1,2), weight = 1)
    beverageframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    beverageframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    backkBtn = Button(beverageframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))
    
    return beverageframe

###################
### Connection ###
#################

createconnection()
def fetchmenu(type) :
    sql = 'SELECT * FROM goods WHERE type = ?'
    cursor.execute(sql, [type])   
    result = cursor.fetchall()
    return result
root = mainwindow()

##################
### Variables ###
################

userinfo = StringVar() 
pwdinfo = StringVar()
gender_info = StringVar()

####################
### Load Images ###
##################

images_login = PhotoImage(file = 'Project/images/login.png').subsample(6, 6)
images_profile = PhotoImage(file = 'Project/images/profile_f.png').subsample(3, 3)
images_profilem = PhotoImage(file = 'Project/images/profile.png').subsample(2, 2)
images_logo = PhotoImage(file = 'Project/images/logo1.png').subsample(1, 1)
images_logo2 = PhotoImage(file = 'Project/images/logo2.png').subsample(3, 3)

#####################
### Goods Images ###
###################

images_porkshoulder = PhotoImage(file = 'Project/images/porkshoulder.png').subsample(4, 4)
images_porkleg = PhotoImage(file = 'Project/images/porkleg.png').subsample(4, 4)
images_sausage = PhotoImage(file = 'Project/images/sausage.png').subsample(10, 10)
images_picanha = PhotoImage(file = 'Project/images/picanha.png').subsample(4, 4)
images_apple = PhotoImage(file = 'Project/images/apple.png').subsample(4, 4)
images_banana = PhotoImage(file = 'Project/images/banana.png').subsample(4, 4)
images_avocado = PhotoImage(file = 'Project/images/avocado.png').subsample(4, 4)
images_chocolate = PhotoImage(file = 'Project/images/chocolate.png').subsample(4, 4)
images_water = PhotoImage(file = 'Project/images/water.png').subsample(4, 4)
images_mamapork = PhotoImage(file = 'Project/images/mama_pork.png').subsample(4, 4)
images_potato_chips = PhotoImage(file = 'Project/images/potato_chips.png').subsample(4, 4)
images_gummy_bear = PhotoImage(file = 'Project/images/gummy_bear.png').subsample(4, 4)
images_broccoli = PhotoImage(file = 'Project/images/broccoli.png').subsample(4, 4)
images_bokchoy = PhotoImage(file = 'Project/images/bokchoy.png').subsample(4, 4)
images_cannedfish = PhotoImage(file = 'Project/images/cannedfish.png').subsample(4, 4)

# loginlayout()
welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
root.mainloop()

#########################
### Close Connection ###
#######################

print(fetchmenu("Meat&Butchery"))

cursor.close() 
conn.close()