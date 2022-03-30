def process_file():
    with open('inputs/input1.txt','r') as f:
        contents = f.readlines()

    lines = list()

    for line in contents:
        line = " ".join(line.split()).split()
        lines.append(line)

    print(lines)

process_file()
