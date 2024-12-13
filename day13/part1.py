
f = open("./input")
lines = [line.strip() for line in f.readlines() if line != "\n"]

def get_coords(line):

    def split_op(op):
        op = op.strip()
        split = op.split("+")
        if len(split) == 1:
            return op.split("=")
        return split

    return tuple([int(split_op(op)[1]) for op in line.split(":")[1].strip().split(",")])

def min_tuple(a, b):
    return min([a, b], key=lambda x: x[0]*3 + x[1])

def count(A, B, PRIZE, counts, pos, memo=None):
    if memo == None:
        memo = {}

    if pos[0] > PRIZE[0] or pos[1] > PRIZE[1]:
        return (float("inf"), float("inf"))

    if pos == PRIZE:
        return counts

    if (counts, pos) in memo:
        return memo[(counts, pos)]

    punchA = count(A, B, PRIZE, (counts[0] + 1, counts[1]), (pos[0] + A[0], pos[1] + A[1]), memo)
    punchB = count(A, B, PRIZE, (counts[0], counts[1] + 1), (pos[0] + B[0], pos[1] + B[1]), memo)

    result = min_tuple(punchA, punchB)

    memo[(counts, pos)] = result
    return result

ans = 0
for i in range(0, len(lines), 3):
    A = get_coords(lines[i])
    B = get_coords(lines[i+1])
    PRIZE = get_coords(lines[i+2])

    res = count(A, B, PRIZE, (0, 0), (0, 0))
    if float("inf") in res:
        continue
    ans += res[0]*3 + res[1]

print(ans)
