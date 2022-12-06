import re
starting_stacks = []
crane_moves = []

def cratemover9000(num, start, end):
    i = 0
    while i < num:
        starting_stacks[end-1].append(starting_stacks[start-1][-1])
        starting_stacks[start-1].pop()
        i += 1
    return starting_stacks

def cratemover9001(num, start, end):
    crates = starting_stacks[start-1][-num:]
    starting_stacks[end-1].extend(crates)
    del starting_stacks[start-1][-num:]
    return starting_stacks

with open('input.txt') as f:
    lines = f.readlines()[0:9]
    ship = list(zip(*lines))
    stacks = [s for s in ship if s[-1] != ' ']
    del stacks[-1]
    stacks = [[i for i in s if i != ' '] for s in stacks]
    for s in stacks:
        stack = list(reversed(s))
        starting_stacks.append(stack)

with open('input.txt') as txtinput:
    moves = txtinput.readlines()[10:]
    moves = [item.strip() for item in moves]
    for each in moves:
        values = [int(s) for s in re.findall(r'\b\d+\b', each)]
        crane_moves.append(values)

for each in crane_moves:
    num = each[0]
    start = each[1]
    end = each[2]
    cratemover9001(num, start, end)

top = [item[-1] for item in starting_stacks]

print("Top crates are:", top)


    

        
    