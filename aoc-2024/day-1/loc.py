with open('input.txt') as f:
    data = f.read().split()
    list = [int(x) for x in data]

list_one = list[::2]
list_one.sort()
list_two = list[1::2]
list_two.sort()

distance = [(x - y) for x,y in zip(list_one, list_two)]
abs_distance = [abs(n) for n in distance]

print("Distance Between: ", sum(abs_distance))

sim_scores = []

for n in list_one:
    occ = list_two.count(n)
    score = n * occ
    sim_scores.append(score)

print("Similarity Score: ", sum(sim_scores))

    





