from collections import defaultdict


def duet(ins):
    prog1 = defaultdict(int)
    prog2 = defaultdict(int)
    prog2['p'] = 1
    p2_send_count = 0

    progs = [prog1, prog2]
    pcs = [0, 0]
    queues = [[], []]
    states = ["ok", "ok"]

    current_program = 0
    registers = prog1
    pc = 0

    def parse(loc):
        if loc.isalpha():
            return registers[loc]
        return int(loc)

    while True:
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
            source = parse(value)

        if instruction == 'snd':
            if current_program == 1:
                p2_send_count += 1
            queues[current_program].append(parse(curr_ins[1]))

        elif instruction == 'set':
            registers[target] = source

        elif instruction == 'add':
            registers[target] += source

        elif instruction == 'mul':
            registers[target] *= source

        elif instruction == 'mod':
            registers[target] %= source

        elif instruction == 'rcv':
            # Check if other program has sent data
            if queues[1-current_program]:
                states[current_program] = "ok"
                registers[target] = queues[1-current_program].pop(0)
            else:  # Current program is waiting on receive
                # Check if we have a deadlock
                # are both programs terminated?
                if states[1-current_program] == "done":
                    break

                # is the other program waiting on receiving,
                # but we have not sent anything?
                if len(queues[current_program]) == 0 \
                        and states[1-current_program] == "waiting":
                    break

                # Otherwise, switch execution to other program
                pcs[current_program] = pc  # store PC
                states[current_program] = "waiting"  # store state
                current_program = 1 - current_program   # change program
                pc = pcs[current_program]  # load PC
                pc -= 1  # offset for incrementing pc below...
                registers = progs[current_program]  # load registers

        elif instruction == 'jgz':
            if parse(target) > 0:
                pc += source
                pc -= 1  # offset for incrementing pc below...

        pc += 1

        # Terminate PC if it goes out of range
        if not 0 <= pc < len(ins):
            # Both done
            if states[1-current_program] == "done":
                break

            states[current_program] = "done"

            # Switch back to other program
            pcs[current_program] = pc
            current_program = 1 - current_program  # change program
            pc = pcs[current_program]  # load PC
            registers = progs[current_program]  # load registers

    return p2_send_count


if __name__ == '__main__':
    with open("input.txt") as f:
        read_asm = [l.strip().split() for l in f]

    print(duet(read_asm))
