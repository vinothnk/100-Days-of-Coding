from tkinter import *
import random
import pandas as pd

# TODO 1: create the background using the color code
BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Arial'

global random_no, flip_timer, current_card

try:
    df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    # reading the csv 1st. then store into a dataframe.

to_learn = df.to_dict(orient='records')
# TODO 5: Pick a random French word/translation and put the word into the flashcard.
# Every time you press the ❌ or ✅ buttons, it should generate a new random word to display.
def random_french_word():
    global random_no, flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(bottom_word, text=current_card['French'], fill='black')
    canvas.itemconfig(top_word, text='French', fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=change_english_word)


def change_english_word():
    global random_no, current_card
    canvas.itemconfig(bottom_word, text=current_card['English'], fill='white')
    canvas.itemconfig(top_word, text='English', fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    random_french_word()
    to_learn.remove(current_card)
    print(len(to_learn))

    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv')
    random_french_word()


# TODO 4: Read the data from the french_words.csv file in the data folder.


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_english_word)
# TODO 2: create a canvas sized width 800 and height 526 with padx and pady 50 each
WHITE = '#FFFFFF'

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='C:/Users/wooo_/PycharmProjects/Day 31 - Flash Card App/images/card_front.png')
card_back_img = PhotoImage(file='C:/Users/wooo_/PycharmProjects/Day 31 - Flash Card App/images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)

# TODO 4: english word position is x = 400, y = 150, font tuple = arial, 40, italic
# TODO 5: french translated word is x = 400, y = 263, font tuple = arial, 60, bold
top_word = canvas.create_text(400, 150, text='Title', font=(FONT, 40, 'italic'))
bottom_word = canvas.create_text(400, 263, text='word', font=(FONT, 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# TODO 3: place the image X and Y at grid 0,1 and grid 1,1, centred
x_button_image = PhotoImage(file='C:/Users/wooo_/PycharmProjects/Day 31 - Flash Card App/images/wrong.png')
x_button = Button(image=x_button_image, borderwidth=0, highlightthickness=0, command=random_french_word)
x_button.grid(row=1, column=0)

tick_button_image = PhotoImage(file='C:/Users/wooo_/PycharmProjects/Day 31 - Flash Card App/images/right.png')
tick_button = Button(image=tick_button_image, borderwidth=0, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)

window.mainloop()
