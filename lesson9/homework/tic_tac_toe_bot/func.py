import random
import tkinter

root = tkinter.Tk()
root.title("Крестики нолики")
game_run = True #Маркер хода игры. если False завершаем игру и обьявляем победителя
field = [] #список содержащий в себе игровое поле 
cross_count = 0 #количество

def new_game():
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


print("sdsds")
    



