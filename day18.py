sample_input = open('c:/temp/day18_sample_input.txt').read().split('\n')[:-1]

class MemorySpace():
    def __init__(self, N):
        self.N = N
    def drop_bytes(self, inp):
        self.corrupted = [tuple([int(y) for y in x.split(',')]) for x in inp]
    def __repr__(self):
        lrepr = [['.' for _ in range(self.N+1)] for _ in range(self.N+1)]
        for x in self.corrupted:
            lrepr[x[1]][x[0]] = '#'
        return '\n'.join([''.join(x) for x in lrepr])
    def _isvalid(self, position):
        if position[0] >= 0 and position[1] >= 0 and position[0]<=self.N and position[1] <= self.N:
            return True
        return False
    def traverse(self):
        seen = {(0,0): 0}
        start = (0,0)
        nxt = [start,]
        while len(nxt) > 0:
            cur = nxt.pop(0)
            for delta in [(-1,0),(0,-1),(1,0),(0,1)]:
                newpt = (cur[0] + delta[0], cur[1] + delta[1])
                if self._isvalid(newpt) and newpt not in self.corrupted: 
                    if newpt not in seen or seen[newpt] > seen[cur] + 1:
                        seen[newpt] = seen[cur] + 1
                        nxt.append(newpt)
        return seen[(self.N, self.N)]



space = MemorySpace(6)
space.drop_bytes(sample_input[:12])
print(space.corrupted)
print(space)
print(space.traverse())

actual_input = open('c:/temp/day18_input.txt').read().split('\n')[:-1]
actual_space = MemorySpace(70)
actual_space.drop_bytes(actual_input[:1024])
print(actual_space.traverse())

for k in range(12,len(sample_input)):
    print(k)
    space = MemorySpace(6)
    space.drop_bytes(sample_input[:k])
    #print(space.corrupted)
    #print(space)
    try:
        print(k,space.traverse(), sample_input[k])
    except KeyError:
        print('answer is ', sample_input[k-1])
        break


for k in range(1024,len(actual_input)):
    print(k)
    space = MemorySpace(70)
    space.drop_bytes(actual_input[:k])
    #print(space.corrupted)
    #print(space)
    try:
        print(k,space.traverse(), actual_input[k])
    except KeyError:
        print('answer is ', actual_input[k-1])
        break
