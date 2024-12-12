import time

inp0 = '0 1 10 99 999'
class Stones():
    def __init__(self, input):
        self.stones = [int(x) for x in input.split(' ')]
    def blink(self, times=1):
        for _ in range(times):
            for i in range(len(self.stones))[::-1]:
                #print(i, self.stones[i])
                stone_str = str(self.stones[i])
                if self.stones[i] == 0:
                    self.stones[i] = 1
                elif len(stone_str) % 2 == 0:
                    Lst = int(stone_str[:len(stone_str)//2])
                    Rst = int(stone_str[(len(stone_str)//2):])
                    #print(Lst, Rst)
                    self.stones[i] = int(Lst)
                    self.stones.insert(i+1, int(Rst))
                else:
                    self.stones[i] = 2024 * self.stones[i]


stones0 = Stones(inp0)

print(stones0.stones)
stones0.blink()
newstones0 = stones0.stones 
print(newstones0)
assert newstones0 == [1,2024,1,0,9,9,2021976]

sample_input = '125 17'
def part1(inp, times):
    stones = Stones(inp)
    stones.blink(times)
    return len(stones.stones)
print(part1(sample_input, 6))
print(part1(sample_input, 25))

actual_input = open('c:/temp/day11_input.txt').read().split('\n')[0]
print(actual_input)
tt = time.time()
print(f'Part 1 answer is {part1(actual_input, 25)}. Done in {time.time()-tt:.1f}s')
#tt = time.time()
#print(f'Part 2 answer is {part1(actual_input, 75)}. Done in {time.time()-tt:.1f}s')

test1 = Stones(sample_input)
test1.blink(25)
print(len(test1.stones))
from collections import Counter
print(Counter(test1.stones))

import pdb
class Stones2():
    def __init__(self, input):
        stones0 = [int(x) for x in input.split(' ')]
        self.stonesc = dict(Counter(stones0))
    def blink(self, times=1):
        for _ in range(times):
            new_stonesc = {}
            for i,x in enumerate(self.stonesc.items()):
                #pdb.set_trace()
                stone_str = str(x[0])
                count = x[1]
                if stone_str == '0':
                    try:
                        new_stonesc[1] += count
                    except KeyError:
                        new_stonesc[1] = count
                elif len(stone_str) % 2 == 0:
                    Lst = int(stone_str[:len(stone_str)//2])
                    Rst = int(stone_str[(len(stone_str)//2):])
                    try:
                        new_stonesc[Lst] += count
                    except KeyError:
                        new_stonesc[Lst] = count
                    try:
                        new_stonesc[Rst] += count
                    except KeyError:
                        new_stonesc[Rst] = count
                else:
                    try:
                        new_stonesc[x[0] * 2024] += count
                    except KeyError:
                        new_stonesc[x[0] * 2024] = count
            self.stonesc = dict(new_stonesc)

test2 = Stones2(sample_input)
print(test2.stonesc)
test2.blink()
print(test2.stonesc)
test2.blink()
print(test2.stonesc)
test2.blink()
print(test2.stonesc)
test2.blink()
print(test2.stonesc)
test2.blink()
print(test2.stonesc)
test2.blink()
print(test2.stonesc)

def part2(inp, times):
    stones = Stones2(inp)
    stones.blink(times)
    return sum(stones.stonesc.values())

for t in [25,30,35,40,45,50,55,60,65,70,75]:
    tt = time.time()
    print(f'{t}: {part2(actual_input, t)}, {time.time()-tt:.1f}s')
