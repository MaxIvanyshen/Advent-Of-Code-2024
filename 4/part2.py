board = []

with open('./input', 'r') as file:
    for line in file:
        board.append([c for c in list(line) if c != '\n'])

ans = 0

for i in range(len(board)):
    for j in range(len(board[i])):
        if (
            (i + 2 < len(board) and j + 2 < len(board[i]))
            and (board[i][j] + board[i + 1][j + 1] + board[i + 2][j + 2] in ["MAS", "SAM"])
            and (board[i + 2][j] + board[i + 1][j + 1] + board[i][j + 2] in ["MAS", "SAM"])
        ):
            ans += 1

print(ans)
