import heapq
infile = open("data/day01_large.txt", "r")
data = infile.read()[:-1].split("\n\n")
data = [a.split("\n") for a in data]
data = [[int(a) for a in elve] for elve in data]
elves = [sum(elve) for elve in data]
print("Part1:\t{}".format(max(elves)))
print("Part2:\t{}".format(sum(heapq.nlargest(3, elves))))
