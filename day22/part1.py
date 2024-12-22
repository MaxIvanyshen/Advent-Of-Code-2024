import re
from functools import cache

nums = []
with open('./input') as file:
    for line in file:
        nums.extend([int(c) for c in re.findall(r'\d+', line)])


ITERATIONS = 2000

@cache
def mix(secret, n):
    return secret ^ n

@cache
def prune(n):
    return n % 16777216

@cache
def calc(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret

for j in range(ITERATIONS):
    for i in range(len(nums)):
        nums[i] = calc(nums[i])

print(sum(nums))

