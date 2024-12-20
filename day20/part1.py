from collections import deque, defaultdict

board = []
with open('./input') as file:
    for line in file:
        board.append([c for c in line.strip()])

S, E = (0, 0), (0, 0)
ROWS, COLS = len(board), len(board[0])
DIRS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]

for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "S":
            S = (r, c)
        elif board[r][c] == "E":
            E = (r, c)

dists = [[-1] * COLS for _ in range(ROWS)]
dists[S[0]][S[1]] = 0
q = deque([S])

while q:
    r, c = q.popleft()
    if (r, c) == E:
        break

    for (dr, dc) in DIRS:
        if not(r+dr in range(ROWS) and c+dc in range(COLS)):
            continue
        if board[r+dr][c+dc] == "#":
            continue
        if dists[r+dr][c+dc] != -1:
            continue
        dists[r+dr][c+dc] = dists[r][c] + 1
        q.append((r+dr, c+dc))
    
ans = 0
DIRS2 = [
        (2, 0),
        (1, 1),
        (0, 2),
        (-1, 1)
]
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == "#":
            continue
        for (dr, dc) in DIRS2:
            if not(r+dr in range(ROWS) and c+dc in range(COLS)):
                continue
            if board[r+dr][c+dc] == "#":
                continue
            if abs(dists[r+dr][c+dc] - dists[r][c]) >= 102:
                ans += 1

print(ans)

