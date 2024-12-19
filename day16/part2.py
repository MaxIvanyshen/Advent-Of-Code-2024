from collections import deque

# Load the maze
board = []
with open("./example_input") as file:
    for line in file:
        board.append(list(line.strip()))

ROWS, COLS = len(board), len(board[0])

S = (ROWS - 2, 1)
E = (1, COLS - 2)

# Movement directions
dirs = [
    (0, 1),   # Right
    (1, 0),   # Down
    (-1, 0),  # Up
    (0, -1)   # Left
]

def is_90_turn(old_dir, new_dir):
    """Check if turning from old_dir to new_dir is a 90-degree turn."""
    return old_dir[0] * new_dir[1] - old_dir[1] * new_dir[0] != 0

# BFS
q = deque([(0, S, (0, 1))])  # Queue: (score, position, direction)
seen = {}
predecessors = {}  # To track predecessors for backtracking

while q:
    score, (r, c), dir = q.popleft()

    # Skip if we already have a better or equal score for this state
    if (r, c, dir) in seen and seen[(r, c, dir)] <= score:
        continue
    seen[(r, c, dir)] = score

    # Store the predecessors for backtracking
    if (r, c) not in predecessors:
        predecessors[(r, c)] = []
    predecessors[(r, c)].append((score, dir))  # Track how we reached this tile

    # Explore all possible directions
    for new_dir in dirs:
        dr, dc = new_dir
        nr, nc = r + dr, c + dc

        # Skip invalid positions or walls
        if not (0 <= nr < ROWS and 0 <= nc < COLS) or board[nr][nc] == "#":
            continue

        # Calculate the cost for moving in the new direction
        new_score = score + 1
        if new_dir != dir and is_90_turn(dir, new_dir):
            new_score += 1000

        # Add the new state to the queue
        q.append((new_score, (nr, nc), new_dir))

# Find the minimum score to reach the endpoint
final_scores = [seen[(E[0], E[1], d)] for d in dirs if (E[0], E[1], d) in seen]
ans = min(final_scores)

# Backtrack to find all tiles part of any best path
best_tiles = set()
q = deque([E])  # Start backtracking from the endpoint

while q:
    r, c = q.popleft()
    if (r, c) in best_tiles:
        continue
    best_tiles.add((r, c))  # Mark this tile as part of the best path

    # Check all predecessors and backtrack
    for score, dir in predecessors.get((r, c), []):
        for dr, dc in dirs:
            nr, nc = r - dr, c - dc
            if (nr, nc, dir) in seen and seen[(nr, nc, dir)] + 1 == score:
                q.append((nr, nc))

# Output the results
print("Minimum Score:", ans)
print("Number of Tiles on Best Paths:", len(best_tiles))

# Visualize the maze with best paths marked
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) in best_tiles:
            print("O", end="")
        else:
            print(board[r][c], end="")
    print()

