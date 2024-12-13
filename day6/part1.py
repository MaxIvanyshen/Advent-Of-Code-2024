
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

def solve():
    dir = [-1, 0]
    visited = set()
    i, j = guard
    while True:
        visited.add((i, j))
        di, dj = dir
        if(
                (i + di < 0 or i + di >= len(board))
                or (j + dj < 0 or j + dj >= len(board[i]))
        ):
            break
        if board[i + di][j + dj] == ".":
            i += di
            j += dj
        else:
            dir = rotate(dir)

    return len(visited)

print(solve())
