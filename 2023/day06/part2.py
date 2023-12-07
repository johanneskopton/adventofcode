import re
import math
import numpy as np

f = open("input.txt", "r")
lines = f.readlines()
f.close()

times = re.split(r"\s+", lines[0])[1:-1]
distances = re.split(r"\s+", lines[1])[1:-1]

time = ""
for time_str in times:
    time += time_str

distance = ""
for distance_str in distances:
    distance += distance_str

times = [int(time)]
distances = [int(distance)]

ways_to_win = list()
for i in range(len(times)):
    t = times[i]
    d = distances[i]
    pm = math.sqrt(t**2/4 - d)
    lower = math.floor(t/2 - pm)
    upper = math.ceil(t/2 + pm)
    ways_to_win.append(upper-lower-1)

print(np.product(ways_to_win))


"""
d(p, t) = (t-p) * p = t*p - p**2
t*p - p**2 = d

p**2 - t*p + d = 0

p_{1,2} = t/2 +- sqrt(t**2/4 - d)

2 * sqrt(t**2/4 - d)
"""
