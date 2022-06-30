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
my_timer = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # stop the timer function
    window.after_cancel(my_timer)
    # reset timer text 00:00
    canvas.itemconfig(timer_text, text='00:00')
    # reset title label to TIMER
    timer.config(text='TIMER')
    # reset checkmarks
    cycles.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # # If its 8th rep:
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text='BREAK', fg=RED)

    # If its the 1st/3rd/5th/7th rep
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text='BREAK', fg=PINK)
    # # If its the 2nd/4th/6th rep:
    else:
        countdown(work_sec)
        timer.config(text='WORK', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global my_timer
    global marks
    # format in time 00:00
    count_min = math.floor(count / 60)
    # math.floor will return the largest whole number.
    # example. 4.8. largest whole number below 4.8 is 4
    count_sec = count % 60

    # using dynamic typing - changing an INT to a STR
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in work_sessions:
            marks += '✔'
            cycles.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# ADDING IMAGE to the canvas
window = Tk()
window.title('My Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

# def say_smth(thing):
#     print(thing)
#
# window.after(1000, say_smth, 'hello') # example - time in milliseconds, calling a function, multiple arguments

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# to remove borders from a canvas, use highlightthickness
# load the image using the PhotoImage class, indicating the source of the image
tomato_img = PhotoImage(file='tomato.png')
# image to be placed in the centre of the canvas size, image variable to be placed after the x, y coordinates
canvas.create_image(100, 112, image=tomato_img)
# add text - need to provide * args which is the x and y args.
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Adding Timer Label
timer = Label(text='TIMER', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, 'bold'))
timer.grid(column=1, row=0)

# Adding Start and Reset Button
start_button = Button(text='START', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='RESET', command=reset_timer)
reset_button.grid(column=2, row=2)
# Adding a Tick Label indicating no of pomodoro's done.
cycles = Label(bg=YELLOW, fg=GREEN)
cycles.grid(column=1, row=3)

window.mainloop()
