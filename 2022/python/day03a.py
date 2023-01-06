infile = open("data/day03_large.txt", "r")
total_score1 = 0
total_score2 = 0
i = 0
rucksacks = []


def score(character):
    code = ord(character)
    score = code - 96 if code >= 97 else code - 38
    return score


while True:
    line = infile.readline()[:-1]
    if not line:
        break
    # Part 1
    halflen = int(len(line)/2)
    firsthalf = line[:halflen]
    for a in line[halflen:]:
        if a in firsthalf:
            total_score1 += score(a)
            break
    # Part 2
    if i == 2:
        for a in line:
            if a in rucksacks[0] and a in rucksacks[1]:
                total_score2 += score(a)
                break
        i = 0
        rucksacks = []
    else:
        i += 1
        rucksacks.append(line)

print("Part1:\t{}".format(total_score1))
print("Part2:\t{}".format(total_score2))
