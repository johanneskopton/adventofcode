import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

number_coordinate_list_x = list()
number_coordinate_list_y = list()
number_value_list = list()

for line_i, line in enumerate(lines):
    m = re.search(r"(\d+)", line)
    matches = list()
    pos = 0
    while m:
        matches.append(m)
        coords_x = [pos + a for a in range(m.start(1), m.end(1))]
        coords_y = [line_i] * len(coords_x)
        number_value_list.append(int(m.group(1)))
        number_coordinate_list_x.append(coords_x)
        number_coordinate_list_y.append(coords_y)

        pos += m.end(1)
        m = re.search(r"(\d+)", line[pos:])

symbol_coordinate_list_x = list()
symbol_coordinate_list_y = list()
symbol_value_list = list()

for line_i, line in enumerate(lines):
    m = re.search(r"(\*|\+|\#|\$|\&|\@|\/|\-|\=|\%)", line)
    matches = list()
    pos = 0
    while m:
        matches.append(m)
        coords_x = pos + m.start(1)
        coords_y = line_i
        symbol_value_list.append(m.group(1))
        symbol_coordinate_list_x.append(coords_x)
        symbol_coordinate_list_y.append(coords_y)

        pos += m.end(1)
        m = re.search(r"(\*|\+|\#|\$|\&|\@|\/|\-|\=|\%)", line[pos:])

adjacent_number_ids_set = set()

for symbol_i in range(len(symbol_value_list)):
    symbol_coords_x = symbol_coordinate_list_x[symbol_i]
    symbol_coords_y = symbol_coordinate_list_y[symbol_i]
    for number_i in range(len(number_value_list)):
        number_coords_x = number_coordinate_list_x[number_i]
        number_coords_y = number_coordinate_list_y[number_i]
        for digit_i in range(len(number_coords_x)):
            digit_coods_x = number_coords_x[digit_i]
            digit_coods_y = number_coords_y[digit_i]
            is_adjacent = (abs(digit_coods_x - symbol_coords_x) <= 1) and \
                (abs(digit_coods_y - symbol_coords_y) <= 1)
            if is_adjacent:
                adjacent_number_ids_set.add(number_i)

res = 0
for adjacent_number_id in adjacent_number_ids_set:
    res += number_value_list[adjacent_number_id]

print(res)
