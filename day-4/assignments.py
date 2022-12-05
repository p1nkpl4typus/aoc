range_convert = []
intersects = 0
overlaps = 0

def overlap(start1, end1, start2, end2):
    return end1 >= start2 and end2 >= start1

with open('input.txt') as f:
    assignments = f.read().splitlines()
    for a in assignments:
        r = a.split(',')
        ranges = [i.split('-') for i in r]
        range_convert.append(ranges)

for group in range_convert:
    r1 = [int(r) for r in group[0]]
    r2 = [int(r) for r in group[1]]
    arange1 = range(r1[0], r1[1]+1)
    arange2 = range(r2[0], r2[1]+1)
    compare = set(arange1).intersection(set(arange2))
    if compare == set(arange1) or compare == set(arange2):
        intersects += 1
    if overlap(r1[0], r1[1], r2[0], r2[1]) == True:
        overlaps +=1

print(overlaps)