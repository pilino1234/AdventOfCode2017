

class Register:

    def __init__(self, name):
        self.name = name
        self.value = 0

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return "Register " + self.name + ": " + str(self.value)

    def __gt__(self, other):
        return self.value > other.value


class Condition:

    def __init__(self, reg, op, amount):
        self.reg = reg
        self.op = op
        self.amount = amount

    def evaluate(self):
        if self.op == "==":
            return self.reg.value == self.amount
        elif self.op == "!=":
            return self.reg.value != self.amount
        elif self.op == ">":
            return self.reg.value > self.amount
        elif self.op == "<":
            return self.reg.value < self.amount
        elif self.op == ">=":
            return self.reg.value >= self.amount
        elif self.op == "<=":
            return self.reg.value <= self.amount
        else:
            print("Invalid condition operator", self.op)


class Instruction:

    def __init__(self, reg, op, amount, cond):
        self.reg = reg
        self.op = op
        self.amount = amount
        self.cond = cond

    def evaluate(self):
        if self.cond.evaluate():
            if self.op == "inc":
                self.reg.value += self.amount
            elif self.op == "dec":
                self.reg.value -= self.amount
            else:
                print("Invalid instruction operator", self.op)


def parse_instructions(read):
    regs = {}
    instrux = []

    for line in read:
        parts = line.split()

        create_reg_if_not_exist(parts[0], regs)
        create_reg_if_not_exist(parts[4], regs)

        cond = Condition(regs[parts[4]], parts[5], int(parts[6]))
        instrux.append(Instruction(regs[parts[0]], parts[1], int(parts[2]), cond))

    return regs, instrux


def create_reg_if_not_exist(name, regs):
    if name not in regs.keys():
        reg = Register(name)
        regs.update({name: reg})


def evaluate(instrux, regs):
    highest = 0

    for ins in instrux:
        ins.evaluate()

        if max(regs.values()).value > highest:
            highest = max(regs.values()).value

    return highest


if __name__ == "__main__":
    with open("input.txt") as f:
        read_instructions = f.readlines()

    # read_instructions = [
    #    "b inc 5 if a > 1",
    #     "a inc 1 if b < 5",
    #     "c dec -10 if a >= 1",
    #     "c inc -20 if c == 10"
    # ]

    registers, instructions = parse_instructions(read_instructions)

    highest_reg_value = evaluate(instructions, registers)

    print("Largest register at end:", max(registers.values()))
    print("Largest register value during:", highest_reg_value)




