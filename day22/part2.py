import re
from functools import cache
from collections import defaultdict

nums = []
with open('input') as file:
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

total_seq = {}

for n in nums:
    buyer = [n % 10]
    for _ in range(ITERATIONS):
        n = calc(n)
        buyer.append(n % 10)
    seen = set()
    for i in range(len(buyer) - 4):
        a, b, c, d, e = buyer[i:i+5]
        seq = (b - a, c - b, d - c, e - d)
        if seq in seen:
            continue
        seen.add(seq)
        if not seq in total_seq:
            total_seq[seq] = 0
        total_seq[seq] += e

print(max(total_seq.values()))

