
arr = []
endOfRules = -1
with open('./input') as file:
    for (i, line) in enumerate(file):
        line = line.strip()
        
        if line == '':
            endOfRules = i
        arr.append(line)

rules = arr[:endOfRules]
orders = arr[endOfRules+1:]

map = {}

for rule in rules:
    before, after = rule.split("|")
    if int(after) not in map:
        map[int(after)] = set()

    map[int(after)].add(int(before))

ans = 0
for order in orders:
    nums = [int(c) for c in order.split(",")]
    valid = True
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] in map and nums[i] in map[nums[j]]:
                valid = False
    if valid:
        ans += nums[len(nums) // 2]

print(ans)

