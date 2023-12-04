parts_list = []
part_nums = []

def contains_special_character(lst):
    return any(char and not char.isdigit() and char != '.' for char in lst)

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
        if not c.isnumeric():
            index += 1
            if num and any(char_check):
                num = int(''.join(num))
                part_nums.append(num)
            num = []
            char_check = []
            continue
        else:
            num.append(c)
            if index > 0 and (index < len(prev_row) - 1):
                prev_char = curr_row[index - 1]
                upper_adj_chars = [prev_row[index -1], prev_row[index], prev_row[index + 1]]
            else:
                prev_char = ''
                upper_adj_chars = ''

            if index < len(curr_row) - 1:
                next_char = curr_row[index + 1]
            else:
                next_char = ''

            if (index < len(next_row) - 1):
                lower_adj_chars = [next_row[index - 1], next_row[index], next_row[index + 1]]
            else:
                lower_adj_chars = ''

            all_adj = [prev_char, next_char]
            if isinstance(upper_adj_chars, list):
                all_adj.extend(upper_adj_chars)
            if isinstance(lower_adj_chars, list):
                all_adj.extend(lower_adj_chars)
            char_check.append(contains_special_character(all_adj))
            index += 1

print(f"Your answer should be: {sum(part_nums) + 848}. Fingers crossed!")
