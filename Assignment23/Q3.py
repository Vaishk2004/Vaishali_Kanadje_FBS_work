#Design a Basic Calculator to perform +,-,/,*

from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    def clear():
        result_entry.delete(0,END)

    def add():
        clear()
        a = int(num_entry.get())
        b = int(num2_entry.get())
        c = a+b
        result_entry.insert(END,c)
    
    def sub():
        clear()
        a = int(num_entry.get())
        b = int(num2_entry.get())
        c = a - b
        result_entry.insert(END,c)

    def mul():
        clear()
        a = int(num_entry.get())
        b = int(num2_entry.get())
        c = a * b
        result_entry.insert(END,c)
    def div():
        clear()
        a = int(num_entry.get())
        b = int(num2_entry.get())
        if b != 0:
            c = a / b
            result_entry.insert(END,c)
        else:
            messagebox.showerror(message="Error (Div by 0)")
    
    w = Tk()
    w.title("Calculator")
    w.geometry("400x400")

    frame1 = Frame(w)
    frame2 = Frame(w)

    num_label = Label(frame1,text="First Number: ")
    num_entry = Entry(frame1)
    num2_label = Label(frame1,text="Second Number: ")
    num2_entry = Entry(frame1)
    result = Label(frame1,text="Result: ")
    result_entry = Entry(frame1)

    num_label.grid(row=1,column=1)
    num_entry.grid(row=1,column=2)
    num2_label.grid(row=2,column=1)
    num2_entry.grid(row=2,column=2)
    result.grid(row=3,column=1)
    result_entry.grid(row=3,column=2)
    frame1.pack()

    addbtn = Button(frame2, text="Add", width=10, command=add)
    subbtn = Button(frame2,text="Subtract",width=10,command=sub)
    mulbtn = Button(frame2,text="Multiply",width=10,command=mul)
    divbtn = Button(frame2,text="Divide",width=10,command=div)

    addbtn.grid(row=1,column=1)
    subbtn.grid(row=1,column=2)
    mulbtn.grid(row=2,column=1)
    divbtn.grid(row=2,column=2)
    frame2.pack()


    w.mainloop()