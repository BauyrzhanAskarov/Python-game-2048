from implementation import *

difficulty_level = [2048, 8192, 32768]  # easy , medium, hard


def get_movement_input():
    valid_inputs = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'BOT']
    while True:
        user_input = input("Enter a direction (UP/DOWN/LEFT/RIGHT/BOT)").strip().upper()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, Please try again")


def get_difficulty():
    valid_inputs = ["easy", "medium", "hard"]
    while True:
        user_input = input("Choose a difficulty (easy / medium / hard)").strip()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, Please try again")


def difficulty_selection(inp):
    if inp == "easy":
        target = difficulty_level[0]
    elif inp == "medium":
        target = difficulty_level[1]
    elif inp == "hard":
        target = difficulty_level[2]
    return target


def move(inp, grd):
    if inp == "UP":
        moved = up(grd)
    elif inp == "DOWN":
        moved = down(grd)
    elif inp == "LEFT":
        moved = left(grd)
    elif inp == "RIGHT":
        moved = right(grd)
    return moved


def save_best_result(result, level):
    with open('best_result.txt', 'a') as file:
        file.write(f"Best result in level: {level} which is {str(round(result))} seconds \n")


def load_best_result(level):
    try:
        with open("best_result.txt", "r") as file:
            lines = (file.read()).split()
            result = []
            check = False
            for word in lines:
                if word == level:
                    check = True
                if check:
                    for char in word:
                        if char.isdigit():
                            result.append(word)
            if not result:
                return 0
            else:
                size = len(result)
                return int(result[size - 1])
    except FileNotFoundError:
        return 0
