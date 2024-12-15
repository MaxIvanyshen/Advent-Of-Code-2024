import re

robots = []
with open("./input") as file:
    for line in file:
        c, r = tuple(int(c) for c in line.split()[0].split("=")[1].split(","))
        dc, dr = tuple(int(c) for c in line.split()[1].split("=")[1].split(","))
        robots.append((c, r, dc, dr))

ROWS, COLS = 103, 101
ITERATIONS = 100

board = []
for i in range(ROWS):
    board.append([0] * COLS)

def display():
    for robot in robots:
        c, r, dc, dr  = robot
        board[r][c] = int(board[r][c]) + 1 if board[r][c] != 0 else 1

def danger(iterations):
    a = b = c = d = 0
    for x, y, dx, dy in robots:
        x = (x + dx * iterations) % COLS
        y = (y + dy * iterations) % ROWS

        a += x > COLS//2 and y > ROWS//2
        b += x > COLS//2 and y < ROWS//2
        c += x < COLS//2 and y > ROWS//2
        d += x < COLS//2 and y < ROWS//2
    return a*b*c*d

mdl = float("inf")
mdl_i = 0

print(min(range(10_000), key=danger))


