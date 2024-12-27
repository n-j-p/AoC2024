def group_generator(input, size=3):
    import networkx as nx

    G = nx.Graph()

    for edge in input:
        G.add_edge(*edge.split('-')) 

    for xy in nx.enumerate_all_cliques(G):
        if len(xy) == size:
            yield xy
        if len(xy) > size:
            break

def part1(input):
    for xyz in group_generator(input):
        x,y,z = xyz
        if x[0] == 't' or y[0] == 't' or z[0] == 't':
            yield xyz
def part2(input):
    import networkx as nx

    G = nx.Graph()

    for edge in input:
        G.add_edge(*edge.split('-')) 

    mx = 0
    lg = []
    for t in nx.find_cliques(G):
        if len(t) > mx:
            mx = len(t)
            lg = [t,]
        elif len(t) == mx:
            lg.append(t)
        else:
            continue
    if len(lg) > 1:
        raise Exception('More than one maximal clique')
    import itertools as it
    for xy in it.combinations(lg[0], 2):
        assert G.has_edge(*xy)
    return ','.join(sorted(lg[0]))

    
if __name__ == '__main__':
    import time
    actual_input = open('c:/temp/day23_input.txt').read().split('\n')[:-1]
    tt = time.time()
    c = 0
    for xyz in part1(actual_input):
        c += 1
    print(f'Part 1 answer is {c}. Done in {time.time()-tt:.1f}s')
    tt = time.time()
    print(f'\nPart 2 answer is {part2(actual_input)}. Done in {time.time()-tt:.1f}s')
