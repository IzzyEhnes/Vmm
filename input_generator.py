import random

f = open("input2.txt", "a")

all_lines = "p     9\n"

num_lines = 10

possible_addresses = list()

# we want some repeats when running out simulation, so make a pseudo-random list that scales with number of lines
for x in range(num_lines):
    possible_addresses.append(random.randrange(1000, 10000))

w_or_r = ["w", "r", "r"]

for line in range(num_lines):
    temp_line = ""
    for operation in range(5):
        op = random.choice(w_or_r)

        if op == "w":
            address = random.choice(possible_addresses)
            value = random.randrange(0, 9)
            temp_line += f'{"w": <3} {str(address)} {str(value)}  '

        if op == "r":
            address = random.choice(possible_addresses)
            temp_line += f'{"r": <3} {str(address)}    '
    all_lines += temp_line + '\n'

print(all_lines)

f.write(all_lines)