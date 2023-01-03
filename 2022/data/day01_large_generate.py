import random
random.seed(0)

N_ELVES = int(5e4)

result = ""

for i in range(N_ELVES):
    items = max(1, int(random.normalvariate(10, 7)))
    for j in range(items):
        calories = random.randint(1000, 10000)
        result += "{}\n".format(calories)
    if i < N_ELVES-1:
        result += "\n"

file = open("data/day01_large.txt", "w")
file.write(result)
file.close()
