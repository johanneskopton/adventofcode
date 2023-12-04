import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

res = 0
for line in lines:
    split1 = line.split(":")
    card_no = int(re.findall(r"Card\s+(\d+)", split1[0])[0])
    winning_str, have_str = split1[1].split("|")
    winning_numbers = re.split(r"\s+", winning_str.strip())
    have_numbers = re.split(r"\s+", have_str.strip())
    winning_numbers = set([int(a) for a in winning_numbers])
    have_numbers = set([int(a) for a in have_numbers])
    intersection = winning_numbers.intersection(have_numbers)
    no_intersection = len(intersection)
    points = 0
    if no_intersection > 0:
        points = 2**(no_intersection-1)
    res += points

print(res)
