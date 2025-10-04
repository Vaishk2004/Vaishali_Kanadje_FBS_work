from tkinter import *
from tkinter import messagebox

# --------------------- Questions ---------------------
science_questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "What is H2O commonly known as?",
        "options": ["Hydrogen", "Oxygen", "Water", "Salt"],
        "answer": "Water"
    }
]

gk_questions = [
    {
        "question": "Who is known as the father of our nation?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Bhagat Singh", "Subhash Chandra Bose"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Rome", "Berlin", "Madrid"],
        "answer": "Paris"
    }
]

math_questions = [
    {
        "question": "What is 5 + 7?",
        "options": ["10", "12", "14", "15"],
        "answer": "12"
    },
    {
        "question": "Square root of 64?",
        "options": ["6", "7", "8", "9"],
        "answer": "8"
    }
]

python_questions = [
    {
        "question": "Which of these is a Python keyword?",
        "options": ["then", "fun", "def", "define"],
        "answer": "def"
    },
    {
        "question": "What data type is the object below? \n`[1, 2, 3]`",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "List"
    }
]


score = 0

def startGame():
    name = name_entry.get()
    passw = passw_entry.get()
    if name == "" or passw == "":
        messagebox.showerror("Error", "Please enter Name and Password")
    else:
        frame1.pack_forget()
        frame2.pack()
        messagebox.showinfo("Welcome", f"Hello {name}, choose a category!")

def start_quiz(questions):
    global score
    score = 0
    frame2.pack_forget()
    frame3.pack()
    show_question(0, questions)

def show_question(index, questions):
    if index >= len(questions):
        messagebox.showinfo("Quiz Finished", f"You scored {score} out of {len(questions)}")
        frame3.pack_forget()
        frame2.pack()
        return
    
    q = questions[index]
    question_label.config(text=q["question"])
    
    for i, opt in enumerate(q["options"]):
        option_buttons[i].config(
            text=opt,
            command=lambda opt=opt: check_answer(opt, q["answer"], index, questions)
        )

def check_answer(selected, correct, index, questions):
    global score
    if selected == correct:
        score += 1
        messagebox.showinfo("Correct!", " Your answer is correct!")
    else:
        messagebox.showerror("Incorrect!", f" Wrong answer! Correct answer: {correct}")
    show_question(index + 1, questions)


w = Tk()
w.title("Quiz Game")
w.geometry("500x400")

# Login frame
frame1 = Frame(w)
name_label = Label(frame1, text="Enter Name: ")
name_entry = Entry(frame1)
passw_label = Label(frame1, text="Password: ")
passw_entry = Entry(frame1)

name_label.grid(row=0, column=0, pady=5)
name_entry.grid(row=0, column=1, pady=5)
passw_label.grid(row=1, column=0, pady=5)
passw_entry.grid(row=1, column=1, pady=5)
Button(frame1, text="Start", command=startGame).grid(row=2, columnspan=2, pady=10)
frame1.pack()

# Category frame
frame2 = Frame(w)
Label(frame2, text="Select a category:", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

Button(frame2, text="Science", width=15, command=lambda: start_quiz(science_questions)).grid(row=1, column=0, padx=10, pady=10)
Button(frame2, text="GK", width=15, command=lambda: start_quiz(gk_questions)).grid(row=1, column=1, padx=10, pady=10)
Button(frame2, text="Math", width=15, command=lambda: start_quiz(math_questions)).grid(row=2, column=0, padx=10, pady=10)
Button(frame2, text="Python", width=15, command=lambda: start_quiz(python_questions)).grid(row=2, column=1, padx=10, pady=10)

# Quiz frame
frame3 = Frame(w)
question_label = Label(frame3, text="", wraplength=400, font=("Arial", 14))
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = Button(frame3, text="", width=30)
    btn.pack(pady=5)
    option_buttons.append(btn)

w.mainloop()
