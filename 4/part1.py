
def backtrack(board, i, j, word, char_idx, dir):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
        return 0

    if board[i][j] != word[char_idx]:
        return 0

    if char_idx == len(word) - 1:
        return 1

    ans = 0
    ans += backtrack(board, i + dir[0], j + dir[1], word, char_idx + 1, dir)

    return ans

board = []

with open('./input', 'r') as file:
    for line in file:
        board.append([c for c in list(line) if c != '\n'])

ans = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        dirs = [
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1]
        ]
        for dir in dirs:
            ans += backtrack(board, i, j, "XMAS", 0, dir)

print(ans)
