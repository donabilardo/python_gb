from tkinter import *
import random, time
from colorama import init, Fore
init(autoreset=True)

def init_game():
    root = Tk()
    root.title("")
    label = Label(width=22, text="Крестики нолики на Python", font=("Arial", 18,"bold"))
    button_0 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_1 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_2 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_3 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_4 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_5 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_6 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_7 = Button(width=5,height=2, font=("Arial", 28,"bold"))
    button_8 = Button(width=5,height=2, font=("Arial", 28,"bold"))

    label.grid(row=0, column=0, columnspan=3)
    button_0.grid(row=1, column=0)
    button_1.grid(row=1, column=1)
    button_2.grid(row=1, column=2)
    button_3.grid(row=2, column=0)
    button_4.grid(row=2, column=1)
    button_5.grid(row=2, column=2)
    button_6.grid(row=3, column=0)
    button_7.grid(row=3, column=1)
    button_8.grid(row=3, column=2)

    root.mainloop()