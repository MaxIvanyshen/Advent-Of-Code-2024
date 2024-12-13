
left, right = [], []

with open('./input', 'r') as file:
    for line in file:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

left.sort()
right.sort()

ans = 0

for i in range(len(left)):
    ans += abs(left[i] - right[i])

print(ans)
