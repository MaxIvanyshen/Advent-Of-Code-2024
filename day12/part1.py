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

def get_area(char, pos):
    if pos in seen:
        return []
    if not (
            (pos[0] in range(ROWS))
            and (pos[1] in range(COLS))
    ):
        return []
    if board[pos[0]][pos[1]] != char:
        return []
    q = deque()
    q.appendleft(pos)
    area = [pos]
    while q:
        r, c = q.pop()
        seen.add((r, c))
        for (dr, dc) in dirs:
            area.extend(get_area(char, (r+dr, c+dc)))
    return area

areas = []
for r in range(ROWS):
    for c in range(COLS):
        if not (r, c) in seen:
            areas.append(get_area(board[r][c], (r, c)))

def get_price(area):
    char = board[area[0][0]][area[0][1]]
    p = len(area) * 4

    for (r, c) in area:
        for (dr, dc) in dirs:
            if r+dr in range(ROWS) and c+dc in range(COLS) and board[r+dr][c+dc] == char:
                p -= 1

    return len(area) * p


ans = 0
for a in areas:
    ans += get_price(a)

print(ans)

