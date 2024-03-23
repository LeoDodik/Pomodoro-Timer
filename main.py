from tkinter import *
import math
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
    canvas.itemconfig(timer_text,text="00:00")
    timer_heading.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    reps += 1
    work_sec = 1 * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60




    if reps % 8 == 0:
       count_down(long_break_sec)
       timer_heading.config(fg=RED, highlightthickness=0,text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_heading.config(fg=PINK, highlightthickness=0, text="Break")
    else:
        count_down(work_sec)
        timer_heading.config(fg=GREEN, highlightthickness=0, text="Work")

#---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        check_marks.config(text=f"{marks}")
# ---------------------------- UI SETUP ------------------------------- #

#SCREEN SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


#UI FOR TOMATO IMG AND TIMER TEXT
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)



#TIMER HEADING
timer_heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_heading.grid(column=2, row=1)
timer_heading.config(bg=YELLOW, highlightthickness=0)

#START BUTTON
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)

#RESET BUTTON
reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=3,row=3)

#CHECK MARK
check_marks = Label(text="")
check_marks.grid(column=2,row=4)
check_marks.config(fg=GREEN,bg=YELLOW)
window.mainloop()