
board = []
movements = False
moves = []

with open("./input") as file:
    for line in file:
        if line == "\n":
            movements = True
            continue
        if movements:
            moves.extend([c for c in line.strip()])
        else:
            board.append([c for c in line.strip()])

def dir(c):
    if c == "<":
        return (0, -1)
    elif c == "^":
        return (-1, 0)
    elif c == ">":
        return (0, 1)
    return (1, 0)

ROWS, COLS = len(board), len(board[0])

rr, rc = 0, 0
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "@":
            rr, rc = r, c
            break

for line in board:
    print("".join(line))
print()

def move_box(r, c, dir):
    print("moving box")
    dr, dc = dir
    print(board[r+dr][c+dc])
    if board[r+dr][c+dc] == "#":
        return False
    elif board[r+dr][c+dc] == "O":
        moved = move_box(r+dr, c+dc, dir)
        if not moved:
            return False
        if board[r+dr][c+dc] == ".":
            board[r+dr][c+dc] = "O"
    else:
        board[r+dr][c+dc] = "O"
        board[r][c] = "."

    return True


def change(rr, rc, dir):
    dr, dc = dir
    print(board[rr+dr][rc+dc])
    if board[rr+dr][rc+dc] == "O":
        i, j = rr+dr, rc+dc
        if move_box(i, j, dir):
            board[i][j] = "@"
            board[rr][rc] = "."
            rr, rc = rr+dr, rc+dc
    elif board[rr+dr][rc+dc] == ".":
        board[rr][rc] = "."
        board[rr+dr][rc+dc] = "@" 
        rr, rc = rr+dr, rc+dc

    for line in board:
        print("".join(line))
    print()
    return rr, rc

for move in moves:
    print(move)
    rr, rc = change(rr, rc, dir(move))

ans = 0
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "O":
            ans += 100 * r + c
print(ans)

