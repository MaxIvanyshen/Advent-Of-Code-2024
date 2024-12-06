
board = []
with open("input") as file:
    for line in file:
        board.append([c for c in list(line) if c != "\n"])

# find the guard "^"
guard = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "^":
            guard = [i, j]

# simulate path
def rotate(dir):
    if dir == [-1, 0]:
        return [0, 1]
    elif dir == [0, 1]:
        return [1, 0]
    elif dir == [1, 0]:
        return [0, -1]
    return [-1, 0]

dir = [-1, 0]
i, j = guard
while (
        (i >= 0 and i < len(board)) 
        and (j >= 0 and j <= len(board[i]))
):
    board[i][j] = "X"
    di, dj = dir
    if (
            (i + di < 0 or i + di >= len(board))
            or (j + dj < 0 or j + dj >= len(board[i]))
        ):
        break
    if board[i + di][j + dj] == "#":
        dir = rotate(dir)
    i += dir[0]
    j += dir[1]

# count cells
ans = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "X":
            ans += 1

print(ans)

