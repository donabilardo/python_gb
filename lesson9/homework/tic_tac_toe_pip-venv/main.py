from tkinter import *
import random, time


def push(b):
    global game
    global game_left
    global turn

    game[b] = "X"
    buttons[b].config(text="X", state="disabled", bg='#B533FF', fg='WHITE')
    game_left.remove(b)


    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - b

 
    game[t] = "O"
    time.sleep(0.4)
    buttons[t].config(text="O", state="disabled", fg="BLUE")
    turn += 1



game = [None] * 9
game_left = list(range(9))
turn = 0


root = Tk()
root.title("")
label = Label(width=22, text="Крестики нолики", font=("Arial", 18,"bold"))
buttons = [Button(width=5, height=2, font=("Arial", 28,"bold"), command = lambda x = i: push(x)) for i in range(9)] 

label.grid(row=0, column=0, columnspan=3)
row = 1; col = 0

for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()

