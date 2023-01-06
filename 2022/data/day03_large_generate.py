import random

random.seed(0)

N_GROUPS = int(1e5)

charset = set()
for i in range(52):
    charset.add(chr(i + 97 if i < 26 else i + 39))

def pop_random(charset):
    charset = charset.copy()
    element = random.choice(tuple(charset))
    charset.remove(element)
    return element, charset

result = ""

for i in range(N_GROUPS):
    group_common, group_charset = pop_random(charset)
    for j in range(3):
        rucksack_charset = set(random.choices(tuple(group_charset), k=17))
        rucksack_charset.add(group_common)
        group_charset -= rucksack_charset

        compartment_common, compartment_charset = pop_random(rucksack_charset)
        left_compartment = set(random.choices(tuple(rucksack_charset), k=8))
        right_compartment = compartment_charset - left_compartment

        left_compartment.add(compartment_common)
        right_compartment.add(compartment_common)

        left_str = "".join(left_compartment)
        right_str = "".join(right_compartment)
        
        compartment_len = random.randint(max(len(left_str), len(right_str)), 24)
        for k in range(compartment_len-len(left_str)):
            left_str += random.choice(tuple(left_compartment))
        for k in range(compartment_len-len(right_str)):
            right_str += random.choice(tuple(right_compartment))
        result += left_str + right_str + "\n"

file = open("data/day03_large.txt", "w")
file.write(result)
file.close()
