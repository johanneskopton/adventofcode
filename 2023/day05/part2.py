import re


def apply_map(input_range, mmap):
    # takes range, outputs list of ranges

    # for i, rrange in enumerate(mmap):
    if mmap:
        res = []
        rrange = mmap[0]
        source_range = (rrange[1], rrange[1] + rrange[2])
        shift = rrange[0] - rrange[1]

        print(source_range)
        print(input_range)
        if input_range[0] < source_range[0]:
            print("A")
            range_start = input_range[0]
            range_end = min(input_range[1], source_range[0])
            res.extend(apply_map((range_start, range_end), mmap[1:]))
        if input_range[1] > source_range[1]:
            print("B")
            range_start = max(input_range[0], source_range[1])
            range_end = input_range[1]
            res.extend(apply_map((range_start, range_end), mmap[1:]))
        if input_range[0] < source_range[1] and\
                input_range[1] > source_range[0]:
            print("C")
            range_start = max(source_range[0], input_range[0])
            range_end = min(source_range[1], input_range[1])
            res.append((range_start+shift, range_end+shift))
        print(res)
        return res
    else:
        return [input_range]


f = open("input.txt", "r")
lines = f.readlines()
f.close()

seed_ints = [int(a) for a in lines[0].strip().split(" ")[1:]]

seed_ranges = []
for i, seed_int in enumerate(seed_ints):
    if i % 2 == 0:
        range_start = seed_int
    else:
        seed_ranges.append((range_start, seed_int+range_start))


maps = []

for line in lines[2:]:
    if line == "\n":
        continue
    if re.match(r"[a-z]", line):
        maps.append([])
        continue
    range_params = [int(a) for a in line.strip().split(" ")]
    maps[-1].append(range_params)

# seed_ranges = [seed_ranges[0]]
# maps = [maps[0]]

input_ranges = seed_ranges
for mmap in maps:
    next_input_ranges = []
    # print(input_ranges)
    for input_range in input_ranges:
        next_input_ranges.extend(apply_map(input_range, mmap))
    input_ranges = next_input_ranges

location_range_starts = [a[0] for a in input_ranges]


print(min(location_range_starts))
