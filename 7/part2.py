def possible(result, values, after_idx, curr=0):
    if after_idx >= len(values):
        if curr == result:
            return True
        else:
            return False

    plus = possible(result, values, after_idx + 1, curr + values[after_idx])
    mult = possible(result, values, after_idx + 1, curr * values[after_idx] if curr != 0 else values[after_idx])
    concat = possible(result, values, after_idx + 1, int(f"{curr}{values[after_idx]}"))

    return plus or mult or concat

ans = 0
with open("./input") as file:
    for line in file:
        result, values = line.split(":")
        result = int(result)
        values = list(int(c) for c in values.strip().split())

        if possible(result, values, 0):
            ans += result

print(ans)
