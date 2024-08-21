import tkinter as tk
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


# ------------ CARDS ------------ #

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/hanzi.csv")

data_cut = data[["character", "pinyin", "definition"]].to_dict(orient="records")
random_pair = {}


def random_card():
    global random_pair, flip_timer
    window.after_cancel(flip_timer)
    random_pair = random.choice(data_cut)
    canvas.itemconfig(flashcard_bg, image=card_front)
    canvas.itemconfig(card_title, text="Chinese", fill="black")
    canvas.itemconfig(card_word, text=random_pair["character"], font=("Ariel", 60, "bold"), fill="black")
    flip_timer = window.after(3000, turn_card)


def turn_card():
    canvas.itemconfig(flashcard_bg, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_pair["definition"], font=("Ariel", 20, "bold"), fill="white")
    canvas.itemconfig(card_pinyin, text=random_pair["pinyin"], fill="white")


def guess_correct():
    data_cut.remove(random_pair)
    words_to_learn_data = pd.DataFrame(data_cut)
    words_to_learn_data.to_csv("data/words_to_learn.csv")
    random_card()

# -------------- UI -------------- #
window = tk.Tk()
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer = window.after(3000, turn_card)


canvas = tk.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
flashcard_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), tags="title")
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), tags="word")
card_pinyin = canvas.create_text(400, 330, text="", font=("Ariel", 20, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_button_image, highlightthickness=0, command=random_card)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=1, column=0)


right_button_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_button_image, highlightthickness=0, command=guess_correct)
right_button.config(borderwidth=0)
right_button.grid(row=1, column=1)



random_card()

window.mainloop()
