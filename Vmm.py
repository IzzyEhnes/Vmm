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

    num_memory_accesses = 0
    num_swap_ins = 0
    num_swap_outs = 0
    num_pages_malloced = 0
    total_memory_cycles = 0
    max_working_set_size = 0
    last_working_set_size = 0

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

        address = "0x" + memory_accesses[1][1]

        for operation in memory_accesses:
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
                Vmm.total_memory_cycles += constants.CYCLES_PER_VICTIM_SELECTION

                if PF[victim_index] == 1:
                    Vmm.num_swap_ins += 1
        
                PF[victim_index] = 1 # PF[victim_index] is now being used
                
                Vmm.PT[PT_index][1] = 1 # Page is now resident in memory
                
                Vmm.total_memory_cycles += constants.CYCLES_PER_SWAP

                # if data is swapped out before being written
                if memory_accesses[1][0] == 'w':
                    Vmm.num_swap_outs += 1

            P_index = Vmm.get_P_index(address)

            if memory_accesses[1][0] == 'w':
                # perform the write operation
                Vmm.P[P_index] = memory_accesses[1][2]
                Vmm.PT[PT_index][2] = 1 # Page has been modified
            #else:
                # read operation performed here [nothing happens during the simulation]

            Vmm.num_memory_accesses += 1


memory_accesses = Vmm.process_file()
Vmm.run_vmm(memory_accesses)

def print_output():
    print("* * * Paging Activity Statistics * * *  ")
    print("number of memory accesses       = ", Vmm.num_memory_accesses)
    print("number of triples (1 + access)  = ", Vmm.num_memory_accesses + 1)
    print("number of swap ins (faults)     = ", Vmm.num_swap_ins)
    print("number of swap outs             = ", Vmm.num_swap_outs)
    print("total number of pages malloced  = ", Vmm.num_pages_malloced)
    print("number of pages for Page Tables = ", 1)
    print("number of page frames for user  = ", )
    print("total memory cycles             = ", Vmm.total_memory_cycles )
    print("cycles w/o Vmm                  = ", Vmm.num_memory_accesses * 10)
    print("cycles per swap_in              = ", constants.CYCLES_PER_SWAP)
    print("cycles per swap_out             = ", constants.CYCLES_PER_SWAP)
    print("last working set size           = ", Vmm.working_set_size)
    print("max working set size ever       = ", Vmm.working_set_size)