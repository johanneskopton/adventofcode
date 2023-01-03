infile = open("data/day01_large.txt", "r")
data = infile.read()[:-1].split("\n\n")
data = [a.split("\n") for a in data]
data = [[int(a) for a in elve] for elve in data]
elves = sorted([sum(elve) for elve in data])
print("Part1:\t{}".format(elves[-1]))
print("Part2:\t{}".format(sum(elves[-3:])))
