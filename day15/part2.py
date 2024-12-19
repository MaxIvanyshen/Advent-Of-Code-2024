
board = []
movements = False
moves = []

with open("./example_input") as file:
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

for line in board:
    print("".join(line))
print()

def build_new_map():
    for r in range(ROWS):
        line = board[r]
        new_line = []
        for (i, c) in enumerate(line):
            if c == "#":
                new_line.extend(["#", "#"])
            elif c == "O":
                new_line.extend(["[", "]"])
            elif c == ".":
                new_line.extend([".", "."])
            elif c == "@":
                new_line.extend(["@", "."])
        board[r] = new_line
build_new_map()
COLS *= 2
for line in board:
    print("".join(line))
print()

'''
lines = [
"####################",
"##[]..[]....[]..[]##",
"##[]..........[]..##",
"##........@.[][][]##",
"##........[]..[]..##",
"##..##[]..[]......##",
"##...[]...[]..[]..##",
"##.....[]..[].[][]##",
"##........[]......##",
"####################"
        ]

board = []
for line in lines:
    board.append([c for c in list(line)])

ROWS, COLS = len(board), len(board[0])

moves = ["v"]
for line in board:
    print("".join(line))
print()
'''

rr, rc = 0, 0
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "@":
            rr, rc = r, c
            break

def can_move(r, c, dir, j):
    dr, dc = dir
    if board[r+dr][c+dc] == "#" or board[r+dr][c+dc+j] == "#" or board[r+dr][c+dc-j] == "#":
        return False
    return can_move(r+dr, c+dc, dir, j)

def move_box(r, c, dir, new="."):
    print("moving box")
    dr, dc = dir
    char = board[r][c]
    if board[r+dr][c+dc] == "#":
        return False
    elif board[r+dr][c+dc] in ["[", "]"]:
        moved = True
        if dr in [-1, 1]:
            j = 1 if board[r+dr][c+dc] == "[" else -1
            print(r+dr, j)
            print(board[r+dr][c+dc], board[r+dr][c+dc+j])
            new_char = "]" if j == 1 else "]"
            can = can_move(r+dr, c+dc, dir, j)
            print(can)
            if can:
                moved = move_box(r+dr, c+dc, dir, char) and move_box(r+dr, c+dc+j, dir, char)
                if moved:
                    board[r+dr][c+dc+j] = "."
                    board[r][c] = new
                else:
                    return False
            else:
                return False
        else:
            moved = move_box(r+dr, c+dc, dir, char)
            if not moved:
                return False
            board[r][c] = new

    else:
        board[r+dr][c+dc] = char
        board[r][c] = new

    return True


def change(rr, rc, dir):
    dr, dc = dir
    if board[rr+dr][rc+dc] in ["[", "]"]:
        i, j = rr+dr, rc+dc
        if dr == 0:
            if move_box(i, j, dir):
                board[i][j] = "@"
                board[rr][rc] = "."
                rr, rc = rr+dr, rc+dc
        else:
            if board[i][j] == "[":
               if move_box(i, j, dir) and move_box(i, j + 1, dir):
                    board[i][j] = "@"
                    board[rr][rc] = "."
                    rr, rc = rr+dr, rc+dc
            elif board[i][j] == "]":
               if move_box(i, j, dir) and move_box(i, j - 1, dir):
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
        if board[r][c] == "[":
            ans += 100 * r + c
print(ans)
