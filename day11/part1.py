
input = []
mem = {}

with open("./input") as file:
    for line in file:
        input = [int(c) for c in line.strip().split()]

def count(steps, curr):
    if (steps, curr) in mem:
        return mem.get((steps, curr))

    if steps == 0:
        return 1
    
    if curr == 0:
        return count(steps - 1, 1)

    c = str(curr)
    if len(c) % 2 == 0:
        n1 = count(steps - 1, int(c[:len(c) // 2]))
        n2 = count(steps - 1, int(c[len(c) // 2:]))
        mem[(steps, curr)] = n1 + n2
        return n1 + n2

    return count(steps - 1, curr * 2024)



print(f"Part 1: {sum([count(25, x) for x in input])}")
print(f"Part 2: {sum([count(75, x) for x in input])}")
