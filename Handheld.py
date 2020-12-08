class Handheld:
    def __init__(self):
        self.ip = 0
        self.acc = 0
        self.prog = []
        self.visited = set()

    def load(self, lines):
        for line in lines:
            inst, val = line.split()
            self.prog.append([inst, int(val)])

    def run(self):
        while True:
            if self.ip not in self.visited:
                self.visited.add(self.ip)
            else:
                return "loops", self.acc
            if self.ip >= len(self.prog):
                return "terminates", self.acc
            if self.prog[self.ip][0] == "nop":
                self.ip += 1
            elif self.prog[self.ip][0] == "acc":
                self.acc += self.prog[self.ip][1]
                self.ip += 1
            elif self.prog[self.ip][0] == "jmp":
                self.ip += self.prog[self.ip][1]

