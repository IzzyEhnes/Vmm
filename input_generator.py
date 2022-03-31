import random

f = open("input2.txt", "a")
f.write("p     9")

num_lines = 10

w_or_r = ["w", "r", "r"]

for line in range(num_lines):
    temp_line = ""
    for operation in range(5):
        op = random.choice(w_or_r)
        temp_line += op + " "
    print(temp_line)