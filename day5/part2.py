from collections import defaultdict, deque

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
invalid = []
for order in orders:
    nums = [int(c) for c in order.split(",")]
    valid = True
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[j] in map and nums[i] in map[nums[j]]:
                valid = False
    if not valid:
        invalid.append(nums)

def topological_sort(nums, map):
    curr_map = {key: {val for val in beforeSet if val in nums} 
                for key, beforeSet in map.items() if key in nums}
    in_degree = defaultdict(int)
    graph = defaultdict(set)
    
    for n in nums:
        graph[n]
        in_degree[n] = 0

    for k, beforeSet in curr_map.items():
        for before in beforeSet:
            if before not in graph:
                graph[before] = set()
                in_degree[before] = 0
            graph[before].add(k)
            in_degree[k] += 1

    dq = deque([n for n in nums if in_degree[n] == 0])
    new_order = []
    while dq:
        curr = dq.popleft()
        new_order.append(curr)

        for nei in graph[curr]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                dq.append(nei)

    return new_order

for line in invalid:
    new_order = topological_sort(line, map)
    ans += new_order[len(new_order) // 2]
print(ans)

