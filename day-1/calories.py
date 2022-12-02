import numpy as np

total_calories = np.array([])
calories = 0

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            line = 0
            total_calories = np.append(total_calories, calories)
            calories = 0
        else:
            calories += int(line)

top_elf = np.argmax(total_calories)

#Answer 1
print("The elf carrying the most calories is " + str(top_elf) + " with a total of " + str(total_calories[top_elf]) + " calories.")

print("------")

#Answer 2
top_elves = np.argsort(total_calories)[::-1][:3]
shared_calories = 0
for e in top_elves:
    shared_calories += total_calories[e]

print("The top 3 elves are carrying " + str(shared_calories) + " calories.")

