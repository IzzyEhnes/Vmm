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

        return input


    def get_bits(num, k, i):

        # convert number into binary
        binary = bin(num)

        # remove '0b' from beginning of string
        binary = binary[2:].zfill(32)

        if i + k > len(binary):
            end = len(binary) - 1
        else:
            end = i + k

        # extract k bit sub-string
        bit_substr = binary[i : end + 1]

        # convert extracted sub-string back into decimal
        return int(bit_substr, 2)


    def get_PD_index(address):
        return Vmm.get_bits(int(address, 0), 10, 0)


    def get_PT_index(address):
        return Vmm.get_bits(int(address, 0), 10, 10)


    def get_P_index(address):
        return Vmm.get_bits(int(address, 0), 12, 22)


    def run_vmm(memory_accesses):
        available_page_frames = memory_accesses[0][1]

        if memory_accesses[1][0] == 'w':
            address = "0x" + memory_accesses[1][1]
            print(address)
            PD_index = Vmm.get_PD_index(address)
            print(PD_index)
            
            if Vmm.PD[PD_index] == None:
                Vmm.PD[PD_index] = 1

            



memory_accesses = Vmm.process_file()
Vmm.run_vmm(memory_accesses)
print(Vmm.PD[0])