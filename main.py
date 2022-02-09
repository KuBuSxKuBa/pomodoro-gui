from tkinter import *
import math
#3 CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFEDDB"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_ui = None
                                        # TIMER RESET
def reset():
    global marks
    global reps
    window.after_cancel(timer_ui)
    canvas.itemconfig(timer_counter, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 0
                                        # TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0:
        if reps % 8 == 0:
            timer.config(text="Long break", fg=GREEN)
            count_down(long_break_sec)
        else:
            timer.config(text="Short break", fg=PINK)
            count_down(short_break_sec)
    else:
        timer.config(text="Work for 25 minutes!", fg=RED)
        count_down(work_sec)
                                        # COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_counter, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_ui
        timer_ui = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✓"
        checkmarks.config(text=marks, bg=YELLOW, fg=GREEN, font=(FONT_NAME , 20 , "bold"))
                                        # UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50 , bg=YELLOW)


canvas = Canvas(width=820 , height=800 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(420 , 410 , image=tomato_img)
timer_counter = canvas.create_text(415 , 300 , text="00:00" , fill="white", font=(FONT_NAME , 40 , "bold"))
canvas.grid(row=2, column=2)

timer = Label(text="Timer" , fg=GREEN , bg=YELLOW, font=(FONT_NAME , 40 , "bold"))
timer.grid(row=1, column=2)

start = Button(text="Start", command=start_timer , width=15, height=3)
start.grid(row=3, column=1)

reset = Button(text="Reset", command=reset , width=15, height=3)
reset.grid(row=3, column=3)

checkmarks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME , 20 , "bold"))
checkmarks.grid(row=4, column=2)

window.mainloop()