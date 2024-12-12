from collections import deque

board = []
with open('./input') as file:
    for line in file:
        board.append(list(line.strip()))

ROWS, COLS = len(board), len(board[0])

seen = set()

dirs = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1]
]

ans = 0
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in seen:
            continue
        area = 0
        p = 0
        q = deque()
        q.appendleft((r, c))
        while q:
            i, j = q.pop()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            area += 1
            for (di, dj) in dirs:
                if i+di in range(ROWS) and j+dj in range(COLS) and board[i+di][j+dj] == board[i][j]:
                    q.append((i+di, j+dj))
                else:
                    p += 1
        
        ans += area * p

print(ans)



