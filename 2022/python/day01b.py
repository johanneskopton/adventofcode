infile = open("data/day01_large.txt", "r")
data = infile.read()[:-1].split("\n\n")
data = [a.split("\n") for a in data]
for i in range(len(data)):
    data[i] = [int(a) for a in data[i]]
elves = sorted([sum(elve) for elve in data])
print("Part1:\t{}".format(elves[-1]))
print("Part2:\t{}".format(sum(elves[-3:])))
