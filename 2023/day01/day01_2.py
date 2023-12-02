import re

letterwords = ["one", "two", "three",
               "four", "five", "six", "seven", "eight",
               "nine"]
regex = "(" + "|".join(letterwords) + r"|\d)"


f = open("input01.txt", "r")
lines = f.readlines()
f.close()

res = 0
for line in lines:
    matches = list()
    for i in range(len(line)-1):
        m = re.findall(regex, line[i:])
        if m:
            matches.append(m[0])
    for i, match in enumerate(matches):
        if len(match) > 1:
            matches[i] = letterwords.index(match)+1
        else:
            matches[i] = int(match)

    val = matches[0]*10 + matches[-1]
    res += val
print(res)
