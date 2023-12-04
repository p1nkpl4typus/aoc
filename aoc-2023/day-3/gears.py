"""
CLOSE - BUT NO CIGAR
This is so convoluted...haha
Can't figure out how to account for numbers like 123.456 in the upper and lower rows, which is causing my sum to be off.....
And now I am tired.
Star 2 is a no go for 2023.....
"""

from functools import reduce
import operator

parts_list = []
gear_ratios = []

def contains_digit(lst):
    return any(char.isdigit() for char in lst)

with open('input.txt') as f:
    for line in f:
        line.strip()
        row = []
        for c in line:
            if c == '\n':
                continue
            else:
                row.append(c)
        parts_list.append(row)

for row in range(len(parts_list)):
    curr_row = parts_list[row]
    if row == 0:
        prev_row = []
    else:
        prev_row = parts_list[row - 1]

    if row == len(parts_list) - 1:
        next_row = []
    else:
        next_row = parts_list[row + 1]

    index = 0
    num = []
    char_check = []
    for c in curr_row:
        if c != '*':
            index += 1
            continue
        else:
            if index > 0 and (index < len(prev_row) - 1):
                prev_char = curr_row[index - 1]
                ul_char = prev_row[index - 1]
                uc_char = prev_row[index]
                ur_char = prev_row[index + 1]
            else:
                prev_char = ''
                ul_char = ''
                uc_char = ''
                ur_char = ''

            if index < len(curr_row) - 1:
                next_char = curr_row[index + 1]
            else:
                next_char = ''

            if (index < len(next_row) - 1):
                ll_char = next_row[index - 1]
                lc_char = next_row[index]
                lr_char = next_row[index + 1]
            else:
                ll_char = ''
                lc_char = ''
                lr_char = ''

            prev_adj = ''
            next_adj = ''
            upper_adj = ''
            below_adj = ''
            all_adj = []

            if prev_char.isdigit():
                for i in range(index - 1, -1, -1):
                    if not curr_row[i].isdigit():
                        break
                    prev_adj = curr_row[i] + prev_adj

            if next_char.isdigit():
                for i in range(index +1, len(curr_row)):
                    if not curr_row[i].isdigit():
                        break
                    next_adj += curr_row[i]

            if ul_char.isdigit() or uc_char.isdigit() or ur_char.isdigit():
                upper_adj_list = []
                upper_adj_before = prev_row[index] if prev_row[index].isdigit() else ''
                upper_adj_after = prev_row[index] if prev_row[index].isdigit() else ''

                for i in range(index - 1, -1, -1):
                    if not prev_row[i].isdigit():
                        upper_adj_list.append(upper_adj_before)
                        break
                    upper_adj_before = prev_row[i] + upper_adj_before
                for i in range(index + 1, len(prev_row)):
                    if not prev_row[i].isdigit():
                        upper_adj_list.append(upper_adj_after)
                        break
                    upper_adj_after = upper_adj_after + prev_row[i]

            if ll_char.isdigit() or lc_char.isdigit() or lr_char.isdigit():
                below_adj_list = []
                below_adj_before = next_row[index] if next_row[index].isdigit() else ''
                below_adj_after = next_row[index] if next_row[index].isdigit() else ''

                for i in range(index - 1, -1, -1):
                    if not next_row[i].isdigit():
                        break
                    below_adj_before = next_row[i] + below_adj_before
                    below_adj_list.append(below_adj_before)
                for i in range(index + 1, len(next_row)):
                    if not next_row[i].isdigit():
                        break
                    below_adj_after = below_adj_after + next_row[i]
                    below_adj_list.append(below_adj_after)

            if upper_adj: all_adj.append(int(upper_adj))
            if prev_adj: all_adj.append(int(prev_adj))
            if next_adj: all_adj.append(int(next_adj))
            if below_adj: all_adj.append(int(below_adj))

            if len(all_adj) == 1:
                print(f"row: {row + 1} -- {all_adj}")
            print(f"{row - 2 } -- TEST UPPER: {upper_adj_list}")
            print(f"{row + 2} -- TEST LOWER: {below_adj_list}")

            if len(all_adj) == 2:
                gear_ratio = reduce(operator.mul, all_adj)
                gear_ratios.append(gear_ratio)

            index += 1

print(sum(gear_ratios))
