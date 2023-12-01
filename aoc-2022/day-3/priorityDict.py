import string

v = 0
items = list(string.ascii_letters)
values = []

for i in items:
    v += 1
    values.append(v)

priority = dict(zip(items, values))