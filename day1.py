import time
from collections import Counter
print()

# Sample data
sample_list0 = [3,4,2,1,3,3]
sample_list1 = [4,3,5,3,9,3]

# Read in actual data
fpath = '../input.txt'
input = open(fpath).read().split('\n')
parsed = [[int(z) for z in x.split('   ')] for x in input[:-1]]
list0, list1 = zip(*parsed)


### Part 1 ###
def part1(x,y):
    c = 0
    for ab in zip(sorted(x), sorted(y)):
        c += abs(ab[0] - ab[1])
    return c

assert part1(sample_list0,
             sample_list1) == 11

tt = time.time()
print(f'Part 1 answer is {part1(list0, list1)}, done in {time.time()-tt:.2f}s')

### Part 2
def part2(x,y):
    cc = Counter()
    cc.update(y)
    c = 0
    for a in x:
        c += a * cc[a]
    return c

assert part2(sample_list0,
             sample_list1) == 31

tt = time.time()
print(f'Part 2 answer is {part2(list0, list1)}, done in {time.time()-tt:.2f}s')
