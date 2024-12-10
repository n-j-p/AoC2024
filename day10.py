sample_input = ['89010123',
                '78121874',
                '87430965',
                '96549874',
                '45678903',
                '32019012',
                '01329801',
                '10456732']

class Map():
    def __init__(self, inp):
        self.inp = inp
        self.R = len(inp)
        self.C = len(inp[0]) 
        
    def find_trailheads(self):
        trailheads = []
        for i, r in enumerate(self.inp):
            for j, c in enumerate(r):
                if c == '0':
                    trailheads.append((i,j))
        return trailheads

m0 = Map(sample_input)

#print(m0.find_trailheads())

def traverse(map, start):
    assert map.inp[start[0]][start[1]] == '0'
    seen = set(start)
    def check_valid(pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= map.R or pos[1] >= map.C:
            return False
        return True
    cur = 0
    cur_pt = start
    nxt = [cur_pt,]
    reached = set(())
    while True:
        print(nxt, cur_pt)
        # Check if current level is 9:
        cur_level = int(map.inp[cur_pt[0]][cur_pt[1]])
        if cur_level == 9:
            reached.add(cur_pt)
            nxt.remove(cur_pt)
            if len(nxt) == 0:
                break
            cur_pt = nxt[0]
            continue
        else:
            nxt_level = cur_level + 1

            # Pop current point
            nxt.remove(cur_pt)



        # Work out next points (adjacent points up one level) 
        for pt in [(cur_pt[0]-1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]+1),
                (cur_pt[0]+1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]-1)]:
            if check_valid(pt) and map.inp[pt[0]][pt[1]] == str(nxt_level):
                nxt.append(pt)

        if len(nxt) == 0:
            break
        cur_pt = nxt[0]
        
    return reached

print(traverse(m0, (7,1)))

def part1(inp):
    map_ = Map(inp)
    trails = {}
    for start in map_.find_trailheads():
        trails[start] = traverse(map_, start)
    return trails

print({k: len(v) for k,v in part1(sample_input).items()})

actual_input = open('c:/temp/day10_input.txt').read().split('\n')[:-1]
#print(actual_input)

#ans = {k: len(v) for k,v in part1(actual_input).items()}
#print(sum(ans.values()))

def traverse_with_trail(map, start):
    assert map.inp[start[0]][start[1]] == '0'
    seen = set(start)
    def check_valid(pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= map.R or pos[1] >= map.C:
            return False
        return True
    cur = 0
    nxt = [(start, (start,))]
    cur = nxt[0]
    reached = set(())
    while True:
        #print(nxt, cur[0])
        cur_pt, cur_trail = cur
        # Check if current level is 9:
        cur_level = int(map.inp[cur_pt[0]][cur_pt[1]])
        if cur_level == 9:
            #import pdb
            #pdb.set_trace()
            reached.add(cur[1])
            nxt.remove(cur)
            if len(nxt) == 0:
                break
            cur = nxt[0]
            continue
        else:
            nxt_level = cur_level + 1
            # Pop current point and trail
            nxt.remove(cur)



        # Work out next points (adjacent points up one level) 
        for pt in [(cur_pt[0]-1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]+1),
                (cur_pt[0]+1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]-1)]:
            if check_valid(pt) and map.inp[pt[0]][pt[1]] == str(nxt_level):
                nxt.append((pt, cur_trail + (pt,)))

        if len(nxt) == 0:
            break
        cur = nxt[0]
        
    return reached
print()
map0 = Map(sample_input)
for start in map0.find_trailheads():
    qtrails = traverse_with_trail(map0, start)
    print(start, len(qtrails))

print()
c = 0
map0 = Map(actual_input)
for start in map0.find_trailheads():
    qtrails = traverse_with_trail(map0, start)
    print(start, len(qtrails))
    c += len(qtrails)
print()
print(f'Actual part 2 answer is {c}')
