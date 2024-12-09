from collections import deque

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



free = []
free_set = set()

for i in range(len(space)):
    if space[i] == ".":
        start = i
        while space[i] == ".":
            i += 1
        if not i in free_set:
            free.append((start, i - start))
            free_set.add(i)

files = deque()
files_set = set()
for i in range(len(space) - 1, -1, -1):
    if space[i] != '.':
        id = space[i]
        start = i
        while space[i] == id:
            i -= 1
        if not i in files_set:
            files.appendleft((id, i + 1, start - i))
            files_set.add(i)

while files:
    curr = files.pop()
    for i in range(len(free)):
        if free[i][1] == 0:
            continue
        if free[i][0] < curr[1] and free[i][1] >= curr[2]:
            for j in range(free[i][0], free[i][0] + curr[2]):
                space[j] = curr[0]
            for j in range(curr[1], curr[1] + curr[2]):
                space[j] = '.'
            free[i] = (free[i][0] + curr[2], free[i][1] - curr[2])
            break

ans = 0
for i in range(len(space)):
    if space[i] == '.':
        continue
    ans += i * int(space[i])

print(ans)
