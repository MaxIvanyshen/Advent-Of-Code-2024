import re

ans = 0

with open('./input') as file:
    do = True
    for line in file:
        for i in range(len(line)):
            for j in range(len(line)):
                if line[i:j+1] == "do()":
                    do = True
                elif line[i:j+1] == "don't()":
                    do = False
                elif re.match(r'mul\((\d{1,3}),\s*(\d{1,3})\)',line[i:j+1]):
                    print(f'{"do" if do else "don't"} {line[i:j+1]}')
                    exp = line[i:j+1].split("(")
                    digits = exp[1][0:len(exp[1])-1]
                    nums = digits.split(",")
                    if do:
                        ans += int(nums[0]) * int(nums[1])

                    i = j


print(ans)

