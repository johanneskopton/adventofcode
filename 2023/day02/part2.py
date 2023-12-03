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
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for subset_str in subset_strs:
        color_strs = subset_str.split(", ")
        for color_str in color_strs:
            m = re.match(r"(\d+) (blue|red|green)", color_str)
            amount = int(m.group(1))
            color = m.group(2)
            if amount > min_cubes[color]:
                min_cubes[color] = amount
    power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    res += power

print(res)
