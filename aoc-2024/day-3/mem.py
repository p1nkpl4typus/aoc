import re

with open('input.txt') as f:
    results = [
        int(a) * int(b)
        for line in f
        for a, b in re.findall(r'mul\((\d+),(\d+)\)', line)
    ]

print(sum(results))