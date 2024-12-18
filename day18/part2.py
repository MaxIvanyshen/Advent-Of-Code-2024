from collections import deque

S = (0, 0)
E = (70, 70)
L = 71
DIRS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]

board = []
for i in range(L):
    board.append(["."] * L)

b = []
with open("./input") as file:
    for line in file:
        b.append(tuple([int(c) for c in line.strip().split(",")]))

def solve():
    q = deque([(S, 0)])
    seen = set()
    ans = float("inf")
    while q:
        pos, steps = q.popleft()
        r, c = pos

        if pos == E:
            ans = min(ans, steps)

        if pos in seen:
            continue
        seen.add(pos)

        for (dr, dc) in DIRS:
            if r+dr in range(L) and c+dc in range(L) and board[r+dr][c+dc] != "#":
                q.append(((r+dr, c+dc), steps + 1))

    return ans

ans = 0
while True:
    if ans >= len(b):
        break
    c, r = b[ans]
    board[r][c] = "#"
    if solve() == float("inf"):
        break
    ans += 1

print("out of range" if ans >= len(b) else b[ans])
