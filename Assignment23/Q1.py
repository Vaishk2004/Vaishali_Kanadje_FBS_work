#Develop Simple Login System

from tkinter import *
from tkinter import messagebox

def login():
    uid = uid_entry.get()
    passw = passw_entry.get()
    if(uid=='Vaishali' and passw=='Vaish123'):
        messagebox.showinfo(message="Login Successful!!!")
    else:
        messagebox.showerror(message="Login Fail")


if __name__ == "__main__":
    w = Tk()
    w.title("Login System")
    w.geometry("300x300")

    uid_label = Label(w,text="User ID: ")
    uid_entry = Entry()

    passw_label = Label(w,text="Password: ")
    passw_entry = Entry()

    uid_label.grid(row =1,column=1)
    uid_entry.grid(row =1,column=2)
    passw_label.grid(row =2,column=1)
    passw_entry.grid(row =2,column=2)

    logbtn = Button(w,text="Login",command=login)
    logbtn.grid(row=3,column=2)

    w.mainloop()
