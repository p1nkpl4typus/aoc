from priorityDict import priority

all_shared_items = []

def item_checker(c1, c2):
    shared_items = []
    for ch in c1:
        if ch in c2:
            shared_items.append(ch)
        else:
            continue
    return shared_items[0]

with open('input.txt') as f:
    for line in f:
        c1, c2 = line[:len(line)//2], line[len(line)//2:]
        results = item_checker(c1, c2)
        v = priority[results]
        all_shared_items.append(v)

print(sum(all_shared_items))
