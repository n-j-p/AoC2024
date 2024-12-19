import re
import time

sample_input = open('c:/temp/day19_sample_input.txt').read().split('\n')[:-1]

def f(target, pattern_res):
    if len(target) == 0:
        yield [target,]
        return
    for i,ps in enumerate(pattern_res):
        if ps[0].match(target) is not None:          
            for x in f(re.sub(ps[0],'',target), pattern_res):
                yield [ps[1],] + x
            
        
                      

def slow_part1(inp, VERBOSE = True):
    cached = {}
    patterns = [x.lstrip() for x in inp[0].split(',')]
    designs = inp[2:]
    c = 0
    ci = 0
    for design in designs:
        ci = 0
        for x in f(design, tuple([(re.compile('^' + s), s) for s in patterns])):
            if VERBOSE:
                print(x[:-1])
            ci += 1
        if VERBOSE:
            print(design, ci)
        c += ci
    return c


print(slow_part1(sample_input))
actual_input = open('c:/temp/day19_input.txt').read().split('\n')[:-1]
# Doesn't work for actual_input:
#print(slow_part1(actual_input))

# Dynamic programming approach
# For a given target, work from left-to-right.
# If a pattern matches the target from the given index,
# increment the count at current position plus length of matching pattern`
def DP(target, pattern_res):
    count = [1,] + [0,] * len(target)
    for n in range(len(target)):
        for i,ps in enumerate(pattern_res):
            if ps[0].match(target[n:]) is not None:          
                # i.e. target[n:] matches start of pattern
                try:
                    count[n + len(ps[1])] += count[n]
                except IndexError: # This takes us past the end of the target string
                    pass
    return count[n+1]

def test1(inp, VERBOSE=True, part2=False):
    patterns = [x.lstrip() for x in inp[0].split(',')]
    designs = inp[2:]
    re_patterns = tuple([(re.compile('^' + s), s) for s in patterns])
    c = 0
    for design in designs:
        ans = DP(design, re_patterns)
        if VERBOSE:
            print(design, ans)
        if ans > 0:
            if part2:
                c += ans
            else:
                c += 1
    return c

tt = time.time()
print(f'Part 1 sample answer is {test1(sample_input)}. Done in {time.time()-tt:.1f}s.')
tt = time.time()
print(f'Part 1 actual answer is {test1(actual_input, False)}. Done in {time.time()-tt:.1f}s.')
tt = time.time()
print(f'Part 2 actual answer is {test1(actual_input, False, part2=True)}. Done in {time.time()-tt:.1f}s.')
