infile = open("data/day01_large.txt", "r")
calories_richest = [0, 0, 0]
calories_this = 0
active = True
while active:
    line = infile.readline()
    if not line:
        line = ''
        active = False
    line = line.strip()
    if line == '':
        id_third_richest = min(range(3), key=lambda i: calories_richest[i])
        calories_richest[id_third_richest] = max(
            calories_richest[id_third_richest], calories_this)
        calories_this = 0
    else:
        calories_this += int(line)
print("Part1: {}".format(max(calories_richest)))
print("Part2: {}".format(sum(calories_richest)))
