
input = ""
with open('input') as file:
    for line in file:
        input += line.strip()

space = []
file_id = 0
for i in range(len(input)):
    if i % 2 == 0:
        for j in range(int(input[i])):
            space.append(f"{file_id}")
        file_id += 1
    else:
        for j in range(int(input[i])):
            space.append('.')

l, r = 0, len(space) - 1
while l <= r:
    if space[l] != '.':
        l += 1
    elif space[r] == '.':
        r -= 1
    elif space[l] == '.' and space[r] != '.':
        space[l], space[r] = space[r], space[l]
        l += 1
        r -= 1

i = 0
ans = 0
while space[i] != '.':
    ans += i * int(space[i])
    i += 1

print(ans)
