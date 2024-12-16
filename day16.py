import pdb

class Path():
    def __init__(self, score, ops):
        self.score = score
        self.ops = ops
    def __repr__(self):
        repr_str = f'${self.score}: '
        for op in self.ops:
            repr_str += op.__repr__() + ' -> '
        return repr_str[:-4]
    def next(self, score_increment, nxt_op): # add a new op to existing Path and adjust score
        new_path = Path(self.score, self.ops)
        new_path.score = new_path.score + score_increment
        new_path.ops = new_path.ops + [nxt_op,]
        return new_path
class OrientedPosition():
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
    def __eq__(self,other):
        if self.position == other.position and self.direction == other.direction:
            return True
        return False
    def __hash__(self): # Need hash function to allow this as a dictionary key
        return hash((self.position[0], self.position[1], self.direction))
    def __repr__(self):
        dir_repr = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}
        return f'{self.position}/{dir_repr[self.direction]}'
class Maze():
    def __init__(self,inp):
        self.inp = inp
    def _what(self, pos):
        return self.inp[pos[0]][pos[1]]
    def locate_start(self):
        for i,r in enumerate(self.inp):
            for j,x in enumerate(r):
                if x == 'S':
                    return((i,j))
    def locate_end(self):
        for i,r in enumerate(self.inp):
            for j,x in enumerate(r):
                if x == 'E':
                    return((i,j))

    def _get_nxt_pos(self, pos, dir):

        if dir == 0:
            nxt_pos = (pos[0] - 1, pos[1])
        elif dir == 1:
            nxt_pos = (pos[0], pos[1] + 1)
        elif dir == 2:
            nxt_pos = (pos[0] + 1, pos[1])
        elif dir == 3:
            nxt_pos = (pos[0], pos[1] - 1)
        else:
            raise ValueError('Unknown direction, should be 0-3')
        return nxt_pos
    def traverse(self):
        '''Traverse the map as a tree. 
        Keep track of position and orientation.'''
        # For part 2, keep a record of traversed path in the self.lowest_score
        # We'll do this with a dictionary: keys hold OrientedPositions instances (position and
        # directions), and items are minimum cost path(s) getting there. This needs to be a list
        # as there are multiple minimum-cost ways to get to certain states.
        self.lowest_score = {}

#        cur = (self.locate_start(), 1) # 0 represents north, 1 east, etc.
        cur_op = OrientedPosition(self.locate_start(), 1) # 0 represents north, 1 east, etc.
        
        # Assume there is no reason for doing a 180 degree turn at any time.
        # Even if we have reached a dead end, it would have been cheaper to 
        # have turned the other way at the nearest intersection than to have 
        # turned 180 degrees and walked backwards.
#        self.lowest_score[cur] = [0, [cur,]]
        self.lowest_score[cur_op] = [Path(0, [cur_op,]),]
        nxt = [cur_op,] # list of next positions/directions to traverse
        while len(nxt) > 0:
            cur = nxt.pop(0)
            if cur.position == (9,3) and cur.direction == 0:
                pass#pdb.set_trace()
#            cur_pos = cur[0]
#            cur_dir = cur[1]

            for delta_dir in [-1, 0, 1]: # i.e anti-clockwise turn, straight, and clockwise turn
#                nxt_dir = (curdir + delta_dir) % 4
                nxt_dir = (cur.direction + delta_dir) % 4
#                nxt_pos = self._get_nxt_pos(cur_pos, 
#                                            nxt_dir)
                nxt_op = OrientedPosition(self._get_nxt_pos(cur.position,
                                                         nxt_dir),
                                          nxt_dir)
                if self._what(nxt_op.position) in ['.', 'E']:
                    #pdb.set_trace()
#                    if (nxt_pos, nxt_dir) not in self.lowest_score:
                    if nxt_op not in self.lowest_score: # We haven't reached this yet
                                                        # Always add this to minimum-cost dict
#                        self.lowest_score[(nxt_pos, nxt_dir)] = [self.lowest_score[(cur_pos, cur_dir)][0]+\
#                            1 + 1000*(cur_dir != nxt_dir),]

#                        nxt_score = self.lowest_score[cur][0].score + 1 + 1000*(cur.direction != nxt_op.direction)
                        # Add new score and next position/direction to lowest_score dict
#                        nxt_path = self.lowest_score[cur][0].next(1 + 1000*(cur.direction != nxt_op.direction), # score increment
#                                                                  nxt_op)
                        nxt_paths = [cur_paths.next(1 + 1000*(cur.direction != nxt_op.direction), # score increment
                                                    nxt_op) for cur_paths in self.lowest_score[cur]]
                        self.lowest_score[nxt_op] = nxt_paths

                        # Add to list of next positions to traverse, unless we are at the end
#                        nxt.append((nxt_pos, nxt_dir))
                        if self._what(nxt_op.position) != 'E':
                            nxt.append(nxt_op)
#                    elif True:#self.lowest_score[(nxt_pos, nxt_dir)][0] > self.lowest_score[(cur_pos, cur_dir)][0]+\
#                            #1 + 1000*(cur_dir != nxt_dir):
                    elif self.lowest_score[nxt_op][0].score == self.lowest_score[cur][0].score + 1 + 1000*(cur.direction != nxt_op.direction):

                        #pdb.set_trace()
                        # Equal cost way of getting here
                        pass
                        nxt_paths = [cur_paths.next(1 + 1000*(cur.direction != nxt_op.direction), # score increment
                                                    nxt_op) for cur_paths in self.lowest_score[cur]]
                        self.lowest_score[nxt_op] += nxt_paths

#                        self.lowest_score[(nxt_pos, nxt_dir)] = [self.lowest_score[(cur_pos, cur_dir)][0]+\
#                            1 + 1000*(cur_dir != nxt_dir),]
#                        nxt.append((nxt_pos, nxt_dir))
                        if self._what(nxt_op.position) != 'E':
                            if nxt_op not in nxt:
                                nxt.append(nxt_op)
                    elif self.lowest_score[nxt_op][0].score > self.lowest_score[cur][0].score + 1 + 1000*(cur.direction != nxt_op.direction):
                        #pdb.set_trace()
                        # This is a better way of getting here
                        pass
                        nxt_paths = [cur_paths.next(1 + 1000*(cur.direction != nxt_op.direction), # score increment
                                                    nxt_op) for cur_paths in self.lowest_score[cur]]
                        self.lowest_score[nxt_op] = nxt_paths
                        if self._what(nxt_op.position) != 'E':
                            if nxt_op not in nxt:
                                nxt.append(nxt_op)
                    else: # Already a better way to get to the next square, do not add to nxt
                        continue

                    #pdb.set_trace()
                    # Add to lowest_score
#                    self.lowest_score[(nxt_pos, nxt_dir)].append(self.lowest_score[(cur_pos, cur_dir)][1] + [(nxt_pos, nxt_dir),])



                else: # hit a wall
                    pass

            #print(nxt)
        #print(self.lowest_score)
        #pdb.set_trace()
        import numpy as np
        final_paths = []
        min_score = np.inf
        for dir in range(4):
            op = OrientedPosition(self.locate_end(), dir)
            try:
                final_score = self.lowest_score[op][0].score
            except KeyError:
                continue

            if final_score < min_score:
                final_paths = [x for x in self.lowest_score[op]]
                min_score = final_score
            elif final_score == min_score:
                final_paths += [x for x in self.lowest_score[op]]

#        final_paths = {k: v for k,v in self.lowest_score.items() if k[0] == self.locate_end() and v[0] == min_score}
        return min_score, final_paths
            
            

def part2(inp):
    maze = Maze(inp)

    result = maze.traverse()
    all_paths = result[1]
    all_ops = [x.ops for x in all_paths]
    all_tiles = [[x.position for x in ops] for ops in all_ops]
    unique_tiles = set(())
    for tiles in all_tiles:
        unique_tiles.update(tiles)
    return len(unique_tiles)

if __name__ == '__main__':
    actual_input = open('c:/temp/day16_input.txt').read().split('\n')[:-1]
    import time
    tt = time.time()
    maze = Maze(actual_input)

    ans = maze.traverse()
    actual_part1_answer = ans[0]
    print(f'Part 1 answer is {actual_part1_answer}. Done in {time.time()-tt:.1f}s')

    #print(ans[1])

    tt = time.time()
    print(f'Part 2 answer is {part2(actual_input)}. Done in {time.time()-tt:.1f}s')

