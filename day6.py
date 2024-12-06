#day6.py

sample_input = ['....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...']
print(len(sample_input))
for x in sample_input:
    print(x)
    print()
def locate_start(inp):
    for i,r in enumerate(inp):
        if r.count('^') == 0:
            continue
        else:
            #print(r)
            return (i,r.index('^'))
print(locate_start(sample_input))

def traverse(inp):
    inp1 = [''.join(list(x)) for x in inp]
    R = len(inp1)
    C = len(inp1[0])
    cur = locate_start(inp) + (0,) # direction, 0 = N, 1 = E, etc.
    while cur[0] >= 0 and cur[0] < C and cur[1] >= 0 and cur[1] < R:
        i = cur[0]
        j = cur[1]
        #print(inp1[i])
        inp1[i] = inp1[i][:j] + 'X' + inp1[i][(j+1):]
        if cur[2] == 0:
            nxt = (cur[0]-1, cur[1], cur[2])
        elif cur[2] == 1:
            nxt = (cur[0], cur[1]+1, cur[2])
        elif cur[2] == 2:
            nxt = (cur[0]+1, cur[1], cur[2])
        else:
            nxt = (cur[0], cur[1]-1, cur[2])
        try:
            test = inp1[nxt[0]][nxt[1]]
        except IndexError:
            return inp1
        if test == '#':
            cur = (cur[0], cur[1], (cur[2] + 1) % 4)
        else:
            cur = nxt
    return inp1
        

traversed = traverse(sample_input)
print()
for x in traversed:
    print(x)
print('Part 1 test result is', sum([r.count('X') for r in traversed]))
assert sum([r.count('X') for r in traversed]) == 41

fpath = 'c:/temp/day6_input.txt'
actual_inp = open(fpath).read().split('\n')[:-1]
#print(actual_inp)

traversed = traverse(actual_inp)
#print()
#for x in traversed:
#    print(x)
print('Part 1 answer is', sum([r.count('X') for r in traversed]))

def traverse2(inp): # same but keep a list of previous states
    seen = set(())
    inp1 = [''.join(list(x)) for x in inp]
    R = len(inp1)
    C = len(inp1[0])
    cur = locate_start(inp) + (0,) # direction, 0 = N, 1 = E, etc.
    while True:
        if cur in seen:
            #print()
            #for x in inp1:
            #    print(x)
            #print()
            return None
        seen.add(cur)
        i = cur[0]  
        j = cur[1]
        #print(inp1[i])
        inp1[i] = inp1[i][:j] + 'X' + inp1[i][(j+1):]
        if cur[2] == 0:
            nxt = (cur[0]-1, cur[1], cur[2])
        elif cur[2] == 1:
            nxt = (cur[0], cur[1]+1, cur[2])
        elif cur[2] == 2:
            nxt = (cur[0]+1, cur[1], cur[2])
        else:
            nxt = (cur[0], cur[1]-1, cur[2])
        if nxt[0] < 0 or nxt[0] >= R or nxt[1] < 0 or nxt[1] >= C:
            return inp1
        try:
            test = inp1[nxt[0]][nxt[1]]
        except IndexError:
            return inp1
        if test == '#':
            cur = (cur[0], cur[1], (cur[2] + 1) % 4)
        else:
            cur = nxt
        #print()
        #for y in inp1:
        #    print(y)
        #print()
    return inp1
#print(sample_input)  

def part2(inp, start_pos=[]):
    c = 0
    zz = 0
    start = locate_start(inp)
    for ij in start_pos:
#    for i in range(len(inp)):
#        for j in range(len(inp[0])):
        i,j = ij
        inp2 = [''.join(list(x)) for x in inp]
        if inp2[i][j] == '.':
            inp2[i] = inp2[i][:j] + '#' + inp2[i][(j+1):]
            if traverse2(inp2) is None:
                c += 1
                #print(i,j)
    #print(zz)
    return c
pos = []
for j,row in enumerate(traverse(sample_input)):
    k = [i for i,x in enumerate(row) if x=='X']
    print(row, k)
    for l in k:
        pos.append((j,l))
#print(pos)
p2t = part2(sample_input, pos)
print('Part 2 test value is', p2t)
assert p2t == 6

actual_traversed = traverse(actual_inp)
pos = []
start = locate_start(actual_inp)
print(start)
for j,row in enumerate(actual_traversed):
    k = [i for i,x in enumerate(row) if x=='X']# and (not (j < start[0] and i == start[1]))]
    #print(row, k)
    for l in k:
        pos.append((j,l))
        
#print(pos)
pt2a = part2(actual_inp, pos)
print('Part 2 answer is',pt2a)
