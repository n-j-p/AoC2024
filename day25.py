class Schem():
    def __init__(self,input):
        self.input = input
    def is_key(self):
        if self.input[0][0] == '#' and self.input[-1][-1] == '.':
            return True
        return False
    def __repr__(self):
        return '\n'.join(self.input)
    def encode(self):
        # Transpose schematic
        # https://stackoverflow.com/a/6473724
        tr = map(list,zip(*self.input))
        # get pin heights
        if self.is_key():
            return [x.index('.')-1 for x in tr]
        else:
            return [x[::-1].index('.')-1 for x in tr]
    def fits(self, other):
        if self.is_key() ^ other.is_key():
            self_pins = self.encode()
            other_pins = other.encode()
            #print(list(zip(self_pins, other_pins)))
            for i,x in enumerate(self_pins):
                #print(x + other_pins[i])
                if x + other_pins[i] > 5:
                    return False
            return True

        else:
            raise ValueError('fits() requires one lock and one key')

    
def read_input(input):
    schematics = []
    schematic_i = []
    for i,x in enumerate(input):
        #print('zxcv', x)
        if x != '':
            schematic_i.append(x)
            #print(schematic_i)
        else:
            schematics.append(Schem(schematic_i))
            schematic_i = []
    return schematics

if __name__ == '__main__':
    import itertools as it
    from tqdm import tqdm
    actual_input = open('c:/temp/day25_input.txt').read().split('\n')
    schematics = read_input(actual_input)
    c = 0
    for xy in tqdm(it.combinations(schematics, 2),  
                   total=len(schematics)*(len(schematics)-1)//2):
        x,y = xy
        try:
            OK = x.fits(y)
            if OK:
                c += 1
        except ValueError:
            continue
    print('Part 1 answer is',c)