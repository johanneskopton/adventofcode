infile = open("data/day02_large.txt", "r")
total_score1 = 0
total_score2 = 0
while True:
    line = infile.readline()[:-1]
    if not line:
        break
    a, b = line.split(" ")
    # Part 1
    enemy = ord(a) - 65
    me = ord(b) - 88
    shape_score1 = me + 1
    outcome_score1 = (me - enemy + 1) % 3 * 3
    total_score1 += shape_score1 + outcome_score1
    # Part 2
    result = me
    me = (enemy + result - 1) % 3
    shape_score2 = me + 1
    outcome_score2 = result * 3
    total_score2 += shape_score2 + outcome_score2
print("Part1:\t{}".format(total_score1))
print("Part2:\t{}".format(total_score2))
