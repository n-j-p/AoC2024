print()
sample_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

import re
mul = re.compile('mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)')

def multiply(astr):
    c = 0
    for x in mul.findall(astr):
        #print(x,x[0],x[1], int(x[0])*int(x[1]))
        c += int(x[0])*int(x[1])
    return(c)
assert multiply(sample_string) == 161

### Part 1

fpath = 'input/day3_input.txt'
inp = open(fpath).read().split('\n')

c = 0
for string in inp:
    r = multiply(string)
    c += r
print(f'Part 1 answer is {c}')

### Part 2

sample_string2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
stop = re.compile("don't\(\)")
start = re.compile("do\(\)")


# This function censors over disabled part of the string:
    
def censor_string(astring):
    ss2 = astring
    last_start = -1
    for i in stop.finditer(astring):
        if i.start() < last_start:
            continue
        for j in start.finditer(astring):
            if j.start() < i.end():
                continue
            last_start = j.end()
            ss2 = ss2[:i.start()] + 'X' * (j.end()-i.start()) + ss2[j.end():]
            break

    # If the line ends with don't, truncate it
    last_stop = list(stop.finditer(astring))[-1]
    last_start = list(start.finditer(astring))[-1]
          
    if last_stop.end() > last_start.start():
        ss2 = ss2[:last_stop.start()]
    return ss2

# Example:

print()
print("Replace string between don't and do with Xs (i.e. censor that part)")
print("-----------")
print(sample_string2)
print(censor_string(sample_string2))


print()
print("If the string ends with a don't with no following do, just truncate")
print("-----------")
ss3 = "mul(1,1)don't()mul(2,2)do()mul(3,3)don't()mul(4,4)"
print(ss3)
print(censor_string(ss3))




part2_example = multiply(censor_string(sample_string2))
assert part2_example == 48

print()

if False: # We need to treat the entire input as one big string...
    c = 0
    for string in inp[:-1]:
        r = multiply(censor_string(string))
        c += r
    print(f'Part 2 answer is {c}')


print(f"Part 2 answer is {multiply(censor_string(''.join(inp)))}")
