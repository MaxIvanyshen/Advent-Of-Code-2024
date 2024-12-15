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

for i in range(len(robots)):
    c, r, dc, dr = robots[i]
    for j in range(ITERATIONS):
        r += dr
        c += dc
        if r < 0:
            r = ROWS - abs(r)
        if r >= ROWS:
            r = r - ROWS
        if c < 0:
            c = COLS - abs(c)
        if c >= COLS:
            c = c - COLS
    robots[i] = (c, r, dc, dr)

display()

mr = ROWS // 2
mc = COLS // 2

count = [0, 0, 0, 0]
for r in range(mr):
    for c in range(mc):
        count[0] += board[r][c]

for r in range(mr):
    for c in range(mc + 1, COLS):
        count[1] += board[r][c]

for r in range(mr + 1, ROWS):
    for c in range(mc):
        count[2] += board[r][c]

for r in range(mr + 1, ROWS):
    for c in range(mc + 1, COLS):
        count[3] += board[r][c]

ans = count[0]*count[1]*count[2]*count[3]

print(ans)
