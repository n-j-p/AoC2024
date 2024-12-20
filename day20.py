import numpy as np
import time

class Race():
    def __init__(self, input):
        self.input = input
        walls = set(())
        start = None
        end = None

        for i, row in enumerate(input):
            self.C = len(row)
            for j, x in enumerate(row):
                if x == '#':
                    walls.add((i,j))
                elif x == 'S':
                    start = (i,j)
                elif x == 'E':
                    end = (i,j)
        self.R = i+1
        self.walls = walls
        self.start = start
        self.end = end
        self.seen = set(())
    
    def __repr__(self):
        lrepr = [['.' for _ in range(self.C)] for _ in range(self.R)]
        for wloc in self.walls:
            lrepr[wloc[0]][wloc[1]] = '.'
        for cloc in self.seen:
            lrepr[cloc[0]][cloc[1]] = str(self.seen[cloc]%10)
        return '\n'.join([''.join(row) for row in lrepr])
    
    def _is_interior(self, pt):
        if pt[0] != 0 and pt[1] != 0 and pt[0] != self.C-1 and pt[1] != self.R-1:
            return True
        return False
    def traverse(self, start_from):
        seen = {start_from: 0}
        nxt = [start_from,]
        while len(nxt) > 0:
            cur = nxt.pop(0)
            for delta in [(-1,0),(0,-1),(1,0),(0,1)]:
                newpt = (cur[0] + delta[0], cur[1] + delta[1])
                if newpt not in self.walls: 
                    if newpt not in seen or seen[newpt] > seen[cur] + 1:
                        seen[newpt] = seen[cur] + 1
                        nxt.append(newpt)
        self.seen = seen
        return seen
    def traverse_both(self):
        self.from_start = self.traverse(self.start)
        self.from_end = self.traverse(self.end)
    def remove_single_pt(self, pos):
        min_from_start = np.inf
        min_from_end = np.inf
        for delta in [(-1,0),(0,-1),(1,0),(0,1)]:
            newpt = (pos[0] + delta[0], pos[1] + delta[1])
            if newpt in self.walls:
                continue
            try:
                min_from_start = min(min_from_start,
                                     self.from_start[newpt])
            except KeyError:
                pass
            try:
                min_from_end = min(min_from_end,
                                   self.from_end[newpt])
            except KeyError:
                pass
        return min_from_start + min_from_end + 2
    def remove_two_pts(self, pts):
        assert len(pts) == 2
        min_from_start = np.inf
        min_from_end = np.inf
        for pos in pts:
            for delta in [(-1,0),(0,-1),(1,0),(0,1)]:
                newpt = (pos[0] + delta[0], pos[1] + delta[1])
                if newpt in self.walls:
                    continue
                try:
                    min_from_start = min(min_from_start,
                                        self.from_start[newpt])
                except KeyError:
                    pass
                try:
                    min_from_end = min(min_from_end,
                                    self.from_end[newpt])
                except KeyError:
                    pass
        return min_from_start + min_from_end + 3
    def gen_all_single_pts(self):
        for pt in self.walls:
            if self._is_interior(pt):
                yield pt
    def gen_all_double_pts(self):
        for pt in self.gen_all_single_pts():
            for delta in [(1,0),(0,1)]: # only go south and east to avoid double counting
                pt2 = (pt[0] + delta[0], pt[1] + delta[1])
                if self._is_interior(pt2) and pt2 in self.walls:
                    yield (pt, pt2)


def part1(input, VERBOSE=True):                                     
    race = Race(input)
    race.traverse_both()
    noncheat_time = race.from_start[race.end]
    if VERBOSE:
        print('No-cheat time is', noncheat_time)

    res = {}
    for pt in race.gen_all_single_pts():
        completion_time = race.remove_single_pt(pt)
        #print(pt, completion_time)
        res[pt] = completion_time

    from collections import Counter
    cheat_savings = Counter()
    for k,v in res.items():
        if v > noncheat_time:
            continue
        #print(k,v)
        cheat_savings.update((noncheat_time - v,))
    #return list(cheat_savings.items())
    savings_counts = set(())
    for time,count in sorted(list(cheat_savings.items()), key = lambda x: x[0]):
        if count > 0 and time > 0:
            if VERBOSE:
                print(f'{count:2d} savings of {time} ps')
            savings_counts.add((count,time))
    return savings_counts

def get_part1_answer(input, threshold):
    all_savings = part1(input, False)
    c = 0
    for count, time in all_savings:
        if time >= threshold:
            c += count
    return c

if __name__ == '__main__':
    tt = time.time()
    actual_input = open('c:/temp/day20_input.txt').read().split('\n')[:-1]
    print(f'Part 1 answer is {get_part1_answer(actual_input, 100)}. Done in {time.time()-tt:.1f}s')
