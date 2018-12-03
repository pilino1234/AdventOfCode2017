from collections import defaultdict


def duet(ins):
    registers = defaultdict(int)

    pc = 0
    last_played_freq = 0
    recovered = False

    while not recovered:
        curr_ins = ins[pc]
        instruction = curr_ins[0]

        # The first parameter to an instruction is always a register
        # If the register does not exist, create a new register initialized to 0
        # Store the register name in x
        target = curr_ins[1]

        # The second parameter may not exist, but if it exists it may either be a number
        # or a register name. If the register does not exist, create it (value 0)
        # Finally, store the value of the register (or None) in y
        source = None
        if len(curr_ins) == 3:
            value = curr_ins[2]
            if value.isalpha():
                source = registers[value]
            else:
                source = int(value)

        if instruction == 'snd':
            last_played_freq = registers[target]

        elif instruction == 'set':
            registers[target] = source

        elif instruction == 'add':
            registers[target] += source

        elif instruction == 'mul':
            registers[target] *= source

        elif instruction == 'mod':
            registers[target] %= source

        elif instruction == 'rcv':
            if registers[target] != 0:
                recovered = True

        elif instruction == 'jgz':
            if target.isnumeric():
                val = int(target)
            else:
                val = registers[target]
            if val > 0:
                pc += source
                continue

        pc += 1

    return last_played_freq


if __name__ == '__main__':
    with open("input.txt") as f:
        read_asm = [l.strip().split() for l in f]

    print(duet(read_asm))
