import re
import numpy as np

f = open("input.txt", "r")
lines = f.readlines()
f.close()

number_coordinate_list = list()
number_value_list = list()

for line_i, line in enumerate(lines):
    m = re.search(r"(\d+)", line)
    matches = list()
    pos = 0
    while m:
        matches.append(m)
        x_coords = pos + np.arange(m.start(1), m.end(1))
        y_coords = np.ones_like(x_coords) * line_i
        coords = np.column_stack([x_coords, y_coords])
        number_value_list.append(int(m.group(1)))
        number_coordinate_list.append(coords)

        pos += m.end(1)
        m = re.search(r"(\d+)", line[pos:])

symbol_coordinate_list = list()
symbol_value_list = list()

for line_i, line in enumerate(lines):
    m = re.search(r"(\*|\+|\#|\$|\&|\@|\/|\-|\=|\%)", line)
    matches = list()
    pos = 0
    while m:
        matches.append(m)
        x_coords = pos + m.start(1)
        y_coords = line_i
        coords = np.array([x_coords, y_coords])
        symbol_value_list.append(m.group(1))
        symbol_coordinate_list.append(coords)

        pos += m.end(1)
        m = re.search(r"(\*|\+|\#|\$|\&|\@|\/|\-|\=|\%)", line[pos:])

res = 0

for symbol_i in range(len(symbol_value_list)):
    if symbol_value_list[symbol_i] != "*":
        continue
    symbol_coords = symbol_coordinate_list[symbol_i]
    gear_candidate_number_idx_list = set()
    for number_i in range(len(number_value_list)):
        number_coords = number_coordinate_list[number_i]
        for digit_i in range(number_coords.shape[0]):
            digit_coods = number_coords[digit_i, :]
            is_adjacent = (np.absolute(digit_coods - symbol_coords) <= 1).all()
            if is_adjacent:
                gear_candidate_number_idx_list.add(number_i)
    if len(gear_candidate_number_idx_list) == 2:
        gear_ratio = 1
        for adjacent_number_id in gear_candidate_number_idx_list:
            gear_ratio *= number_value_list[adjacent_number_id]
        res += gear_ratio


print(res)
