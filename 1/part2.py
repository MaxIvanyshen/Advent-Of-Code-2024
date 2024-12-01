
left, right = [], []

with open('./input', 'r') as file:
    for line in file:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

count = {}

for n in right:
    count[n] = count.get(n, 0) + 1

ans = 0

for n in left:
    c = count.get(n, 0)
    ans += n * c

print(ans)
