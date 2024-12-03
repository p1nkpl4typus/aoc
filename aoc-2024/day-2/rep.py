with open('input.txt') as f:
    data = f.read().splitlines()

min_diff = 0
max_diff = 4
safe_reports = []

def is_increasing(lst):
    return all(x<=y for x, y in zip(lst, lst[1:]))

def is_decreasing(lst):
    return all(x>=y for x, y in zip(lst, lst[1:]))

def monotonic(lst):
    return is_decreasing(lst) or is_increasing(lst)

def is_safe(lst, min_diff, max_diff):
    level_diff = [abs(x - y) for x, y in zip(lst, lst[1:])]
    return all(min_diff < e < max_diff for e in level_diff)

for row in data:
    report = [int(e) for e in row.split()]
    if monotonic(report) and is_safe(report, min_diff, max_diff):
        safe_reports.append(report)

print(len(safe_reports))

