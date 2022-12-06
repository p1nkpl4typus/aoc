elf_signal = []
marker_check = []
processed = 0

to_check = 14

with open('input.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        elf_signal.append(c)

for ch in elf_signal:
    processed += 1
    marker_check.append(ch)
    if len(marker_check) > to_check:
        marker_check.pop(0)
    if len(marker_check) < to_check:
        continue
    if len(marker_check) != len(set(marker_check)):
        print(marker_check, processed, 'Duplicated Character')
    else:
        print(marker_check, processed, 'No Duplicates')
        break