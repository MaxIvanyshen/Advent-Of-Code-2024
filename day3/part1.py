import re

ans = 0

with open('./input') as file:
    for line in file:
        for i in range(len(line)):
            for j in range(len(line)):
                if re.match(r'mul\((\d{1,3}),\s*(\d{1,3})\)',line[i:j+1]):
                    exp = line[i:j+1].split("(")
                    digits = exp[1][0:len(exp[1])-1]
                    nums = digits.split(",")
                    ans += int(nums[0]) * int(nums[1])

                    i = j


print(ans)

