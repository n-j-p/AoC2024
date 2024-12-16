def traverse(map, start):
    R = len(map)
    C = len(map[0])
    plant = map[start[0]][start[1]]

    #return plant
    seen = set((start,))
    reached = set((start,))
    def check_valid(pos):
        if pos[0] < 0 or pos[1] < 0:
            return False
        if pos[0] >= R or pos[1] >= C:
            return False
        return True

    nxt = [start]
    cur_pt = start
    while True:
        #print(cur_pt, nxt)
        # Work out next points (adjacent points with sample letter) 
        for pt in [(cur_pt[0]-1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]+1),
                (cur_pt[0]+1, cur_pt[1]),
                (cur_pt[0], cur_pt[1]-1)]:
            if check_valid(pt):
                if pt not in seen:
                    x = map[pt[0]][pt[1]] 
                    #print(pt, x)
                    if x == plant:
                        nxt.append(pt)
                seen.add(pt)

        if len(nxt) == 0:
            break
        cur_pt = nxt.pop(0)
        reached.add(cur_pt)
        seen.add(cur_pt)        
    return plant, reached

def get_partition(inp_):
    #print('partitioning')
    R_ = len(inp_)
    C_ = len(inp_[0])
    import itertools as it
    all_pts = set(it.product(range(R_),range(C_)))
    N = R_ * C_
    partition = {}
    plants = {}
    while len(all_pts) > 0:
        pt = list(all_pts)[0]
        plant, region = traverse(inp_,pt)
        all_pts.difference_update(region)
        #print('--',len(all_pts),'--')
        print(f'{(1-len(all_pts)/N)*100:.1f}%', end='\r')
        partition[pt] = region
        plants[pt] = plant
        #print(pt, plant, region)
    return partition, plants

def calc(pts):
    A = 0
    P = 0
    for pt in pts:
        A += 1
        p = 4
        for adj_pt in [(pt[0]-1, pt[1]),
                        (pt[0], pt[1]+1),
                        (pt[0]+1, pt[1]),
                        (pt[0], pt[1]-1)]:
            if adj_pt in set(pts):
                p -= 1
        P += p
    return (A, P)

def part1(inp_):
    import pdb
    #pdb.set_trace()
    partition, plants = get_partition(inp_)
    print("\n")
    c = 0
    for pt0 in partition.keys():
        print(pt0, end = ': ')
        A, P = calc(partition[pt0])
        print(f'A = {A}, P = {P}, price = {A*P}')
        c += A*P
    return(c)
actual_input = open('c:/temp/day12_input.txt').read().split('\n')[:-1]


 


# Part 2
'''
Rather than counting edges, it is easier to count corners.

For a west-east edge, there are two options, a convex pattern:
 
 --->
 ____
|AAAA|
|AAAA|
|AAAA|
 ----

 and a concave pattern:

   -->
 A|
 A|__
 AAAA

 Thus a W-E edge would be drawn over a region if the following patterns are observed:

 X+
 XA, which is a convex west-east edge, where + is the square of interest, 
      X indicates the square is not part of the region, and

 A+ denotes a concave west-east wall.
  A

 In both cases "+" is not part of the region (actually, it must be an adjacent square.)

 Similarly, a N-S edge is either 

 XX    A
 A+   A+

 for convex and concave edges respectively. The other four alignments are defined similarly.
'''




# First get set of adjacent pts to a region:
def calc_border(pts):
    adjs = set(())
    for pt in pts:
        north = (pt[0], pt[1]-1)
        east = (pt[0]+1, pt[1])
        south = (pt[0], pt[1]+1)
        west = (pt[0]-1, pt[1])
        if north not in pts:
            adjs.add(north)
        if south not in pts:
            adjs.add(south)
        if east not in pts:
            adjs.add(east)
        if west not in pts:
            adjs.add(west)
    return adjs

def draw_partition(coords, letter, R_, C_, repr=None):
    if repr is None:
        repr = [['.' for _ in range(C_)] for _ in range(R_)]

    for x in coords:
        repr[x[0]][x[1]] = letter

    return('\n'.join([''.join(x) for x in repr]))


def calc2(pts, adjs, VERBOSE=True):
    spts = set(pts)
    sadjs = set(adjs)

    # pts defining convex edges
    WE = []
    NS = []
    EW = []
    SN = []

    # pts defining concave edges
    WE2 = []
    NS2 = []
    EW2 = []
    SN2 = []

    A = 0
    E = 0
    for pt in pts:
        A += 1
    
        
        
    # Convex corners, see above
    for pt in adjs:
        north = (pt[0]-1, pt[1])
        east = (pt[0], pt[1]+1)
        south = (pt[0]+1, pt[1])
        west = (pt[0], pt[1]-1)
        northeast = (pt[0]-1, pt[1]+1)
        northwest = (pt[0]-1, pt[1]-1)
        southeast = (pt[0]+1, pt[1]+1)
        southwest = (pt[0]+1, pt[1]-1)

        if south in pts and west not in pts and southwest not in pts:
            E += 1
            WE.append(pt)
        if west in pts and north not in pts and northwest not in pts:
            E += 1
            NS.append(pt)
        if north in pts and east not in pts and northeast not in pts:
            E += 1
            EW.append(pt)
        if east in pts and south not in pts and southeast not in pts:
            E += 1
            SN.append(pt)

    # Concave corners, see above
    for pt in adjs:
        north = (pt[0]-1, pt[1])
        east = (pt[0], pt[1]+1)
        south = (pt[0]+1, pt[1])
        west = (pt[0], pt[1]-1)
        if west in spts and south in spts:
            WE2.append(pt)
            E += 1
        if north in spts and west in spts:
            E += 1
            NS2.append(pt)
        if east in spts and north in spts:
            E += 1
            EW2.append(pt)
        if south in spts and east in spts:
            E += 1
            SN2.append(pt)
    if VERBOSE:
        print(f'A={A}, E={E}')
    return (A,E, WE, NS, EW, SN, WE2, NS2, EW2, SN2)



def calc_edges(pts_):
    adj_pts_ = calc_border(pts_)
    return calc2(pts_, adj_pts_, False)[:2]


def part2(inp_):
    partition, plants = get_partition(inp_)
    print("\n")
    c = 0
    for pt0 in partition.keys():
        print(pt0, end = ': ')
        A, E = calc_edges(partition[pt0])
        print(f'A = {A}, P = {E}, price = {A*E}')
        c += A*E
    return(c)

if __name__ == '__main__':
    import time

    tt = time.time()
    
    part1_answer = part1(actual_input)

    t1 = time.time() - tt

    tt = time.time()
    part2_answer = part2(actual_input)

    t2 = time.time() - tt
    print(f'Part 1 answer is {part1_answer}. Done in {t1:.1f}s.')

    print(f'Part 2 answer is {part2_answer}. Done in {t2:.1f}s.')
