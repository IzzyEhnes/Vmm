def process_file():
    with open('inputs/input1.txt','r') as f:
        contents = f.read()
        
    line = " ".join(contents.split()).split()

    input = list()

    for element in line:
        if element == 'p' or element == 'r':
            input.append(line[:2])
            line = line[2:]
        elif element == 'w':
            input.append(line[:3])
            line = line[3:]

process_file()
