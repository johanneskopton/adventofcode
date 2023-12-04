import re

f = open("input.txt", "r")
lines = f.readlines()
f.close()

res = 0

cards_no = [1] * len(lines)


for card_i, line in enumerate(lines):
    split1 = line.split(":")
    card_no = int(re.findall(r"Card\s+(\d+)", split1[0])[0])
    winning_str, have_str = split1[1].split("|")
    winning_numbers = re.split(r"\s+", winning_str.strip())
    have_numbers = re.split(r"\s+", have_str.strip())
    winning_numbers = set([int(a) for a in winning_numbers])
    have_numbers = set([int(a) for a in have_numbers])
    intersection = winning_numbers.intersection(have_numbers)
    no_intersection = len(intersection)

    for new_card_i in range(card_i+1, card_i+1+no_intersection):
        cards_no[new_card_i] += cards_no[card_i]

print(sum(cards_no))
