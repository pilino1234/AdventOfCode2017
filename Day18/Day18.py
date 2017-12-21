
def duet(ins):
    registers = {}

    pc = 0
    last_played_freq = -1
    recovered = False

    while not recovered:
        curr_ins = ins[pc]

        # The first parameter to an instruction is always a register
        # If the register does not exist, create a new register initialized to 0
        # Store the register name in x
        a = curr_ins[1]
        if a not in registers.keys():
            registers.update({a: 0})
        x = a

        # The second parameter may not exist, but if it exists it may either be a number
        # or a register name. If the register does not exist, create it (value 0)
        # Finally, store the value of the register (or None) in y
        y = None
        if len(curr_ins) == 3:
            b = curr_ins[2]
            if b.isnumeric() or b.startswith('-'):
                y = int(b)
            elif b.isalpha():
                if b not in registers.keys():
                    registers.update({b: 0})
                y = registers[b]
            else:
                raise TypeError("Unknown type of parameter 2 to instruction '{}'".format(" ".join(curr_ins)))

        instruction = curr_ins[0]

        if instruction == 'snd':
            last_played_freq = registers[x]

        elif instruction == 'set':
            registers[x] = y

        elif instruction == 'add':
            registers[x] += y

        elif instruction == 'mul':
            registers[x] *= y

        elif instruction == 'mod':
            registers[x] %= y

        elif instruction == 'rcv':
            if registers[x] != 0:
                recovered = True

        elif instruction == 'jgz':
            if registers[x] > 0:
                pc += y
                continue

        pc += 1

    return last_played_freq


if __name__ == '__main__':
    with open("input.txt") as f:
        read_asm = [l.strip().split() for l in f]

#    read_asm = [
#        "set a 1",
#        "add a 2",
#        "mul a a",
#        "mod a 5",
#        "snd a",
#        "set a 0",
#        "rcv a",
#        "jgz a -1",
#        "set a 1",
#        "jgz a -2"
#    ]
#    read_asm = [l.split() for l in read_asm]

    last_played_frequency = duet(read_asm)

    print("Part 1:", last_played_frequency)
