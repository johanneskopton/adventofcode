d = [a.strip() for a in open("data/day03_large.txt", "r").readlines()]
def s(a): return ord(a) - 96 if ord(a) >= 97 else ord(a) - 38
print("Part1:\t{}\nPart2:\t{}".format(sum([s(set.intersection(*a).pop()) for a in [[set(a[:len(a)//2]), set(a[len(a)//2:])]for a in d]]),
                                      sum([s(set.intersection(*[set(a)for a in d][n:n+3]).pop()) for n in range(0, len(d), 3)])))
