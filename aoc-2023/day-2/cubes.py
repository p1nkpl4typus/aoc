max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def under_max_cubes(cube_list, max_cubes):
    return {cube_info: int(count) > max_cubes[color] for cube_info in cube_list
                                                        for count, color in [cube_info.strip().split()]
                                                        if color in max_cubes}

def all_false(dic):
    return all(not val for val in dic.values())

def true_keys(dic):
    return [key for key, val in dic.items() if val]

game = {}

with open('input.txt') as f:
    for i, line in enumerate(f, start=1):
        stats = line.strip().split(':')
        revealed = stats[1].split(';')
        game[i] = all(all_false(under_max_cubes(reveal.split(', '), max_cubes)) for reveal in revealed)

print(sum(true_keys(game)))
