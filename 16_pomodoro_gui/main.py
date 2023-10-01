import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    heading.config(text="Timer")
    ticks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # On 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="Break", fg=RED)
    # On 2nd, 4th, 6th reps
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="Break", fg=PINK)
    # On 1st, 3rd, 5th, 7th reps
    else:
        count_down(work_sec)
        heading.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        t = f"{minutes} : 0{seconds}"
    else:
        t = f"{minutes} : {seconds}"
    canvas.itemconfig(timer_txt, text=t)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        ticks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW , fg=GREEN)
heading.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

rst = Button(text="Reset", highlightthickness=0, command=reset_time)
rst.grid(row=2, column=2)

ticks = Label(text=" ", bg=YELLOW, fg=GREEN)
ticks.grid(row=3, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

window.mainloop()
