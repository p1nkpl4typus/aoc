from priorityDict import priority
from itertools import islice

badges = []

def item_checker(c1, c2, c3):
    shared_items = []
    for ch in c1:
        if ch in c2 and ch in c3:
            shared_items.append(ch)
        else:
            continue
    return shared_items[0]

with open('input.txt') as f:
    rucksacks = f.read().splitlines()

n = 3

elves = [rucksacks[i * n:(i + 1) * n] for i in range((len(rucksacks) + n - 1 ) // n )]

for group in elves:
    c1 = group[0]
    c2 = group[1]
    c3 = group[2]
    results = item_checker(c1, c2, c3)
    v = priority[results]
    badges.append(v)

print(sum(badges))



