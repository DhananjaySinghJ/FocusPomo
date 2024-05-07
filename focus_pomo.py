from tkinter import *  # Importing the necessary modules
import math

# Constants for colors, font, and time durations
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0  # Counter for work sessions
timer = None  # Variable to hold the timer

# Function to reset the timer
def reset_timer():
    window.after_cancel(timer)  # Cancel the current timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset the timer text
    title_label.config(text="Timer")  # Reset the title
    checkmarks.config(text="")  # Reset the checkmarks
    global reps
    reps = 0  # Reset the work session counter

# Function to start the timer
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Determine the type of session based on the number of repetitions
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work Work Work WOrk", fg=GREEN)

# Function to handle the countdown mechanism
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update the timer text
    if count > 0:
        timer = window.after(1000, count_down, count-1)  # Update the countdown every second
    else:
        start_timer()  # Start the next session when the countdown ends
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"  # Add a checkmark for each completed work session
        checkmarks.config(text=marks)  # Update the checkmarks display

# User Interface setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas to display the tomato image and timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmarks to indicate completed work sessions
checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()  # Start the Tkinter event loop