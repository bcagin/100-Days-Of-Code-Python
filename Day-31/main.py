from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=image_f)
    flip_timer= window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=image_b)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/word_to_learn.csv", index=False)
    next_card()

window = Tk()
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card Game")

flip_timer = window.after(3000, func=flip_card)

right_img = PhotoImage(file="./images/right.png")
button_r = Button(image=right_img, highlightthickness=0, command=is_known)
button_r.grid(row=1, column=1)

wrong_img = PhotoImage(file="./images/wrong.png")
button_w = Button(image=wrong_img, highlightthickness=0, command=next_card)
button_w.grid(row=1, column=0)

image_f = PhotoImage(file="./images/card_front.png")
image_b = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=image_f)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

next_card()

window.mainloop()