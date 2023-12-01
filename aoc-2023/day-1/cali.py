digits = []

with open('input.txt') as f:
    for line in f:
        digits_per_line = []
        for c in line:
            if c.isdigit():
                num = int(c)
                digits_per_line.append(num)
        digits.append(digits_per_line)

calibrations = []

for d in digits:
    first_element = d[0]
    last_element = d[-1:][0]
    new_digit = int(str(first_element) + str(last_element))
    calibrations.append(new_digit)

sum = sum(calibrations)
print(sum)



