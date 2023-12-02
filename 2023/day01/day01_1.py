import re

f = open("input01.txt", "r")
lines = f.readlines()
f.close()

res = 0
for line in lines:
    m = re.findall(r"(\d)", line)
    res += int(m[0] + m[-1])
print(res)
