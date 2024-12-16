#import pdb

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
        self.lowest_score = {}

        cur = (self.locate_start(), 1) # 0 represents north, 1 east, etc.
        # Assume there is no point doing a 180 degree turn at any time.
        # Even if we have reached a dead end, it would have been cheaper to 
        # have turned the other way at the nearest intersection than to have 
        # turned 180 degrees and walked backwards.
        self.lowest_score[cur] = 0
        nxt = [cur,]
        while len(nxt) > 0:
            cur = nxt.pop(0)
            cur_pos = cur[0]
            cur_dir = cur[1]

            for delta_dir in [-1, 0, 1]: # i.e anti-clockwise turn, straight, and clockwise turn
                nxt_dir = (cur_dir + delta_dir) % 4
                nxt_pos = self._get_nxt_pos(cur_pos, 
                                            nxt_dir)
                if self._what(nxt_pos) == 'E':
                    #pdb.set_trace()
                    print('End of maze reached')
                    if (nxt_pos, nxt_dir) not in self.lowest_score:
                        self.lowest_score[(nxt_pos, nxt_dir)] = self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir)
                    elif self.lowest_score[(nxt_pos, nxt_dir)] > self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir):
                        self.lowest_score[(nxt_pos, nxt_dir)] = self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir)
                    else: # Already a better way to get to the next square, do not add to nxt
                        pass

                elif self._what(nxt_pos) == '.':
                    if (nxt_pos, nxt_dir) not in self.lowest_score:
                        self.lowest_score[(nxt_pos, nxt_dir)] = self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir)
                        nxt.append((nxt_pos, nxt_dir))
                    elif self.lowest_score[(nxt_pos, nxt_dir)] > self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir):
                        self.lowest_score[(nxt_pos, nxt_dir)] = self.lowest_score[(cur_pos, cur_dir)]+\
                            1 + 1000*(cur_dir != nxt_dir)
                        nxt.append((nxt_pos, nxt_dir))
                    else: # Already a better way to get to the next square, do not add to nxt
                        pass


                else: # hit a wall
                    pass

            #print(nxt)
            #print(self.lowest_score)
        import numpy as np
        min_score = np.inf
        for dir in range(4):
            try:
                min_score = min(min_score, self.lowest_score[(self.locate_end(), dir)])
            except KeyError:
                pass
        return min_score
            
            

if __name__ == '__main__':
    actual_input = open('c:/temp/day16_input.txt').read().split('\n')[:-1]
    import time
    tt = time.time()
    maze = Maze(actual_input)

    actual_part1_answer = maze.traverse()
    print(f'Part 1 answer is {actual_part1_answer}. Done in {time.time()-tt:.1f}s')
