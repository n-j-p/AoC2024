import pdb
import itertools as it
from tqdm import tqdm
class Keypad():
    def __init__(self):
        raise NotImplementedError('Keypad is a inheritable class only')
        
    def gen_positions(self, code):
        code_positions = [self.positions[x] for x in 'A' + code]
        return code_positions
    def _fill_in(self, pos1, pos2):
        if pos1 == pos2:
            yield [pos1, pos2]
            return
        deltay = pos1[0] - pos2[0]
        deltax = pos1[1] - pos2[1]
        N = abs(deltax)+abs(deltay)
        for ipos in it.combinations(range(N), abs(deltax)):
            #print(ipos)
            i = [0,] * N
            for j in ipos:
                i[j] = 1
            #print(i)
            dx = (0,-1) if deltax > 0 else (0,1)
            dy = (-1,0) if deltay > 0 else (1,0)
            delta = [dx if x == 1 else dy for x in i]
            #print(delta)
            steps = [pos1,]
            for d in delta:
                steps.append((steps[-1][0] + d[0], 
                              steps[-1][1] + d[1]))
            #print(steps)
            if len(self.avoid.intersection(steps)) > 0:
                #print('Crosses gap')
                pass
            else:
                yield steps
    def gen_seq(self, code):
        all_seqs = []
        cps = self.gen_positions(code)
        for i,x in enumerate(cps[1:]):
            seqi = list(self._fill_in(cps[i], x))
            all_seqs.append(seqi)
        for seq in it.product(*all_seqs):
            yield seq
    def _conv_to_str(self, seq):
        last = seq[0][0]
        dirstr = ''
        for step in seq:
            for mv in step:
                dy = mv[0]-last[0]
                dx = mv[1]-last[1]
                if dx == 1:
                    sym = '>'
                elif dx == -1:
                    sym = '<'
                elif dy == 1:
                    sym = 'v'
                elif dy == -1:
                    sym = '^'
                elif dx == 0 and dy == 0:
                    sym = ''
                else:
                    raise ValueError
                dirstr += sym
                last = mv

            dirstr += 'A'
        return dirstr
    def gen_all_seqs(self, code):
        g = self.gen_seq(code)
        return [self._conv_to_str(ng) for ng in g]

class NumericKeypad(Keypad):
    def __init__(self):
        self.positions = {'7': (0,0),
                          '8': (0,1),
                          '9': (0,2),
                          '4': (1,0),
                          '5': (1,1),
                          '6': (1,2),
                          '1': (2,0),
                          '2': (2,1),
                          '3': (2,2),
                          '0': (3,1),
                          'A': (3,2)
                          }
        self.avoid = set(((3,0),))

class DirectionalKeypad(Keypad):
    def __init__(self):
        self.positions = {'^': (0,1),
                          'A': (0,2),
                          '<': (1,0),
                          'v': (1,1),
                          '>': (1,2)}
        self.avoid = set(((0,0),))
        
    

def part1_semiBF(input):
    import time, pdb
    c = 0
    for seq in input:
        tt = time.time()
        nkp = NumericKeypad()
        seqs0 = nkp.gen_all_seqs(seq)
        t = seqs0

        dkp1 = DirectionalKeypad()
        mn_t = min([len(y) for y in t])
        seqs1 = [dkp1.gen_all_seqs(u) for u in filter(lambda x: len(x) == mn_t, t)]
        u = list(it.chain.from_iterable(seqs1))

        dkp2 = DirectionalKeypad()
        mn_u = min([len(y) for y in u])
        seqs2 = [dkp2.gen_all_seqs(v) for v in filter(lambda x: len(x) == mn_u, u)]
        w = list(it.chain.from_iterable(seqs2))
        ans = min([len(x) for x in w])
        print(seq, ans, f'{time.time()-tt:.1f}s')
        print(int(seq[:-1]) * ans)
        c += int(seq[:-1]) * ans

    return c


def minpath(input, depth, DP = {}, keypad = DirectionalKeypad):
    import pdb
    if (input, depth) in DP and depth > 1:
        import pdb
        return DP[(input, depth)][0], '', DP#DP[(input, depth)][1], DP
        pass
    if depth == 1:
        if len(set(input).difference('^<v>A')) > 0:
            raise Exception('Unknown characters')
        else:
            return len(input), '', DP
    if depth < 1:
        raise Exception("Shouldn't happen")
    else:
            
        kp = keypad()
        from numpy import inf
        mn = inf
        mni = -1


        for i,seqi in enumerate(kp.gen_all_seqs(input)):
            broken_seqi = seqi.replace('A','A~').split('~')[:-1]
            reconstructed_seq = ''
            reconstructed_length = 0
            for bseqi in broken_seqi:
                length, next_level_input_seq, DP = minpath(bseqi, depth - 1, DP, DirectionalKeypad) 
                reconstructed_length += length
                reconstructed_seq += next_level_input_seq
            if reconstructed_length < mn:
                mn_i = i
                mn = reconstructed_length
                mn_seq = reconstructed_seq

        DP[(input, depth)] = (mn, '')
        return mn, '', DP
    

def part2_recursive(input, depth = 3, VERBOSE = True):
    import time, tqdm

    DP = {}

    c = 0
    print()
    for seq in tqdm.tqdm(input):
        tt = time.time()
        nkp = NumericKeypad()
        if VERBOSE:
            print()
            print(seq)
            print("-----------")
        seqs0 = nkp.gen_all_seqs(seq)
        from numpy import inf
        mn = inf
        for seq0 in seqs0:
            mn_i, _, DP = minpath(seq0, depth, DP)
            if VERBOSE: print(seq0, mn_i)
            mn = min(mn, mn_i)
        if VERBOSE: print(mn, int(seq[:-1]), mn*int(seq[:-1]))
        c += mn * int(seq[:-1])
    return c

if __name__ == '__main__':
    import time


    tt = time.time()
    actual_input = ['208A',
                    '586A',
                    '341A',
                    '463A',
                    '593A']
    #ans = part1_semiBF(actual_input)
    #print(f'Part 1 answer = {ans}. Done in {time.time()-tt:.1f}s')
    print("Using part 2 method:")
    print(part2_recursive(actual_input, VERBOSE=False))

    tt = time.time()
    print()
    ans = part2_recursive(actual_input, depth = 26, VERBOSE=False)
    print(f'Part 2 answer = {ans}. Done in {time.time()-tt:.1f}s')
