infile = open("data/day03_input.txt", "r")
data = [a.strip() for a in infile.readlines()]
data_halves = [[set(a[:len(a)//2]), set(a[len(a)//2:])] for a in data]
data = [set(a) for a in data]
def score(a): return ord(a) - 96 if ord(a) >= 97 else ord(a) - 38
score1 = sum([score(set.intersection(*a).pop()) for a in data_halves])
score2 = sum([score(set.intersection(*data[n:n+3]).pop()) for n in range(0, len(data), 3)])
print("Part1:\t{}\nPart2:\t{}".format(score1, score2))
