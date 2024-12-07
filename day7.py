class Expr():
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
    def set_operators(self, operators):
        assert len(self.nums) == len(operators) + 1
        self.operators = operators
    def eval(self):
        cp = self.nums[0]
        for i,x in enumerate(self.operators):
            if x == 0: # addition
                cp += self.nums[i+1]
            elif x == 1: # multiplication
                cp *= self.nums[i+1]
            else:
                raise Exception('Unknown operator, 0=+, 1=*')
        return cp
    def check_all(self):
        import itertools as it
        for ops in it.product([0,1], repeat=self.n-1):
            self.set_operators(ops)
            yield(self.eval(), ops)

e0 = Expr([10,19])
e0.set_operators([0,])
#print(e0.eval())

e0.set_operators([1,])
#print(e0.eval())

e2 = Expr([11,6,16,20])
#print(list(e2.check_all()))

sample_input = ['190: 10 19',
        '3267: 81 40 27',
        '83: 17 5',
        '156: 15 6',
        '7290: 6 8 6 15',
        '161011: 16 10 13',
        '192: 17 8 14',
        '21037: 9 7 18 13',
        '292: 11 6 16 20']

inp0 = sample_input

def part1(inp, VERBOSE=True):
    c = 0
    for row in inp:
        target_str, nums_str = row.split(': ') 
        target = int(target_str)
        nums = [int(x) for x in nums_str.split(' ')]
        if VERBOSE:
            print(target, nums, end=', ')
        expression = Expr(nums)
        sat = False
        for poss in expression.check_all():
            if poss[0] == target:
                if VERBOSE:
                    print(poss[1])
                sat = True
                c += target
                break
        if not sat and VERBOSE:
            print('not statisfied')
    return c

assert part1(inp0, True) == 3749

fpath = 'c:/temp/day7_input.txt'
actual_input = open(fpath).read().split('\n')[:-1]
#print(actual_input)

print()
print('Part 1 answer is',part1(actual_input, False))
print()

class Expr2(Expr):
    def eval(self):
        cp = self.nums[0]
        for i,x in enumerate(self.operators):
            if x == 0: # addition
                cp += self.nums[i+1]
            elif x == 1: # multiplication
                cp *= self.nums[i+1]
            elif x == 2: # concatentation
                cp = int(str(cp) + str(self.nums[i+1]))
            else:
                raise Exception('Unknown operator, 0=+, 1=*')
        return cp
    def check_all(self):
        import itertools as it
        for ops in it.product([0,1,2], repeat=self.n-1):
            self.set_operators(ops)
            yield(self.eval(), ops)

ex = Expr2([6,8,6,15])
ex.set_operators([1,2,1])
print(ex.eval())


def part2(inp, VERBOSE=True):
    c = 0
    for row in inp:
        target_str, nums_str = row.split(': ') 
        target = int(target_str)
        nums = [int(x) for x in nums_str.split(' ')]
        if VERBOSE:
            print(target, nums, end=', ')
        expression = Expr2(nums)
        sat = False
        for poss in expression.check_all():
            if poss[0] == target:
                if VERBOSE:
                    print(poss[1])
                sat = True
                c += target
                break
        if not sat and VERBOSE:
            print('not statisfied')
    return c

assert part2(inp0, True) == 11387

print()
print('Part 2 answer is',part2(actual_input, False))
print()