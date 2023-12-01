floor = 0
floor_num = []

with open('input.txt') as f:
    for line in f:
        for c in line:
            if c == "(":
                floor += 1
                floor_num.append(floor)
            elif c == ")":
                floor -= 1
                floor_num.append(floor)

print(f"Go to floor: {floor}") # star 1
print(f"You will hit the basement in position: {floor_num.index(-1)+1}") # star 2
