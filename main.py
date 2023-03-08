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
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    sb_sec = SHORT_BREAK_MIN * 60
    lb_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        count_timer(sb_sec)
        timer_label.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_timer(lb_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_timer, count - 1)
    else:
        start_timer()
        mark = ""
        for rep in range(math.floor(reps / 2)):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
canvas_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)
tick = Label(font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
tick.grid(row=3, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)
reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
