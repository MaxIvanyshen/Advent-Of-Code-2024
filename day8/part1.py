from collections import defaultdict

board = []
with open("./input") as file:
    for line in file:
        board.append(list(line.strip()))

ROWS, COLS = len(board), len(board[0])

map = defaultdict(list)
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] != ".":
            if not board[r][c] in map:
                map[board[r][c]] = list()
            map[board[r][c]].append((r, c))

antinodes = set()
for k in map:
    positions = map[k]
    for pos in positions:
        for other_pos in positions:
            if pos == other_pos:
                continue
            dist = (pos[0] - other_pos[0], pos[1] - other_pos[1])
            if pos[0] + dist[0] in range(0, ROWS) and pos[1] + dist[1] in range(0, COLS):
                antinodes.add((pos[0] + dist[0], pos[1] + dist[1]))
            if pos[0] - 2 * dist[0] in range(0, ROWS) and pos[1] - 2 * dist[1] in range(0, COLS):
                antinodes.add((pos[0] - 2 * dist[0], pos[1] - 2 * dist[1]))

print(len(antinodes))

