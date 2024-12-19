from heapq import heappop, heappush

board = []
with open("./input") as file:
    for line in file:
        board.append(list(line.strip()))

ROWS, COLS = len(board), len(board[0])

S = (ROWS - 2, 1)
E = (1, COLS - 2)

dirs = [
    (0, 1),   # Right
    (1, 0),   # Down
    (-1, 0),  # Up
    (0, -1)   # Left
]

def is_90_turn(old_dir, new_dir):
    return old_dir[0] * new_dir[1] - old_dir[1] * new_dir[0] != 0

def solve():
    heap = [(0, S, (0, 1))]
    seen = set()

    while heap:
        score, (r, c), dir = heappop(heap)

        if (r, c) == E:
            return score

        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))

        for new_dir in dirs:
            dr, dc = new_dir
            if not(r+dr in range(ROWS) and c+dc in range(COLS)) or board[r+dr][c+dc] == "#":
                continue

            new_score = score + 1
            if new_dir != dir and is_90_turn(dir, new_dir):
                new_score += 1000

            heappush(heap, (new_score, (r+dr, c+dc), new_dir))
    return float("inf")

ans = solve()
print(ans)

