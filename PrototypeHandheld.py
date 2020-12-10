class Handheld:
    def __init__(self, lines):
        self.ip = 0
        self.a = 0
        self.prog = []
        self.visited = set()
        for line in lines:
            inst, val = line.split()
            self.prog.append([inst, int(val)])
        self.inst = {
            "nop": self.nop,
            "acc": self.acc,
            "jmp": self.jmp
        }

    # instructions

    def nop(self, _):
        self.ip += 1

    def acc(self, val):
        self.a += val
        self.ip += 1

    def jmp(self, val):
        self.ip += val

    # runs the program until it detects an infinite loop or a jump outside of the program
    def run(self):
        while True:
            if self.ip not in self.visited:
                self.visited.add(self.ip)
            else:
                return "loops", self.a

            if self.ip >= len(self.prog):
                return "terminates", self.a

            self.inst[self.prog[self.ip][0]](self.prog[self.ip][1])
