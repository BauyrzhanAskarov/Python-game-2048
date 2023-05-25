import random

# once the function left is constructed, the other movements can be implemented using reverse or transpose matrix


def create_grid(size):
    g = []
    for i in range(size):
        g.append([])
        for j in range(size):
            g[i].append(0)
    return g


def add(size, grid):
    coordinate = []

    for x in range(size):
        for y in range(size):
            if grid[x][y] == 0:
                coordinate.append((x, y))

    if coordinate:
        rand_coord = random.choice(coordinate)
        grid[rand_coord[0]][rand_coord[1]] = random.choice([2, 4])


def print_grid(gr):
    for row in gr:
        print(row)


def reverse(size, grid):
    reversed_grid = create_grid(size)
    for i in range(size):
        for j in range(size):
            reversed_grid[i][j] = grid[i][size - 1 - j]
    return reversed_grid


def transpose(size, grid):
    transposed = create_grid(size)
    for i in range(size):
        for j in range(size):
            transposed[i][j] = (grid[j][i])
    return transposed


def remove_zeros(length, grd):
    modified_grid = create_grid(length)
    count = 0
    for i in range(length):
        for j in range(length):
            if grd[i][j] != 0:
                modified_grid[i][count] = grd[i][j]
                count += 1
        count = 0
    return modified_grid


def adding(length, grd):
    added_grid = create_grid(length)
    for i in range(length):
        for j in range(length):
            if j != length - 1 and grd[i][j] != 0:
                if grd[i][j] == grd[i][j + 1]:
                    added_grid[i][j] = grd[i][j] + grd[i][j + 1]
                    grd[i][j + 1] = 0
                else:
                    added_grid[i][j] = grd[i][j]
            elif j == length - 1 and grd[i][j] != 0:
                added_grid[i][j] = grd[i][j]
    return added_grid


def left(grd):
    rem = remove_zeros(len(grd), grd)
    added = adding(len(rem), rem)
    move_left = remove_zeros(len(added), added)
    return move_left


def right(grd):
    rev = reverse(len(grd), grd)
    move_left = left(rev)
    move_right = reverse(len(move_left),move_left)
    return move_right


def up(grd):
    trans = transpose(len(grd), grd)
    trans_left = left(trans)
    move_up = transpose(len(trans_left), trans_left)
    return move_up


def down(grd):
    trans = transpose(len(grd), grd)
    trans_right = right(trans)
    move_down = transpose(len(trans_right), trans_right)
    return move_down


def winning_state(grd, goal):
    for row in grd:
        if goal in row:
            return True
    return False


def losing_state(grd):
    for LIST in grd:
        if 0 in LIST:
            return False

    size = len(grd)

    for i in range(size):
        for j in range(size):
            if i != size - 1 and j != size - 1:
                if grd[i][j] == grd[i + 1][j] or grd[i][j] == grd[i][j + 1]:
                    return False
            elif i == size - 1 and j != size - 1:
                if grd[i][j] == grd[i][j + 1]:
                    return False
            elif i != size - 1 and j == size - 1:
                if grd[i][j] == grd[i + 1][j]:
                    return False
    return True


def bot_play(grd, goal):
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    random.shuffle(directions)
    if not losing_state(grd) and not winning_state(grd, goal):
        if random.choice(directions) == "UP":
            grd = up(grd)
        elif random.choice(directions) == "DOWN":
            grd = down(grd)
        elif random.choice(directions) == "LEFT":
            grd = left(grd)
        elif random.choice(directions) == "RIGHT":
            grd = right(grd)
        return grd
    return grd


def score(grd):
    result = 0
    for i in range(len(grd)):
        for j in range(len(grd)):
            if grd[i][j] != 2 or grd[i][j] != 4:
                result += grd[i][j] * 2
    return result
