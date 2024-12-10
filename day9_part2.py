import pdb
sample = '2333133121414131402'
def symgen():
    n = 0
    while True:
        yield str(n)
        yield '.'
        n += 1

class Map():
    def __init__(self, map):
        self.map = [int(x) for x in map]
        g = symgen()
        self.syms = [next(g) for _ in range(len(self.map))]

        self.syms = [x for i,x in enumerate(self.syms) if self.map[i] > 0 ]
        self.map = [x for x in self.map if x>0]

        self.nlast = self.syms[-2] if self.syms[-1] == '.' else self.syms[-1]
    def gen_repr(self):
        self.lrepr = []
        for i,x in enumerate(self.map):
            self.lrepr += [self.syms[i],] * x
        self.lrepr = ''.join(self.lrepr)
    def find_dots(self, length):
        '''Locates available slot of length length'''
        for i,x in enumerate(self.map):
            if self.syms[i] != '.':
                continue
            if x >= length:
                return i
        raise ValueError(f'No slot of length {length} available')
    def get_ij(self, sym = None):
        '''Locates indices of symbol and available slot'''
        if sym == '.':
            raise IndexError
        if sym is None:
            sym = str(self.nlast)
        j = self.syms.index(sym)
        assert self.syms[j] == sym
        i = self.find_dots(self.map[j])
        return i,j
    def swap(self,i,j, regen_repr=False):
        '''Performs the actual swap and concatenates consecutive dots'''
        if i >= j:
            raise ValueError('Swap must be from right-to-left')

        sym = self.syms[j]
        sym_length = self.map[j]

        # Replace with dots
        self.syms[j] = '.'

        # Now replace dots with symbol:
        assert self.map[i] <= 9
        self.syms[i] = sym # from position j

        # Check if we need to insert dots after
        if self.map[i] > sym_length:
            if self.syms[i+1] == '.':
                # Here we add extra length to the next position
                self.map[i+1] += self.map[i] - sym_length

            else:
                # Here we need to insert new dots
                self.syms.insert(i+1, '.')
                self.map.insert(i+1, self.map[i] - sym_length)
                # Here we need to shift j out one position before
                # dealing with the symbol 
                j += 1
            self.map[i] = sym_length

        # Check for consecutive dots and combine if necessary:
        try:
            following = self.syms[j+1]
            if following == '.':
                self.syms.pop(j+1)
                self.map[j] += self.map.pop(j+1)
        except IndexError: # Occurs at end of list
            pass
        if self.syms[j-1] == '.': # Check of preceding always possible
            self.syms.pop(j)
            self.map[j-1] += self.map.pop(j)
            assert self.syms[j-1] == '.'
            assert len(self.syms) == j or self.syms[j] != '.'
        else:
            assert self.syms[j] == '.'
            assert len(self.syms) == j+1 or self.syms[j+1] != '.' 

        if regen_repr:
            self.gen_repr()
    def defragment_all(self, VERBOSE=False):
        '''Main function'''
        while True:
            try:
                self.swap(*self.get_ij(self.nlast), VERBOSE)
            except ValueError: # no slot available
                pass
            if VERBOSE:
                print(self.lrepr)
            self.nlast = str(int(self.nlast)-1)
            if self.nlast == '-1':
                break
    def calc(self):
        '''Eventual checksum calculation. Could be sped up using triangular numbers!'''
        long_repr = []
        for i,x in enumerate(self.syms):
            if x == '.':
                n = 0
            else: 
                n = int(x)
            long_repr += [n,] * self.map[i]
        c = 0
        for i,x in enumerate(long_repr):
            c += i * x
        return c
                
def T(n): # Triangular number
    if n < 0:
        return 0
    return (n+1)*n//2

TEST = False
if TEST:
    assert T(3) == 6
    assert T(0) == 0
    assert T(5) == 15
    assert T(-1) == 0

            
    # Testing __init__ and gen_repr methods
    sample_map = Map(sample)
    print(sample_map.map)
    print(sample_map.syms)
    sample_map.gen_repr()
    print(sample_map.lrepr)
    print(sample_map.nlast) # 9
    print()

    # Test find_dots method
    assert sample_map.find_dots(3) == 1
    try:
        sample_map.find_dots(4)
        assert False
    except ValueError:
        assert True
    print()

    # Test get_ij method

    assert sample_map.get_ij() == (1, 17)
    try:
        print(sample_map.get_ij('8')) 
        assert False
    except ValueError:
        assert True
    try:
        print(sample_map.get_ij('.')) 
        assert False
    except IndexError:
        assert True
    assert sample_map.get_ij('2') == (1,4)

    # Test swap method
    print('Swapping 2')
    sample_map.swap(1,4,True)
    print(sample_map.lrepr)
    print(list(zip(sample_map.syms, sample_map.map)))

    print('\nReset. Swapping 7')
    sample_map = Map(sample)
    sample_map.swap(*sample_map.get_ij('7'), True)
    print(sample_map.lrepr)
    print(list(zip(sample_map.syms, sample_map.map)))

    print('\nSwapping 9')
    sample_map.swap(*sample_map.get_ij('9'), True)
    print(sample_map.lrepr)
    print(list(zip(sample_map.syms, sample_map.map)))

    # We can't move 8 because there is not a valid space:
    print("Reset. Check if we can move 8 (we can't)")
    sample_map = Map(sample)
    try:
        sample_map.swap(*sample_map.get_ij('8'), True)
        assert False
    except ValueError:
        assert True
    sample_map.gen_repr()
    print(sample_map.lrepr)
    print(sample_map.calc())

    sample_map.defragment_all(VERBOSE=True)
    print(sample_map.calc())


    test_suite = ['22211',
                '22212',
                '222121',
                '2221213',
                '22212131',
                '222121313',
                '2221213136',
                '2020243136',
                '2020243839',
                '202024383917',
                '1313165',
                '233313312141413140211',
                '23331331651141341231402',
                '482374123',
                '293847',
                '129834798237923745897263459827349582734052345',
                '293847520938475092918726346']
    for test in test_suite:
        print()
        print(test)
        mt0 = Map(test)
        mt0.gen_repr()
        print(''.join(mt0.lrepr))
        print(list(zip(mt0.syms, mt0.map)))
        if test == '':#'293847':
            pdb.run('mt0.defragment_all(VERBOSE=True)')
        else:
            mt0.defragment_all(VERBOSE=True)
        print(''.join(mt0.lrepr))
        print(list(zip(mt0.syms, mt0.map)))



import time
tt = time.time()
actual_input = open('c:/temp/day9_input.txt').read().split('\n')[:-1][0]
actual_map = Map(actual_input)
actual_map.gen_repr()
#print(actual_map.lrepr)
#print()
actual_map.defragment_all(VERBOSE=False)
#actual_map.gen_repr()
#print(actual_map.lrepr)

print(f'\nPart 2 answer is {actual_map.calc()}. Done in {time.time()-tt:.1f}s')