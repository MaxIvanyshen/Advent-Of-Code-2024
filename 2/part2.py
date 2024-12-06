ans = 0


def isSafe(nums):
    increasing = True
    safe = False
    for i in range(1, len(nums)):
        if 1 <= abs(nums[i] - nums[i - 1]) <= 3:
            if i == 1:
                if nums[i] - nums[i - 1] > 0:
                    increasing = True
                else:
                    increasing = False
            if nums[i] - nums[i - 1] > 0 and not increasing:
                safe = False
                break
            elif nums[i] - nums[i - 1] < 0 and increasing:
                safe = False
                break
            elif nums[i] - nums[i - 1] > 0 and increasing:
                safe = True
            elif nums[i] - nums[i - 1] < 0 and not increasing:
                safe = True
        else:
            safe = False
            break
    return safe


with open('./input') as file:
    for line in file:
        nums = []
        for c in line.split():
            nums.append(int(c))

        for i in range(len(nums)):
            val = nums.pop(i)
            if isSafe(nums):
                ans += 1
                break
            nums.insert(i, val)


print(ans)
