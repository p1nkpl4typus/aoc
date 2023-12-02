import re
from functools import reduce
import operator

powers = []

with open('input.txt') as f:
    for line in f:
        stats = re.split('[:]', line)
        game_id = re.split(' ', stats[0])

        revealed = re.split('[;]', stats[1])
        possible = []
        max_colors = {'red': 0, 'blue': 0, 'green': 0}

        for reveal in revealed:

            color_counts = re.findall('(\d+) (\w+)', reveal)

            for count, color in color_counts:
                if int(count) > max_colors[color]:
                    max_colors[color] = int(count)

        values = list(max_colors.values())

        power = reduce(operator.mul, map(int, values))
        powers.append(power)

print(sum(powers))
