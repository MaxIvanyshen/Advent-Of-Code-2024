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
        q = deque()
        q.appendleft((r, c))
        perim = {}
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
                    if not (di, dj) in perim:
                        perim[(di, dj)] = set()
                    perim[(di, dj)].add((i+di, j+dj))
        
        sides = 0
        for (k, vs) in perim.items():
            seen_perim = set()
            for (pr, pc) in vs:
                if (pr, pc) in seen_perim:
                    continue
                sides += 1
                q = deque()
                q.appendleft((pr, pc))
                while q:
                    i, j = q.pop()
                    if (i, j) in seen_perim:
                        continue
                    seen_perim.add((i, j))
                    for (di, dj) in dirs:
                        if (i+di, j+dj) in vs:
                            q.appendleft((i+di, j+dj))
                    
        ans += area * sides

print(ans)




