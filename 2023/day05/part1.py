import re


def apply_map(iinput, mmap):
    for rrange in mmap:
        if iinput >= rrange[1] and iinput < rrange[1] + rrange[2]:
            return iinput - rrange[1] + rrange[0]
    return iinput


f = open("input.txt", "r")
lines = f.readlines()
f.close()

seeds = [int(a) for a in lines[0].strip().split(" ")[1:]]


maps = []

for line in lines[2:]:
    if line == "\n":
        continue
    if re.match(r"[a-z]", line):
        maps.append([])
        continue
    range_params = [int(a) for a in line.strip().split(" ")]
    maps[-1].append(range_params)


locations = []
for seed in seeds:
    iinput = seed
    for mmap in maps:
        iinput = apply_map(iinput, mmap)
    locations.append(iinput)

print(min(locations))
