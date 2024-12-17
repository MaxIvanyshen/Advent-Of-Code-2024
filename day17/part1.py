import re

nums = []
with open('./input') as file:
    for line in file:
        nums.extend([int(c) for c in re.findall(r'\d+', line)])

reg = {}
reg["A"] = nums.pop(0)
reg["B"] = nums.pop(0)
reg["C"] = nums.pop(0)

iptr = 0 #instruction pointer

def convert(n):
    if n == 4:
        return reg['A']
    elif n == 5:
        return reg['B']
    elif n == 6:
        return reg['C']

    return n

out = []
def op(opcode, operand, iptr):
    if opcode == 0:
        reg['A'] = reg['A'] // (pow(2, convert(operand)))
    elif opcode == 1:
        reg['B'] = reg['B'] ^ operand
    elif opcode == 2:
        reg['B'] = convert(operand) % 8
    elif opcode == 3:
        return iptr + 2 if reg['A'] == 0 else operand
    elif opcode == 4:
        reg['B'] = reg['B'] ^ reg['C']
    elif opcode == 5:
        out.append(convert(operand) % 8)
    elif opcode == 6:
        reg['B'] = reg['A'] // (pow(2, convert(operand)))
    elif opcode == 7:
        reg['C'] = reg['A'] // (pow(2, convert(operand)))

    return iptr + 2

while iptr < len(nums):
    iptr = op(nums[iptr], nums[iptr+1], iptr)
    if iptr >= len(nums):
        break

print(",".join([str(c) for c in out]))

