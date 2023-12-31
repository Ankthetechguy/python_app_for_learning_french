BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
from tkinter import *
window = Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
my_image = PhotoImage(file="images//card_front.png")
b_image=PhotoImage(file="images//card_back.png")

card={}
data= pandas.read_csv("data//french_words.csv")
to_learn=data.to_dict(orient="records")

def next_card():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill='black')
    canvas.itemconfig(card_word,text=card["French"],fill='black')
    canvas.itemconfig(back,image=my_image)
    timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text="English",fill='white')
    canvas.itemconfig(card_word,text=card["English"],fill='white')
    canvas.itemconfig(back,image=b_image)



canvas = Canvas(width=800,height=526)
back=canvas.create_image(400,263,image=my_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,145,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",68,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


timer=window.after(3000,func=flip_card)


ximage=PhotoImage(file="images//wrong.png")
unknown_button=Button(image=ximage,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

right_image=PhotoImage(file="images//right.png")
check_mark=Button(image=right_image,highlightthickness=0,command=next_card)
check_mark.grid(row=1,column=1,)

next_card()






window.mainloop()