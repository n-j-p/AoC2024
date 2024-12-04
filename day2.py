import time
print()

# Sample data
sample_data = [[7, 6, 4, 2, 1],
               [1, 2, 7, 8, 9],
               [9, 7, 6, 2, 1],
               [1, 3, 2, 4, 5],
               [8, 6, 4, 4, 1],
               [1, 3, 6, 7, 9]]


# Read in actual data
fpath = '../day2_input.txt'
input = open(fpath).read().split('\n')
parsed = [[int(z) for z in x.split(' ')] for x in input[:-1]]

def is_safe(seq):
    xm = seq[0]
    inc = False
    if seq[1] >= xm:
        inc = True

    for x in seq[1:]:
        f = ((not inc) and x < xm) or (inc and x > xm)
        if (inc and x < xm) or ((not inc) and x > xm):
            #print('contains increase and decrease')
            return False # contains increase and decrease
        if (abs(x-xm) < 1):
            #print("Even levels")
            return False 
        if (abs(x-xm) > 3):
            #print(f"Step too large: {abs(x-xm)}")
            return False 
        xm = x
    return True


def part1(seqs):
    c = 0
    for seq in seqs:
        if is_safe(seq):
            c += 1
    return c

assert part1(sample_data) == 2

print(part1(parsed))


## Let's just apply is_safe function to popped sequences:

def seqrem(seq, i):
    assert i >= 0
    assert i < len(seq)
    seq2 = list(seq)
    seq2.pop(i)
    return seq2

def is_safe2(seq):
    if is_safe(seq):
        return True
    for i in range(len(seq)):
        if is_safe(seqrem(seq, i)):
            return True
    return False

def part2(seqs):
    c = 0
    for seq in seqs:
        if is_safe2(seq):
            c += 1
    return c

assert part2(sample_data) == 4

print(part2(parsed))
