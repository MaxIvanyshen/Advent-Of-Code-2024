board = []
with open("input") as file:
    for line in file:
        board.append([c for c in list(line.strip())])

# Find the guard "^"
guard = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "^":
            guard = [i, j]

def rotate(dir):
    if dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0) 
    elif dir == (1, 0):
        return (0, -1)
    return (-1, 0)   

def has_cycle():
    dir = (-1, 0) 
    visited = set()
    i, j = guard

    while True:
        if (i, j, dir) in visited:
            return True
        visited.add((i, j, dir))

        di, dj = dir
        ni, nj = i + di, j + dj 

        if ni < 0 or ni >= len(board) or nj < 0 or nj >= len(board[0]):
            break 

        if board[ni][nj] == "#":
            dir = rotate(dir)
        else:
            i, j = ni, nj

    return False 

ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "." and [i, j] != guard:
            board[i][j] = "#"
            if has_cycle():
                ans += 1
            board[i][j] = "."

print(ans)

