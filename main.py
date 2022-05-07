import tkinter
import pandas
import random
import time


BACKGROUND_COLOR = "#B1DDC6"


def change_card():
    global new_card
    new_card = random.choice(revision_dict)
    canvas.itemconfig(image, image=card_front_image)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=new_card["French"], fill="black")
    window.after(3000, func=flip)


def change_and_remove_card():
    global new_card
    revision_dict.remove(new_card)
    data = pandas.DataFrame(revision_dict)
    data.to_csv("cards_to_revise.csv", index=False)

    change_card()


def flip():
    canvas.itemconfig(image, image=card_back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=new_card["English"], fill="white")



# Get data
try:
    data = pandas.read_csv("cards_to_revise.csv")
except:
    data = pandas.read_csv("french_words.csv")
    revision_dict = data.to_dict(orient="records")
else:
    revision_dict = data.to_dict(orient="records")


new_card = {}



# Window
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashcards")


# Canvas
card_front_image = tkinter.PhotoImage(file="card_front.png")
card_back_image = tkinter.PhotoImage(file="card_back.png")

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front_image)

language = canvas.create_text(400, 150, text="", font=("Arial", "40", "italic"), fill="black")
word = canvas.create_text(400, 263, text="", font=("Arial", "60", "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")

right = tkinter.Button(image=right_image, highlightthickness=0, command=change_and_remove_card)
right.grid(column=0, row=1)
wrong = tkinter.Button(image=wrong_image, highlightthickness=0, command=change_card)
wrong.grid(column=1, row=1)




change_card()



window.mainloop()