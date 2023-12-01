import re

digits = []
digits_dict = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def custom_parser(string):
    output = []
    for start in range(len(string)):
        found = False
        if string[start].isdigit():
            output.append(int(string[start]))
            continue
        for end in range(start + 1, len(string) + 1):
            sub_str = string[start:end]
            if sub_str in digits_dict:
                output.append(int(digits_dict[sub_str]))
                found = True
                break
        if found:
            continue
    return output

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        digits.append(custom_parser(line))

calibrations = []

for d in digits:
    first_element = d[0]
    last_element = d[-1:][0]
    new_digit = int(str(first_element) + str(last_element))
    calibrations.append(new_digit)

sum = sum(calibrations)
print(sum)
