import re

start = re.match(r'do\(\)')
stop = re.match(r"don't\(\)")

memory = [
    match
    for line in open('input.txt')
    for match in re.findall(r"do\(\)(.*?)(?=don't\(|$)", line)
]

print(memory)

# with open('input.txt') as f:
#     results = [
#         int(a) * int(b)
#         for line in f
#         for a, b in re.findall(r'mul\((\d+),(\d+)\)', line)
#     ]

# print(sum(results))