import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

max_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

res = 0
for line in lines:
    regex = r"Game (\d+): ([\s\S]*)"
    m = re.match(regex, line[:-1])
    game_id = int(m.group(1))
    game_str = m.group(2)
    subset_strs = game_str.split("; ")
    game_possible = True
    for subset_str in subset_strs:
        color_strs = subset_str.split(", ")
        for color_str in color_strs:
            m = re.match(r"(\d+) (blue|red|green)", color_str)
            amount = int(m.group(1))
            color = m.group(2)
            if amount > max_cubes[color]:
                game_possible = False
    if game_possible:
        res += game_id

print(res)
