infile = open("data/day02_large.txt", "r")
data = [a.strip().split(" ") for a in infile.readlines()]
data = [[ord(a[0]) - 65, ord(a[1]) - 88] for a in data]
score1 = sum([a[1] + 1 + (a[1] - a[0] + 1) % 3 * 3 for a in data])
score2 = sum([(a[0] + a[1] - 1) % 3 + 1 + a[1]*3 for a in data])
print("Part1:\t{}".format(score1))
print("Part2:\t{}".format(score2))
