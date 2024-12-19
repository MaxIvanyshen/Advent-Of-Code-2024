towels = []
designs = []
with open('./input') as file:
    for line in file:
        if ',' in line:
            towels.extend([c.strip() for c in line.split(",")])
            continue
        if line.strip() != '':
            designs.append(line.strip()) 

def is_possible(d, towels, i):
    if i >= len(d):
        return True

    for t in towels:
        if d[i:i+len(t)] == t:
            if is_possible(d, towels, i + len(t)):
                return True
    return False

ans = 0
for d in designs:
    ans += 1 if is_possible(d, towels, 0) else 0

print(ans)
