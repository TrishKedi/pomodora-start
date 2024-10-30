import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
rep = 1
timer = None

WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


def start():
    global rep

    print(rep)

    current_time = WORK_MIN * 60000

    if rep % 2 > 0:
        count_down(WORK_MIN * 60)
        timer_label['text'] = "WORK"
        timer_label.config(fg=GREEN)

        print('work')
    elif rep % 2 == 0 and rep != 8:
        count_down(SHORT_BREAK_MIN * 60)
        current_time = SHORT_BREAK_MIN * 60000
        timer_label['text'] = "short break"
        timer_label.config(fg=PINK)
        print('short break')

    else:
        current_time = LONG_BREAK_MIN * 60000
        count_down(LONG_BREAK_MIN * 60)
        timer_label['text'] = "long break"
        timer_label.config(fg=RED)


        print('long break')
    rep += 1

    if rep < 9:
        window.after(current_time, start)





def stop():

    window.after_cancel(timer)
    timer_label['text'] = "TIMER"
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global rep
    rep = 0

def count_down(count):
    global rep
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60

    if len(str(count_sec)) < 2:
        count_sec = "0" + str(count_sec)

    if len(str(count_min)) < 2:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}: {count_sec}")
    if count > 0:
       timer =  window.after(1000, count_down, count -1)
    else:

        work_sessions = math.floor(rep/2)
        for _ in range(work_sessions):
            check_label.config(text="✔")




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", font=("FONT_NAME", 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(font=("FONT_NAME", 35, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=2)

start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=0, row=2)

stop_button = Button(text="Stop", command=stop, highlightthickness=0)
stop_button.grid(column=2, row=2)

window.mainloop()