import random
random.seed(0)

N_ROUNDS = int(1e6)

result = ""

for i in range(N_ROUNDS):
    result += chr(random.randint(0, 2) + 65) + " "
    result += chr(random.randint(0, 2) + 88) + "\n"

file = open("data/day02_large.txt", "w")
file.write(result)
file.close()
