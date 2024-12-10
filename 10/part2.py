
board = []
with open("./input") as file:
    for line in file:
        board.append([int(c) for c in list(line.strip())])

starts = []
ROWS, COLS = len(board), len(board[0])
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == 0:
            starts.append((r, c))

def get_score(board, pos, curr=0):
    r, c = pos
    if not (
        r in range(len(board))
        and c in range(len(board[r]))
    ):
        return 0
    if board[r][c] != curr:
        return 0
    if curr == 9 == board[r][c]:
        return 1

    ans = 0
    dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0],
    ]
    for dir in dirs:
        next_pos = (r + dir[0], c + dir[1])
        ans += get_score(board, next_pos, curr + 1)
    return ans

ans = 0
for s in starts:
    curr = get_score(board, s, 0)
    ans += curr

print(ans)

