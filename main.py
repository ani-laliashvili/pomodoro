import tkinter

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
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    if reps % 2 == 1:
        text_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps == 8:
        text_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        text_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    timer_min = count // 60
    timer_sec = count % 60

    if timer_sec < 10:
        timer_sec = f"0{timer_sec}"

    canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        print(checkmark.cget("text"))
        checkmark_text = ""
        for i in range(reps // 2):
            checkmark_text += "✓"
        checkmark.config(text = f"{checkmark_text}")

        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
text_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50), background=YELLOW, fg=GREEN)
text_label.grid(column=1, row=0)

checkmark = tkinter.Label(font=(FONT_NAME, 15), fg=GREEN, background=YELLOW)
checkmark.grid(column=1, row=3)

#Buttons
start = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = tkinter.Button(text="Reset", command=reset, highlightthickness=0)
reset.grid(column=3, row=2)

window.mainloop()