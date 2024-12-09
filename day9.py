
def gen_r():
    n = 0
    while True:
        yield str(n)
        n += 1
        yield '.'
def long_dcode(y):
    gsymbol = gen_r()
    list_repr = []
    for x in y:
        sym = next(gsymbol)
        
        list_repr += [sym,] * int(x)

    return list_repr
print(long_dcode('512341512'))



            
sample = '2333133121414131402'

print(''.join(long_dcode(sample)))



class Map2():
    def __init__(self, map):
        self.map = [int(z) for z in map]
    def gen_repr(self):
        self.lrepr = long_dcode(self.map)
    def next_dot(self):
        return self.lrepr.index('.')
    def last_nonempty(self):
        for i,x in enumerate(self.lrepr[::-1]):
            if x != '.':
                return len(self.lrepr) - 1 - i
        raise Exception('No non-empty slots')
    def reorder_one(self):
        i = self.next_dot()
        j = self.last_nonempty()
        if j <= i:
            raise ValueError('Sorted')
        x = self.lrepr.pop(j)
        y = self.lrepr.pop(i)
        assert y == '.'
        self.lrepr.insert(i,x)
        self.lrepr.insert(j,y)
        #self.repr = ''.join(list_repr)
    def reorder_all(self, VERBOSE=False):
        while True:
            if VERBOSE:
                print(''.join(self.lrepr))
            try:
                self.reorder_one()
            except ValueError:
                break
            if VERBOSE:
                print(''.join(self.lrepr))
    def calc(self):
        c = 0
        for i,x in enumerate(self.lrepr):
            if x == '.':
                v = 0
            else:
                v = int(x)
            c += v*i
        return c

m0 = Map2(sample)
m0.gen_repr()
m0.reorder_all(VERBOSE=True)

p1_test = m0.calc()
print()
print('Part 1 test value is',p1_test)
assert p1_test == 1928

actual_input = open('c:/temp/day9_input.txt').read().split('\n')[:-1][0]
print(len(actual_input))

import time
tt = time.time()
print()
m1 = Map2(actual_input)
m1.gen_repr()
print('Part 1 answer is', end=' ')
m1.reorder_all()
print(f'{m1.calc()}. Done in {time.time()-tt:.1f}s')