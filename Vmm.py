import constants

class Vmm:

    PD = [None] * constants.PD_SIZE
    PT = [None] * constants.PT_SIZE
    P = [None] * constants.PAGE_SIZE
    
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
        
        for i in input:
            print(i)
        
        print(len(input))

        return input

    def run_Vmm(memory_accesses):
        available_page_frames = memory_accesses[0][1]

memory_accesses = Vmm.process_file()
Vmm.run_Vmm(memory_accesses)
