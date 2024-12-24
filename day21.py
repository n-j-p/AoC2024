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
        #print('*****')
        #print(cps)
        #print('*****')
        for i,x in enumerate(cps[1:]):
            seqi = list(self._fill_in(cps[i], x))
            #print(f'{cps[i]} -> {x}', seqi)
            all_seqs.append(seqi)
        #print(all_seqs)
        for seq in it.product(*all_seqs):
            yield seq
    def _conv_to_str(self, seq):
        last = seq[0][0]
        dirstr = ''
        for step in seq:
            for mv in step:
                #print(mv)
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
    import time
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


if False:#if __name__ == '__main__':

    actual_seqs = ['208A',
                '586A',
                '341A',
                '463A',
                '593A']
    print(part1_semiBF(actual_seqs))

def minpath(input, depth, keypad = DirectionalKeypad):
    if depth == 1:
        if len(set(input).difference('^<v>A')) > 0:
            raise Exception('Unknown characters')
        else:
            return len(input), input
    if depth < 1:
        raise Exception("Shouldn't happen")
    else:
            
        kp = keypad()
        #pdb.set_trace()
        from numpy import inf
        mn = inf
        mni = -1
        for i,seqi in enumerate(kp.gen_all_seqs(input)):
            import pdb
            pdb.set_trace()
            length, next_level_input_seq = minpath(seqi, depth - 1, DirectionalKeypad) 
            if length < mn:
                mn_i = i
                mn = length
                mn_seq = next_level_input_seq

        return mn, next_level_input_seq
    
if False:#__name__ == '__main__':
    # Comparing recursive approach to semi-BF (sequential)
    import time
    sample_input = ['029A',
                    '980A',
                    '179A',
                    '456A',
                    '379A']
    for code in sample_input:
        tt = time.time()
        print(code, minpath(code, 4, NumericKeypad)[0], f'{time.time()-tt:.1f}s')
    print()
    print(part1_semiBF(sample_input))
    # So the recursive approach is an order of magnitude slower, but
    # we can extend this for arbitrary levels and memoise.

if __name__ == '__main__':
    dkp = DirectionalKeypad()
    print(dkp.gen_positions('<>^vA'))
    keypad_transitions = ['A',]
    for x in it.permutations(dkp.gen_positions('<>^vA')[1:], 2):
        #print(x)
        fx = list(dkp._fill_in(*x))
        rpos2 = {(-1,0): '^',
                 (1,0): 'v',
                 (0,-1): '<',
                 (0,1): '>',
                 (0,0): ''}
        def dxy(p1,p2):
            return (p1[0]-p2[0],p1[1]-p2[1])
        rpos = {v:k for k,v in dkp.positions.items()}
        for i,fxi in enumerate(fx):
            # for j, fxj in enumerate(fxi[1:]):
            #     print('xxx',j,fxj,fxi[j],dxy(fxj,fxi[j]),rpos2[dxy(fxj,fxi[j])])
            fstr = [rpos2[dxy(fxj, fxi[j])] for j,fxj in enumerate(fxi[1:])]
            #print(x,fx,i,fxi,fstr)
            print(x,[rpos[p] for p in x], ''.join(fstr))
                #print(x, fx, fxi, fxj, fstr)
    #              minpath(tuple(dkp._fill_in(*x)),1))
            keypad_transitions.append(''.join(fstr) + 'A')
    print(keypad_transitions)
    DP = {}
    for xy in keypad_transitions:
        res = minpath(xy, depth=1)
        DP[(xy, 1)] = res
        #print(xy, minpath(xy, depth=4))
    print(DP)
    print('xxxxxxxxxxxxx',xy)
    print(minpath(xy, depth = 2))