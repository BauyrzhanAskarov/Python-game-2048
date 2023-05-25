from game import *
import time

print("Welcome to the game 2048")
size = 4 # size of the matrix
ans = get_difficulty()   # gets difficulty level easy medium or hard
goal = int(difficulty_selection(ans))    # returns a value that should be achieved
grid = create_grid(size)

best_time_result = load_best_result(ans)
if best_time_result > 0:
    print(f"Best result was {best_time_result} seconds in level {ans}")
add(size, grid)
add(size, grid)
print_grid(grid)
start_of_time = time.time()

while True:
    if winning_state(grid, goal):
        print("You won the game!")
        end_of_time = time.time()
        res = end_of_time - start_of_time
        print(f"Your time on completing the game: {res}")
        if res < load_best_result(ans) or load_best_result(ans) == 0:
            save_best_result(res, ans)
        break
    if losing_state(grid):
        print("You have lost!")
        end_of_time = time.time()
        scr = score(grid)
        print(f"Your earned points are {scr}")
        break
    turn = get_movement_input()
    if turn == "BOT":
        while True:
            if winning_state(grid, goal):
                print("You won the game!")
                end_of_time = time.time()
                res = end_of_time - start_of_time
                print(f"Your time on completing the game: {res}")
                if res < load_best_result(ans) or load_best_result(ans) == 0:
                    print("New Best Result!")
                    save_best_result(res, ans)
                break
            if losing_state(grid):
                print("You have lost!")
                end_of_time = time.time()
                scr = score(grid)
                print(f"Your earned points are {scr}")
                break
            grid = bot_play(grid, goal)
            add(size, grid)
            print_grid(grid)
            print("Bot is thinking...")
        break
    else:
        grid = move(turn, grid)
        add(size, grid)
        print_grid(grid)

