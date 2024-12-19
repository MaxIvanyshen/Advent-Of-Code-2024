from functools import cache

towels = []
designs = []
with open('./input') as file:
    for line in file:
        if ',' in line:
            towels.extend([c.strip() for c in line.split(",")])
            continue
        if line.strip() != '':
            designs.append(line.strip()) 

@cache
def count_ways(d, i):
    if i >= len(d):
        return 1

    ans = 0
    for t in towels:
        if d[i:i+len(t)] == t:
            ans += count_ways(d, i + len(t))
    return ans

ans = 0
for d in designs:
    ans += count_ways(d, 0) 

print(ans)
