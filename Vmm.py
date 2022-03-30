def read_file():
    with open('inputs/input1.txt','r') as f:
        contents = f.readlines()
    print(contents)

read_file()
