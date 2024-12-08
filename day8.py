sample_input = ['............',
                '........0...',
                '.....0......',
                '.......0....',
                '....0.......',
                '......A.....',
                '............',
                '............',
                '........A...',
                '.........A..',
                '............',
                '............']

class Map():
    def __init__(self, inp):
        self.inp = inp
        self.R = len(inp)
        self.C = len(inp[0])
    def map_antennas(self):
        locations = {}
        for i,row in enumerate(self.inp):
            assert len(row) == self.C
            for j,symbol in enumerate(row):
                if symbol != '.':
                    try:
                        locations[symbol].append((i,j))
                    except KeyError:
                        locations[symbol] = [(i,j)]
        return locations
    def _locate_antinodes(self, P, Q):
        diff = (P[0] - Q[0], P[1] - Q[1])
        #print(P)
        #print(Q)
        #print(diff)
        return(((P[0]+diff[0], P[1]+diff[1]),
                (Q[0]-diff[0], Q[1]-diff[1])))
    def locate_all_antinodes(self):
        import itertools as it
        antennas = self.map_antennas()
        antinodes = {}
        for symbol in antennas.keys():
            antinodes[symbol] = []
            for PQ in it.combinations(antennas[symbol], r=2):
                ANs = self._locate_antinodes(*PQ)
                antinodes[symbol].append(ANs[0])
                antinodes[symbol].append(ANs[1])
        self.antinode_locations = antinodes
    def get_filtered_antinode_locations(self):
        #for k in self.antinode_locations.keys():
        #    print(k, self.antinode_locations[k])
        return {k: [loc for loc in self.antinode_locations[k] if \
                    loc[0] >= 0 and loc[1] >= 0 and loc[0] < self.R and loc[1] < self.C] for \
                    k in self.antinode_locations.keys()}


sample_map = Map(sample_input)
sample_antennas = sample_map.map_antennas()
#print(sample_antennas)
#print(sample_map._locate_antinodes(sample_antennas['0'][0],sample_antennas['0'][1]))
sample_map.locate_all_antinodes()
#print(sample_map.antinode_locations)
#print(sample_map.get_filtered_antinode_locations())

qlocs = set(())
for locs in sample_map.get_filtered_antinode_locations().values():
    qlocs.update(tuple(locs))
#print(qlocs)

## Part 1 test

def part1(inp_):
    map0 = Map(inp_)
    sample_antennas = map0.map_antennas()
    map0.locate_all_antinodes()
    
    qlocs = set(())
    for locs in map0.get_filtered_antinode_locations().values():
        qlocs.update(tuple(locs))
    #return qlocs
    return len(qlocs)

p1test = part1(sample_input)
assert p1test == 14
print('Part 1 test answer is', p1test)

## Part 1 actual

fpath = 'c:/temp/day8_input.txt'
actual_inp = open(fpath).read().split('\n')[:-1]
#print(actual_inp)

p1 = part1(actual_inp)
print('Part 1 answer is', p1)


## Part 2

# Rewrite Map()._locate_antinodes as a generator

class Map2(Map):
    def _generate_antinodes(self, P, Q):
        diff = (P[0] - Q[0], P[1] - Q[1])
        yield(P)
        yield(Q)
        newpt = (P[0]+diff[0], P[1]+diff[1]) 
        while newpt[0] >= 0 and newpt[1] >= 0 and newpt[0] < self.C and newpt[1] < self.R:
            yield newpt
            newpt = (newpt[0] + diff[0], newpt[1] + diff[1])
        newpt = (Q[0]-diff[0], Q[1]-diff[1]) 
        while newpt[0] >= 0 and newpt[1] >= 0 and newpt[0] < self.C and newpt[1] < self.R:
            yield newpt
            newpt = (newpt[0] - diff[0], newpt[1] - diff[1])
    def locate_all_antinodes_new(self):
        import itertools as it
        antennas = self.map_antennas()
        antinodes = {}
        for symbol in antennas.keys():
            antinodes[symbol] = []
            for PQ in it.combinations(antennas[symbol], r=2):
                for AN in self._generate_antinodes(*PQ):
                    antinodes[symbol].append(AN)
        self.antinode_locations = antinodes
    locate_all_antinodes = None
m1 = Map2(['T.........',
           '...T......',
           '.T........',
           '..........',
           '..........',
           '..........',
           '..........',
           '..........',
           '..........',
           '..........'])
m1.map_antennas()
m1.locate_all_antinodes_new()
#print(m1.antinode_locations)

def part2(inp_):
    map00 = Map2(inp_)
    sample_antennas = map00.map_antennas()
    map00.locate_all_antinodes_new()
    
    qlocs = set(())

    for locs in map00.antinode_locations.values():
        qlocs.update(tuple(locs))
    #return qlocs
    return len(qlocs)

p2t = part2(sample_input)
assert p2t == 34
print('Part 1 test answer is', p2t)

## Part 2 actual


p2 = part2(actual_inp)
print('Part 2 answer is', p2)
