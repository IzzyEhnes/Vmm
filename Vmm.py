import constants
import random

class Vmm:
    
    # no Page Tables exist in the Page Directory yet
    PD = [0] * constants.PD_SIZE

    # no Pages exist in the Page Table yet,
    # they are not resident in memory, and have not been modified
    PT = [[0, 0, 0]] * constants.PT_SIZE

    # no Page Frames exist in the Page Directory yet
    P = [0] * constants.P_SIZE

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
        available_PFs = int(memory_accesses[0][1])

        # available page frames; none used yet so all elements are set to 0
        PF = [0] * available_PFs

        print(PF)

        if memory_accesses[1][0] == 'w':
            address = "0x" + memory_accesses[1][1]
            print(address)

            # looking for specific Page Table in the Page Directory
            PD_index = Vmm.get_PD_index(address)
            if Vmm.PD[PD_index] == 0:
                Vmm.PD[PD_index] = 1

            # looking for specific Page in the Page Table
            PT_index = Vmm.get_PT_index(address)
            if Vmm.PT[PT_index][0] == 0:
                Vmm.PT[PT_index][0] = 1

            # if page exists but is not resident in memory, swap it into a random Page Frame
            if Vmm.PT[PT_index][0] == 1 and Vmm.PT[PT_index][1] == 0:
                victim_index = random.randrange(0, available_PFs - 1)
                PF[victim_index] = 1 # PF[victim_index] is now being used
                Vmm.PT[PT_index][1] = 1 # Page is now resident in memory


memory_accesses = Vmm.process_file()
Vmm.run_vmm(memory_accesses)
#print(Vmm.PD[0])

#print(Vmm.P)
