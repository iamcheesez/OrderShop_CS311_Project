################################################################
### Import TKINTER , SQLITE , MESSAGEBOX , OS , FILEDIALOG  ###
##############################################################

import datetime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3

import os
from tkinter import filedialog
from tkinter.ttk import Treeview

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

userdata = []

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
    loginBtn.bind("<Leave>", lambda event: loginBtn.config(bg = '#6d4584'))

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

    else:

        sql = "SELECT * FROM login WHERE username = ?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()

        if result :

            sql = "SELECT * FROM login WHERE username = ? AND password = ? "
            cursor.execute(sql, [user, pwd])
            user_result = cursor.fetchone()

            if user_result :

                idno = user_result[0]

                if idno >= 1 and idno <= 3 :

                    messagebox.showinfo("", "Login Successfully")
                    userdata.append(user_result)
                    print(userdata)
                    print(user_result)
                    managerpage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
                    userentry.delete(0, END)  # Clear login entry
                    pwdentry.delete(0, END)  # Clear login entry

                else :

                    messagebox.showinfo("", "Login Successfully")
                    userdata.append(user_result)
                    print(userdata)
                    print(user_result)
                    welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
                    userentry.delete(0, END)  # Clear login entry
                    pwdentry.delete(0, END)  # Clear login entry

            else:

                messagebox.showwarning("Caution!", "Username or Password is invalid.")
                pwdentry.delete(0, END)
                pwdentry.focus_force()

        else:

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

    backBtn = tk.Button(registframe, text = "Cancel",bg = '#6d4584', command = registframe.destroy)
    backBtn.grid(row = 11, column = 0, ipady = 5, ipadx = 5, pady = 5, sticky = 'e', padx = 10)
    backBtn.bind("<Enter>", lambda event: backBtn.config(bg = '#3b204b'))
    backBtn.bind("<Leave>", lambda event: backBtn.config(bg = '#6d4584'))

    submitBtn = Button(registframe, text = "Register now", command = registration, bg = '#5730D8', fg = '#e4fbff')
    submitBtn.grid(row = 11, column = 3, ipady = 5, ipadx = 5, pady = 5, sticky = 'w')
    submitBtn.bind("<Enter>", lambda event: submitBtn.config(bg = '#320BB4'))
    submitBtn.bind("<Leave>", lambda event: submitBtn.config(bg = '#5730D8'))

    student_id.focus_force()

#####################
### Manager Page ###
###################

def managerpage() :

    global managerframe

    managerframe = Frame(root, bg = '#ece0f4')
    managerframe.rowconfigure((0), weight = 1)
    managerframe.rowconfigure((1, 2), weight = 2)
    managerframe.columnconfigure((0, 1, 2), weight = 1)

    # Label(managerframe, text = 'Order Shop Management', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#5A37CE').grid(row = 0, column = 0, columnspan = 3, sticky = 'news')
    Label(managerframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 3, sticky = 'news')

    menuuBtn = Button(managerframe, text = "EDIT MENU", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:menu_edit().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    menuuBtn.grid(row = 1, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    menuuBtn.bind("<Enter>", lambda event: menuuBtn.config(bg = '#612388'))
    menuuBtn.bind("<Leave>", lambda event: menuuBtn.config(bg = '#8150a0'))

    addBtn = Button(managerframe, text = "ADD GOODS", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:addgoods().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    addBtn.grid(row = 1, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    addBtn.bind("<Enter>", lambda event: addBtn.config(bg = '#612388'))
    addBtn.bind("<Leave>", lambda event: addBtn.config(bg = '#8150a0'))

    orderBtn = Button(managerframe, text = "ORDER LIST", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:orderlist().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    orderBtn.grid(row = 1, column = 2, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    orderBtn.bind("<Enter>", lambda event: orderBtn.config(bg = '#612388'))
    orderBtn.bind("<Leave>", lambda event: orderBtn.config(bg = '#8150a0'))

    supporttBtn = Button(managerframe, text = "SUPPORT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:supporter().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    supporttBtn.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    supporttBtn.bind("<Enter>", lambda event: supporttBtn.config(bg = '#612388'))
    supporttBtn.bind("<Leave>", lambda event: supporttBtn.config(bg = '#8150a0'))

    logouttBtn = Button(managerframe, text = "LOGOUT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = logouttclick)
    logouttBtn.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
    logouttBtn.bind("<Enter>", lambda event: logouttBtn.config(bg = '#612388'))
    logouttBtn.bind("<Leave>", lambda event: logouttBtn.config(bg = '#8150a0'))

    return managerframe

#######################
### Edit Menu Page ###
#####################

def menu_edit() :

    global menuuframe

    menuuframe = Frame(root, bg = '#ece0f4')
    menuuframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1)
    menuuframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    menuuframe.grid(row = 1, column = 0, columnspan = 6, rowspan = 7, sticky = 'news')

    Label(menuuframe, text = 'Edit Menu', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(menuuframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')

    backkkBtn = Button(menuuframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:menuuframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0'))

    meatBtn = Button(menuuframe, text = "Meat&Butchery", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Meat&Butchery').grid(column = 0, row = 2, rowspan = 3, columnspan = 6, sticky = 'news'))
    meatBtn.grid(row = 1, column = 0, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    meatBtn.bind("<Enter>", lambda event: meatBtn.config(bg = '#612388'))
    meatBtn.bind("<Leave>", lambda event: meatBtn.config(bg = '#8150a0'))
    
    procBtn = Button(menuuframe, text = "Processed Food", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Processed food').grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    procBtn.grid(row = 1, column = 1, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    procBtn.bind("<Enter>", lambda event: procBtn.config(bg = '#612388'))
    procBtn.bind("<Leave>", lambda event: procBtn.config(bg = '#8150a0'))
    
    veggieBtn = Button(menuuframe, text = "Vegetable", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Vegetable').grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    veggieBtn.grid(row = 1, column = 2, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    veggieBtn.bind("<Enter>", lambda event: veggieBtn.config(bg = '#612388'))
    veggieBtn.bind("<Leave>", lambda event: veggieBtn.config(bg = '#8150a0'))
    
    fruitBtn = Button(menuuframe, text = "Fruit", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Fruit').grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    fruitBtn.grid(row = 1, column = 3, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    fruitBtn.bind("<Enter>", lambda event: fruitBtn.config(bg = '#612388'))
    fruitBtn.bind("<Leave>", lambda event: fruitBtn.config(bg = '#8150a0'))
    
    snsStn = Button(menuuframe, text = "Snack&Sweet", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Snack&Sweet').grid(column = 0, row = 2, columnspan = 6, rowspan = 3, sticky = 'news'))
    snsStn.grid(row = 1, column = 4, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    snsStn.bind("<Enter>", lambda event: snsStn.config(bg = '#612388'))
    snsStn.bind("<Leave>", lambda event: snsStn.config(bg = '#8150a0'))
    
    bevBtn = Button(menuuframe, text = "Beverage", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:meatt(menuuframe, 'Beverage').grid(column=0, row=2, columnspan=6, rowspan=3, sticky='news'))
    bevBtn.grid(row = 1, column = 5, padx = 5, pady = 5, ipadx = 10, sticky = 'new')
    bevBtn.bind("<Enter>", lambda event: bevBtn.config(bg = '#612388'))
    bevBtn.bind("<Leave>", lambda event: bevBtn.config(bg = '#8150a0'))

    return menuuframe

###########################
### Meat&Butchery Edit ###
#########################

def meatt(frame,typechoose) :

    global meattframe

    meattframe = Frame(frame, bg = '#ece0f4')
    meattframe.rowconfigure((0, 1, 2), weight = 1)
    meattframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    meattframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(meattframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(meattframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10, sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    # create table

    tree = Treeview(meattframe, column = ("ID", "Name", "Quantity", "Catergory", "Price", "Path"), show = 'headings')
    tree.heading("ID", text = "ID")
    tree.heading("Name", text = "Name")
    tree.heading("Quantity", text = "Quantity")
    tree.heading("Catergory", text = "Catergory")
    tree.heading("Price", text = "Price")
    tree.heading("Path", text = "Path")

    tree.column("ID", width = 50)
    tree.column("Name", width = 150)
    tree.column("Quantity", width = 150)
    tree.column("Catergory", width = 150)
    tree.column("Price", width = 150)
    tree.column("Path", width = 150)

    tree.grid(row = 0, column = 0, columnspan = 6, rowspan = 3, sticky = 'news')

    sql = "SELECT * FROM goods WHERE type = ?"
    cursor.execute(sql,[typechoose])
    result = cursor.fetchall()

    for i in result :
            
            tree.insert("", "end", values = i)

    # Edit button to edit goods

    editBtn = Button(meattframe, text = "Edit", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:editgoods(tree))
    editBtn.grid(row = 4, column = 1, padx = 10, sticky = 'news')
    editBtn.bind("<Enter>", lambda event: editBtn.config(bg = '#612388'))
    editBtn.bind("<Leave>", lambda event: editBtn.config(bg = '#8150a0'))

    # Delete button to delete goods

    deleteBtn = Button(meattframe, text = "Delete", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:deletegoods(tree))
    deleteBtn.grid(row = 4, column = 2, padx = 10, sticky = 'news')
    deleteBtn.bind("<Enter>", lambda event: deleteBtn.config(bg = '#612388'))
    deleteBtn.bind("<Leave>", lambda event: deleteBtn.config(bg = '#8150a0'))

    return meattframe

########################
### edit goods page ###
######################

def editgoods(tree) :

    global editframe

    editframe = Frame(root, bg = '#ece0f4')
    editframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1)
    editframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    editframe.grid(row = 0, column = 0, columnspan = 6, rowspan = 7, sticky = 'news')

    Label(editframe, text = 'Edit Goods', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(editframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')

    backkkBtn = Button(editframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:editframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, sticky = 'news') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0'))
    

    # get selected item

    selected = tree.focus()
    values = tree.item(selected, 'values')

    # create entry

    Label(editframe, text = 'ID : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 2, column = 1, sticky = 'e')
    Label(editframe, text = 'Name : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 3, column = 1, sticky = 'e')
    Label(editframe, text = 'Quantity : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 4, column = 1, sticky = 'e')
    Label(editframe, text = 'Catergory : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 5, column = 1, sticky = 'e')
    Label(editframe, text = 'Price : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 6, column = 1, sticky = 'e')
    Label(editframe, text = 'Path : ', font = 'Garamond 15 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 7, column = 1, sticky = 'e')

    id = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[0]), state = 'readonly')
    id.grid(row = 2, column = 2, padx = 30, sticky = 'w')
    name = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[1]))
    name.grid(row = 3, column = 2, padx = 30, sticky = 'w')
    quantity = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[2]))
    quantity.grid(row = 4, column = 2, padx = 30, sticky = 'w')
    catergory = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[3]))
    catergory.grid(row = 5, column = 2, padx = 30, sticky = 'w')
    price = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[4]))
    price.grid(row = 6, column = 2, padx = 30, sticky = 'w')
    path = Entry(editframe, bg = '#e4fbff', width = 36, textvariable = StringVar(value = values[5]))
    path.grid(row = 7, column = 2, padx = 30, sticky = 'w')

    # update button

    updateBtn = Button(editframe, text = "Update", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:updategoods(id, name, quantity, catergory, price, path))
    updateBtn.grid(row = 8, column = 2, padx = 10, sticky = 'news')
    updateBtn.bind("<Enter>", lambda event: updateBtn.config(bg = '#612388'))
    updateBtn.bind("<Leave>", lambda event: updateBtn.config(bg = '#8150a0'))

    return editframe

#####################
### Update Goods ###
###################

def updategoods(id, name, quantity, catergory, price, path) :

    id = id.get()
    name = name.get()
    quantity = quantity.get()
    catergory = catergory.get()
    price = price.get()
    path = path.get()

    sql = "UPDATE goods SET pname = ?, quantity = ?, type = ?, price = ?, gpath = ? WHERE gno = ?"
    cursor.execute(sql, [name, quantity, catergory, price, path, id])
    conn.commit()

    messagebox.showinfo("", "Goods updated successfully")
    meattframe.destroy()
    meatt(meattframe)


#####################
### Delete Goods ###
###################

def deletegoods(tree) :

    selected = tree.focus()
    values = tree.item(selected, 'values')
    id = values[0]

    sql = "DELETE FROM goods WHERE gno = ?"
    cursor.execute(sql, [id])
    conn.commit()

    messagebox.showinfo("", "Goods deleted successfully")
    meattframe.destroy()
    meatt(meattframe)

#######################
### Add Goods Page ###
#####################

pathphoto = []

def addgoods() :

    global addgoodsframe
    global product_name, product_price, product_quantity, product_category, product_image

    addgoodsframe = Frame(root, bg = '#ece0f4')
    addgoodsframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1)
    addgoodsframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    addgoodsframe.grid(row = 1, column = 0, columnspan = 6, rowspan = 7, sticky = 'news')

    Label(addgoodsframe, text = 'Add Product', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(addgoodsframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')

    backkkBtn = Button(addgoodsframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:addgoodsframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0'))

    Label(addgoodsframe, text = 'Product Name : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 2, column = 1, sticky = 'ne')
    product_name = Entry(addgoodsframe, width = 15, justify = 'center', bg = '#d3e0ea')
    product_name.grid(row = 2, column = 2, sticky = 'nw', padx = 15)

    Label(addgoodsframe, text = 'Product Price : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 3, column = 1, sticky = 'ne')
    product_price = Entry(addgoodsframe, width = 15, justify = 'center', bg = '#d3e0ea')
    product_price.grid(row = 3, column = 2, sticky = 'nw', padx = 15)

    Label(addgoodsframe, text = 'Product Quantity : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 4, column = 1, sticky = 'ne')
    product_quantity = Entry(addgoodsframe, width = 15, justify = 'center', bg = '#d3e0ea')
    product_quantity.grid(row = 4, column = 2, sticky = 'nw', padx = 15)

    Label(addgoodsframe, text = 'Product Category : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 5, column = 1, sticky = 'ne')
    product_category = Combobox(addgoodsframe, width = 15, justify='center', values = ['Meat&Butchery', 'Processed food', 'Vegetable', 'Fruit', 'Snack&Sweet', 'Beverage'], textvariable=catergoryinfo)
    product_category.grid(row = 5, column = 2, sticky = 'nw', padx = 15)

    Label(addgoodsframe, text = 'Product Image : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 6, column = 1, sticky = 'ne')

    submitBtn = Button(addgoodsframe, text = "Add Product", command = addproduct, bg = '#5730D8', fg = '#e4fbff')
    submitBtn.grid(row = 7, column = 2, ipady = 5, ipadx = 5, pady = 5, sticky = 'w')
    submitBtn.bind("<Enter>", lambda event: submitBtn.config(bg = '#320BB4'))
    submitBtn.bind("<Leave>", lambda event: submitBtn.config(bg = '#5730D8'))

    ####################
    ### Select File ###
    ##################

    

    def select_file() :

        file_path = filedialog.askopenfilename(title = "Select Photo", filetypes = [("Photo", "*.jpg *.png *.jpeg")])

        if file_path :
            # print(file_path)
            label["text"] = f"Selected Photo : {file_path}"
            pathphoto.append(file_path)



    ###############################
    ### Button for Select File ###
    #############################
    product_image = Button(addgoodsframe, text = "Choose File", command = select_file)
    product_image.grid(row = 6, column = 2, sticky = 'nw', padx = 15)

    label = tk.Label( text = "")
    label.pack()

    return addgoodsframe

##################
### Move File ###
################

def move_file(path) :
    source_file = path
    pathtodb = os.path.basename(path)
    destination_folder = "Project/images"
    
    try:
        if not os.path.exists(destination_folder) :
            os.makedirs(destination_folder)
        os.rename(source_file, destination_folder + "/" + os.path.basename(source_file))
        return pathtodb
    except Exception as e :

        print("error")

##########################
### Add Product Click ###
########################

def addproduct() :
    pathphotofile = move_file(pathphoto[0])
    pathphoto.clear()
    productname = product_name.get()
    productprice = product_price.get()
    productquantity = product_quantity.get()
    productcategory = product_category.get()


    if productname == "" :

        messagebox.showwarning("Caution!", "Please enter product name")
        product_name.focus_force()

    elif productprice == "" :

        messagebox.showwarning("Caution!", "Please enter product price")
        product_price.focus_force()

    elif productquantity == "" :

        messagebox.showwarning("Caution!", "Please enter product quantity")
        product_quantity.focus_force()

    elif productcategory == "" :

        messagebox.showwarning("Caution!", "Please select product category")
        product_category.focus_force()

    elif pathphotofile == "" :

        messagebox.showwarning("Caution!", "Please select product image")
        product_image.focus_force()

    else :

        sql = "INSERT INTO goods (pname, price, quantity, type, gpath) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, [productname, productprice, productquantity, productcategory, f"images/{pathphotofile}"])
        conn.commit()

        messagebox.showinfo("Success", "Product added successfully")
        product_name.delete(0, END)
        product_price.delete(0, END)
        product_quantity.delete(0, END)
        product_category.delete(0, END)

########################
### Order List Page ###
######################

def orderlist() :

    global orderlistframe

    orderlistframe = Frame(root, bg='#ece0f4')
    orderlistframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
    orderlistframe.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
    orderlistframe.grid(row=1, column=0, columnspan=6, rowspan=7, sticky='news')

    Label(orderlistframe, text='Order List', font='Garamond 26 bold', fg='#e4fbff', bg='#c4a4dc').grid(row=0,
                                                                                                        column=0,
                                                                                                        columnspan=6,
                                                                                                        sticky='news')
    Label(orderlistframe, image=images_logo2, fg='#e4fbff', bg='#c4a4dc').grid(row=0, column=0, columnspan=6,
                                                                               sticky='news')

    backkkBtn = Button(orderlistframe, text="Back", bg='#8150a0', fg='#e4fbff', width=5, height=1, borderwidth=0,
                       command=lambda: orderlistframe.destroy())
    backkkBtn.grid(row=1, column=0, padx=10, pady=10, sticky='wn')
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg='#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg='#8150a0'))

    # create table
    tree = Treeview(orderlistframe, column=("ID", "Time", "Name", "Price"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Time", text="Time")
    tree.heading("Name", text="Name")
    tree.heading("Price", text="Price")
    tree.column("ID", width=100)
    tree.column("Time", width=100)
    tree.column("Name", width=100)
    tree.column("Price", width=100)
    tree.grid(row=2, column=0, columnspan=6, sticky='news')

    cursor.execute("SELECT * FROM history")
    result = cursor.fetchall()

    # insert data to table
    for row in result:
        tree.insert("", "end", values=row)

    return orderlistframe

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

    cartBtn = Button(welcomeframe, text="CART", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:cartp().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
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

    logoutBtn = Button(welcomeframe, text="LOGOUT", font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = logoutclick)
    logoutBtn.grid(row = 2, column = 1, padx = 10, pady = 10, ipadx = 10, ipady = 5, sticky = 'news')
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

            ins_sql = "INSERT INTO login (username, password, fname, lname, sex, phoneno, email) VALUES(?, ?, ?, ?, ?, ?, ?)"
            param = [newuser.get(), newpwd.get(), firstname.get(), lastname.get(), gender_info.get(), phone.get(), email.get()]
            cursor.execute(ins_sql, param)
            conn.commit()
            retrivedata()
            messagebox.showinfo("Admin", "Registration successfully")
            registframe.destroy()
            loginlayout() ### back to login page ###

######################
### Destroy frame ###
####################


    welcomeframe.destroy()
    # menuframe.destroy()
    # meatframe.destroy()
    # processedframe.destroy()
    # vegetableframe.destroy()
    # fruitframe.destroy()

# ##############################
# ### Logout Click ( User ) ###
# ############################

def logoutclick() :
    
    welcomeframe.destroy()
    messagebox.showinfo("Logout", "Logout Successfully")
    loginlayout()

#################################
### Logout Click ( Manager ) ###
###############################

def logouttclick() :

    managerframe.destroy()
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

    global menuframe

    menuframe = Frame(root, bg = '#ece0f4')
    menuframe.rowconfigure((0, 1), weight = 1)
    menuframe.rowconfigure((2, 3), weight = 2)
    menuframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    menuframe.option_add('*font', "Garamond 11 bold")

    Label(menuframe, text = 'Menu', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(menuframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, sticky = 'news')

    cartmenuBtn = Button(menuframe, text = 'Cart', font = 'Garamond 10 bold', width = 3, height = 1, fg = '#000000',bg = '#C9C9C9', command = lambda:cartp().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
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

    sql = "SELECT * FROM login WHERE username = ?"
    cursor.execute(sql, [user_result[0]])
    result = cursor.fetchone()

    profileframe = Frame(root, bg = '#ece0f4')
    profileframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight = 1)
    profileframe.columnconfigure((0, 1, 2, 3,4), weight = 1)
    # profileframe.option_add('*font', "Garamond 11 bold")
    Label(profileframe, text = 'Profile', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0,rowspan=3, column = 0, columnspan = 6, sticky = 'news')
    Label(profileframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0,rowspan=3, column = 0, sticky = 'news')
    Button(profileframe, text = 'Back', font = 'Garamond 15 bold', bg = '#8150a0', fg = '#e4fbff', command = lambda:profileframe.destroy()).grid(row = 0,rowspan=3, column = 4,)
    Label(profileframe, text = 'First Name : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 4, column = 0, sticky = 'e')
    Label(profileframe, text = 'Last Name : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 5, column = 0, sticky = 'e')
    Label(profileframe, text = 'Username : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 6, column = 0, sticky = 'e')
    Label(profileframe, text = 'Phone Number : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 7, column = 0, sticky = 'e')
    Label(profileframe, text = 'Email : ', font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 8, column = 0, sticky = 'e')
    Label(profileframe, text = userdata[0][3], font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 4, column = 2, sticky = 'w')
    Label(profileframe, text = userdata[0][4], font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 5, column = 2, sticky = 'w')
    Label(profileframe, text = userdata[0][1], font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 6, column = 2, sticky = 'w')
    Label(profileframe, text = userdata[0][6], font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 7, column = 2, sticky = 'w')
    Label(profileframe, text = userdata[0][7], font = 'Garamond 15 bold ', fg = '#000000', bg = '#ece0f4').grid(row = 8, column = 2, sticky = 'w')
    # bannerframe = tk.Tk()
    # bannerframe = Frame(profileframe, bg = '#c4a4dc')
    # w = 800
    # h = 200 
    # x = bannerframe.winfo_screenwidth()/2 - w/2
    # y = bannerframe.winfo_screenheight()/2 - h/2
    # bannerframe.geometry("%dx%d+%d+%d"%(w, h, x, y))
    # bannerframe.place(relx=0.5, rely=0.05, anchor='center')
    
    # Label(frame1, text='Profile', font='Garamond 26 bold', fg='#e4fbff', bg='#c4a4dc').place(relx=0.5, rely=0.05, anchor='center')
    # Label(profileframe, image=images_logo2, fg='#e4fbff', bg='#c4a4dc').place(x = 50, y = 50, anchor='center')
    

    # backkkBtn = Button(profileframe, text="Back", bg='#8150a0', fg='#e4fbff', width=5, height=1, borderwidth=0, command=lambda:profileframe.destroy()).place(x = 50, y= 150, anchor='w')
    # # Label(profileframe, text = 'Profile', font = 'Garamond 26 bold', fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    # # Label(profileframe, image = images_logo2, fg = '#e4fbff',bg = '#c4a4dc').grid(row = 0, column = 0, sticky = 'news')

    # # backkkBtn = Button(profileframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    # # backkkBtn = Button(profileframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:profileframe.destroy())
    # # backkkBtn.grid(row = 1, rowspan = 4, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    # # backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    # # backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0')) 

    # # Label(profileframe, text = 'First Name : ', fg = '#000000', bg = '#ece0f4', width = 5, height = 2).grid(row = 1, column = 1, padx = 10, pady = 5, sticky = 'wn')
    # # Label(profileframe, text = 'Last Name : ', fg = '#000000', bg = '#ece0f4').grid(row = 2, column = 1,padx = 5, pady = 5, sticky = 'wn')
    # # Label(profileframe, text = 'Username : ', fg = '#000000', bg = '#ece0f4').grid(row = 3, column = 1,padx = 5, pady = 5, sticky = 'wn')
    # # Label(profileframe, text = 'Phone Number : ', fg = '#000000', bg = '#ece0f4').grid(row = 4, column = 1,padx = 5, pady = 5, sticky = 'wn')
    # # Label(profileframe, text = 'Email : ', fg = '#000000', bg = '#ece0f4').grid(row = 5, column = 1,padx = 5, pady = 5, sticky = 'wn')

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

    # backkkBtn = Button(supportframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkkBtn = Button(supportframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:supportframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0')) 

    Label(supportframe, text = 'Name : ', fg = '#000000', bg = '#ece0f4', width = 5, height = 2).grid(row = 1, column = 1, padx = 10, pady = 5, sticky = 'wn')
    Label(supportframe, text = 'Description : ', fg = '#000000', bg = '#ece0f4').grid(row = 3, column = 1,padx = 5, pady = 5, sticky = 'wn')

    nameEnt = Entry(supportframe, fg = '#000000', bg = '#e4fbff', width = 30, textvariable = namevar)
    nameEnt.grid(row = 2, column = 1, sticky = 'wen', columnspan = 2, ipady = 3)
    descEnt = Entry(supportframe, fg = '#000000', bg = '#e4fbff', width = 30, textvariable = descvar)
    descEnt.grid(row = 4, column = 1, sticky = 'ewn', ipadx = 10 , ipady = 75, columnspan = 2, rowspan = 2)

    suppsubBth = Button(supportframe, text = 'Submit', bg = '#8150a0', fg = '#e4fbff', width = 1, height = 2, borderwidth = 0, command = lambda:supported(namevar, descvar, nameEnt, descEnt))
    suppsubBth.grid(row = 6, column = 1, padx = 20, pady = 20, sticky = 'ew')
    suppsubBth.bind("<Enter>", lambda event: suppsubBth.config(bg = '#612388'))
    suppsubBth.bind("<Leave>", lambda event: suppsubBth.config(bg = '#8150a0'))

    return supportframe

#######################
### Import Support ###
#####################

support_data = []

def supported(namevar, descvar, nameEnt, descEnt) :

    sql = "INSERT INTO support (name, description) VALUES(?, ?)"
    cursor.execute(sql, [namevar.get(), descvar.get()])
    support_data.append([namevar.get(), descvar.get()])
    conn.commit()

    messagebox.showinfo("Admin", "Support sent successfully")
    nameEnt.delete(0, END)
    descEnt.delete(0, END) 

#################################
### Support Page ( Manager ) ###
###############################

def supporter() :

    global supporterframe

    supporterframe = Frame(root, bg = '#ece0f4')
    supporterframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1)
    supporterframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    supporterframe.grid(row = 1, column = 0, columnspan = 6, rowspan = 7, sticky = 'news')

    Label(supporterframe, text = 'Support', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(supporterframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')

    backkkBtn = Button(supporterframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:supporterframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn') 
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0'))

    # Create table
    table = Treeview(supporterframe)
    table['columns'] = ('Name', 'Description')
    table.column('#0', width = 0, stretch = NO)
    table.column('Name', anchor = CENTER, width = 200)
    table.column('Description', anchor = CENTER, width = 200)
    table.heading('Name', text = 'Name', anchor = CENTER)
    table.heading('Description', text = 'Description', anchor = CENTER)
    
    # Fetch support data from the database
    cursor.execute("SELECT name, description FROM support")
    support_data = cursor.fetchall()
    
    # Insert support data into the table

    for data in support_data :

        table.insert('', 'end', values = data)
    
    table.grid(row = 2, column = 0, columnspan = 6, padx = 10, pady = 10)

    return supporterframe
    
##################
### Cart Page ###
################

def cartp() :
    
    cartframe = Frame(root, bg = '#ece0f4')
    cartframe.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1)
    cartframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    print(cart)
    Label(cartframe, text = 'Summary Of Purchase', font = 'Garamond 26 bold', fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')
    Label(cartframe, image = images_logo2, fg = '#e4fbff', bg = '#c4a4dc').grid(row = 0, column = 0, columnspan = 6, sticky = 'news')

    backkkBtn = Button(cartframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 5, height = 1 , borderwidth = 0, command = lambda:cartframe.destroy())
    backkkBtn.grid(row = 1, column = 0, padx = 10, pady = 10 , sticky = 'wn')
    backkkBtn.bind("<Enter>", lambda event: backkkBtn.config(bg = '#612388'))
    backkkBtn.bind("<Leave>", lambda event: backkkBtn.config(bg = '#8150a0'))
    checkoutbtn = Button(cartframe, text = "Checkout", bg = '#8150a0', fg = '#e4fbff',width = 7, height = 1 , borderwidth = 0, command = lambda:checkout())
    checkoutbtn.grid(row = 1, column = 5, padx = 10, pady = 10 , sticky = 'ne')
    checkoutbtn.bind("<Enter>", lambda event: checkoutbtn.config(bg = '#612388'))
    checkoutbtn.bind("<Leave>", lambda event: checkoutbtn.config(bg = '#8150a0'))
    # Create table
    table = Treeview(cartframe)
    table['columns'] = ('Product', 'Total','Price')
    table.column('#0', width=0, stretch=NO)
    table.column('Product', anchor=CENTER, width=200)
    table.column('Total', anchor=CENTER, width=100) 
    table.column('Price', anchor=CENTER, width=100)
    table.heading('Product', text='Product', anchor=CENTER)
    table.heading('Total', text='Total', anchor=CENTER)
    table.heading('Price', text='Price', anchor=CENTER)
    table.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

    def checkout() :

        sql = "INSERT INTO history (idno,time,pname,price) VALUES(?, ?, ?,?)"
        up_sql = "UPDATE goods SET quantity = quantity - ? WHERE pname = ?"

        Label(cartframe, image = images_qr, bg = '#ece0f4').grid(row = 2, column = 5, padx = 10, sticky = 'nes')

        for i in range(len(cart)) :

            # print(type(cart[list(cart.keys())[i]]))
            if cart[list(cart.keys())[i]] == "0" :

                continue

            else :

                cursor.execute(up_sql, [cart[list(cart.keys())[i]], list(cart.keys())[i]])
                cursor.execute(sql, [userdata[0][0], datetime.datetime.now(), list(cart.keys())[i], list(prize.values())[i]])
                conn.commit()
                # table.insert(parent='', index='end', iid=i, text='', values=(list(cart.keys())[i], list(cart.values())[i], list(prize.values())[i]))
        cart.clear()
        prize.clear()
    # Add data to table
    for i in range(len(cart)):
        print(type(cart[list(cart.keys())[i]]))
        if cart[list(cart.keys())[i]] == "0":
            continue
        else:

 
            table.insert(parent='', index='end', iid=i, text='', values=(list(cart.keys())[i], list(cart.values())[i], list(prize.values())[i]))

    # Calculate total price
    total_price = 0
    for child in table.get_children():
        total_price = float(table.item(child)['values'][2]) * float(table.item(child)['values'][1]) + total_price
    Label(cartframe, text=f'Summary of Purchase: {total_price} THB', font='Garamond 16 bold', fg='#000000', bg='#ece0f4').grid(row=3, column=0, columnspan=6, sticky='news')

    return cartframe

############################
### Meat&Butchery Goods ###
##########################

cart = {}
prize = {}

def meat(frame) :
    
    global meatframe

    data = fetchmenu("Meat&Butchery")
    meatframe = Frame(frame, bg = '#ece0f4')
    meatframe.rowconfigure((0, 1, 2), weight = 1)
    meatframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    meatframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(meatframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(meatframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1, borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10, sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    spinbox =[]

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            print(cart)

    for i in range(len(data)) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(meatframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(meatframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')

        Label(meatframe, text = f'{data[i][1]}\n {data[i][4]} THB : 1 KG\nQuantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
  
        porksh = Spinbox(meatframe, from_ = 0, to = data[i][2], width = 8 , textvariable = IntVar(),command = lambda:get_value())
        # Button(meatframe, text = "Add", bg = '#8150a0', fg = '#e4fbff', borderwidth = 0, command = lambda:get_value()).grid(column = 0, row = 0)
        
        porksh.grid(row = 2, column = i, padx = 50, sticky = 'news')
        porksh.configure(justify = CENTER, state = 'readonly')
        spinbox.append(porksh)
    
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

    global processedframe

    data = fetchmenu("Processed food")
    processedframe = Frame(frame, bg = '#ece0f4')
    processedframe.rowconfigure((0, 1, 2), weight = 1)
    processedframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    processedframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(processedframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(processedframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))


    spinbox = []

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            # print(i.get())
            # cart.append({data[spinbox.index(i)][1]+":"+i.get()})
            print(cart)

    for i in range(len(data)) : # Update the range to iterate over the correct number of items in the data list

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(processedframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(processedframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(processedframe, text = f'{data[i][1]}\n {data[i][4]} THB \n Quantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        proc = Spinbox(processedframe, from_ = 0, to = data[i][2], width = 8, command = lambda:get_value())
        proc.grid(row = 2, column = i, padx = 50, sticky = 'news')
        proc.configure(justify = CENTER, state = 'readonly')
        spinbox.append(proc)

    return processedframe

#####################
### Veggie Goods ###
###################

def vegetable(frame) :

    global vegetableframe

    data = fetchmenu("Vegetable")
    vegetableframe = Frame(frame, bg = '#ece0f4')
    vegetableframe.rowconfigure((0, 1, 2), weight = 1)
    vegetableframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    vegetableframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(vegetableframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(vegetableframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1 , borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))


    spinbox =[]

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            # print(i.get())
            # cart.append({data[spinbox.index(i)][1]+":"+i.get()})
            print(cart)

    for i in range(len(data)) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(vegetableframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(vegetableframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(vegetableframe, text = f'{data[i][1]}\n {data[i][4]} THB \n Quantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        veggiespn = Spinbox(vegetableframe, from_ = 0, to = data[i][2], width = 8, command = lambda:get_value())
        veggiespn.grid(row = 2, column = i, padx = 50, sticky = 'news')
        veggiespn.configure(justify = CENTER, state = 'readonly')
        spinbox.append(veggiespn)

    return vegetableframe

####################
### Fruit Goods ###
##################

def fruit(frame) :

    global fruitframe

    data = fetchmenu("Fruit")
    fruitframe = Frame(frame, bg = '#ece0f4')
    fruitframe.rowconfigure((0,1,2), weight = 1)
    fruitframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    fruitframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(fruitframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(fruitframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))

    spinbox =[]

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            # print(i.get())
            # cart.append({data[spinbox.index(i)][1]+":"+i.get()})
            print(cart)

    for i in range(len(data)) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(fruitframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(fruitframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(fruitframe, text = f'{data[i][1]}\n {data[i][4]} THB \n Quantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        fruitspn = Spinbox(fruitframe, from_ = 0, to = data[i][2], width = 8, command = lambda:get_value())
        fruitspn.grid(row = 2, column = i, padx = 50, sticky = 'news')
        fruitspn.configure(justify = CENTER, state = 'readonly')
        spinbox.append(fruitspn)

    return fruitframe

##########################
### Snack&Sweet Goods ###
########################

def snack(frame) :

    global snackframe

    data = fetchmenu("Snack&Sweet")
    snackframe = Frame(frame, bg = '#ece0f4')
    snackframe.rowconfigure((0,1,2), weight = 1)
    snackframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    snackframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(snackframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(snackframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1 , borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))


    spinbox =[]

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            # print(i.get())
            # cart.append({data[spinbox.index(i)][1]+":"+i.get()})
            print(cart)

    for i in range(len(data)) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(snackframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(snackframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(snackframe, text = f'{data[i][1]}\n {data[i][4]} THB \n Quantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        veggiespn = Spinbox(snackframe, from_ = 0, to = data[i][2], width = 8, command = lambda:get_value())
        veggiespn.grid(row = 2, column = i, padx = 50, sticky = 'news')
        veggiespn.configure(justify = CENTER, state = 'readonly')
        spinbox.append(veggiespn)

    return snackframe

#######################
### Beverage Goods ###
#####################

def beverage(frame) :
    
    global beverageframe

    data = fetchmenu("Beverage")
    beverageframe = Frame(frame, bg = '#ece0f4')
    beverageframe.rowconfigure((0,1,2), weight = 1)
    beverageframe.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
    beverageframe.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1)

    # backkBtn = Button(beverageframe, text = "Back", bg = '#8150a0', fg = '#e4fbff',width = 1, height = 1 , borderwidth = 0, command = lambda:welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news'))
    backkBtn = Button(beverageframe, text = "Back", bg = '#8150a0', fg = '#e4fbff', width = 1, height = 1 , borderwidth = 0, command = lambda:frame.destroy())
    backkBtn.grid(row = 4, column = 0, padx = 10 , sticky = 'news') 
    backkBtn.bind("<Enter>", lambda event: backkBtn.config(bg = '#612388'))
    backkBtn.bind("<Leave>", lambda event: backkBtn.config(bg = '#8150a0'))


    spinbox =[]

    def get_value() :
        for i in spinbox :
            cart.update({data[spinbox.index(i)][1]:i.get()})
            prize.update({data[spinbox.index(i)][1]:data[spinbox.index(i)][4]})
            # print(i.get())
            # cart.append({data[spinbox.index(i)][1]+":"+i.get()})
            print(cart)

    for i in range(len(data)) :

        pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        label = Label(beverageframe, image = pic, compound = LEFT, bg = '#ece0f4')
        label.image = pic  # Keep a reference to the image to prevent it from being garbage collected
        label.grid(row = 0, column = i, sticky = 'news')
        # pic = PhotoImage(file = f"Project/{data[i][5]}").subsample(4, 4)
        # print(f"Project/{data[i][5]}")
        # Label(beverageframe, image = pic, compound = LEFT, bg = '#ece0f4').grid(row = 0, column = i, sticky = 'news')
        Label(beverageframe, text = f'{data[i][1]}\n {data[i][4]} THB \n Quantity : {data[i][2]}', font = 'Garamond 12 bold', fg = '#3b204b', bg = '#ece0f4').grid(row = 1, column = i, padx = 50, sticky = 'nws')
        veggiespn = Spinbox(beverageframe, from_ = 0, to = data[i][2], width = 8, command = lambda:get_value())
        veggiespn.grid(row = 2, column = i, padx = 50, sticky = 'news')
        veggiespn.configure(justify = CENTER, state = 'readonly')
        spinbox.append(veggiespn)
    
    return beverageframe

###################
### Connection ###
#################

createconnection()

#####################################
### Select Info from Goods table ###
###################################

def fetchmenu(type) :

    sql = 'SELECT * FROM goods WHERE type = ?'
    cursor.execute(sql, [type])   
    result = cursor.fetchall()
    return result

root = mainwindow()

##################
### Variables ###
################

namevar = StringVar()
descvar = StringVar()

userinfo = StringVar() 
pwdinfo = StringVar()
gender_info = StringVar()
catergoryinfo = StringVar()

####################
### Load Images ###
##################

images_login = PhotoImage(file = 'Project/images/login.png').subsample(6, 6)
images_profile = PhotoImage(file = 'Project/images/profile_f.png').subsample(3, 3)
images_profilem = PhotoImage(file = 'Project/images/profile.png').subsample(2, 2)
images_logo = PhotoImage(file = 'Project/images/logo1.png').subsample(1, 1)
images_logo2 = PhotoImage(file = 'Project/images/logo2.png').subsample(3, 3)
images_qr = PhotoImage(file = 'Project/images/qr.png').subsample(3, 3)

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

loginlayout()
# support().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
# welcomepage().grid(column = 0, row = 0, columnspan = 6, rowspan = 7, sticky = 'news')
root.mainloop()

#########################
### Close Connection ###
#######################

print(fetchmenu("Meat&Butchery"))

cursor.close() 
conn.close()