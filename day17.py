class Computer():
    def __init__(self, A, B, C):
        self.inspo = 0 # instruction pointer
        self.A = A
        self.B = B
        self.C = C
        self.output = []
    def __repr__(self):
        return ','.join([str(x) for x in self.output])
    def program(self, instructions):
        self.instructions = instructions
    def _mapping(self, opcode):
        return {0: self.adv,
                1: self.bxl,
                2: self.bst,
                3: self.jnz,
                4: self.bxc,
                5: self.out,
                6: self.bdv,
                7: self.cdv}[opcode]
    def run_one_step(self):
        print(self._mapping(self.instructions[self.inspo]))
        self._mapping(self.instructions[self.inspo])(self.instructions[self.inspo+1])
        self.inspo += 2
    def run(self):
        while True:
            try:
                self.run_one_step()
            except IndexError:
                return
    def _return_operand(self, combo_operand):
        if combo_operand == 7:
            raise ValueError('7 not a valid combo operand')
        elif combo_operand <= 3 and combo_operand >= 0:
            val = combo_operand
        elif combo_operand == 4:
            val = self.A
        elif combo_operand == 5:
            val = self.B
        elif combo_operand == 6:
            val = self.C
        else:
           ValueError('Unknown combo operand')
        return val
    def adv(self, combo_operand):
        val = self._return_operand(combo_operand)
        print(self.A, 2**val)
        self.A //= 2**val
    def bxl(self, literal_operand):
        if literal_operand < 0 or literal_operand > 7:
            raise ValueError('Invalid literal operand passed to bxl')
        self.B ^= literal_operand
    def bst(self, combo_operand):
        val = self._return_operand(combo_operand)
        self.B = val % 8
    def jnz(self, literal_operand):
        if self.A == 0:
            return
        self.inspo = literal_operand -2 # This will be removed in run_one_step method
    def bxc(self, dummy_operand):
        self.B ^= self.C
    def out(self, combo_operand):
        val = self._return_operand(combo_operand)
        self.output.append(val % 8)
    def bdv(self, combo_operand):
        val = self._return_operand(combo_operand)
        self.B = self.A//2**val
    def cdv(self, combo_operand):
        val = self._return_operand(combo_operand)
        self.C = self.A//2**val




def parse_input(inp):
    Astr = inp[0].replace('Register A:','')
    A = int(Astr)
    Bstr = inp[1].replace('Register B:','')
    B = int(Bstr)
    Cstr = inp[2].replace('Register C:','')
    C = int(Bstr)
    
    programstr = inp[4].replace('Program: ','')
    program = [int(x) for x in programstr.split(',')]
    cc = Computer(A, B, C)
    cc.program(program)
    return cc

if __name__ == '__main__':
    actual_input = open('c:/temp/day17_input.txt').read().split('\n')[:-1]
    actual_comp = parse_input(actual_input)
    actual_comp.run()

    print(f'Part 1 output is {actual_comp}')

    inp2 = ['Register A: 2024',
            'Register B: 0',
            'Register C: 0',
            '',
            'Program: 0,3,5,4,3,0']

    comp2 = parse_input(inp2)
    comp2.A = 117440
    comp2.run()
    print(comp2)