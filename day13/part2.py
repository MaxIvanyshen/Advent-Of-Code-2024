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

ans = 0
for i in range(0, len(lines), 3):
    ax, ay = get_coords(lines[i])
    bx, by = get_coords(lines[i+1])
    px, py = get_coords(lines[i+2])
    px += 10000000000000
    py += 10000000000000

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == 0 and cb % 1 == 0:
        ans += ca * 3 + cb

print(ans)
