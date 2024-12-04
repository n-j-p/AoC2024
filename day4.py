# This could be cleaned up significantly...
#
# Basically, I use re to search for XMAS, SAMX, etc. strings in:
#   1. the input matrix by rows, which gives L-R occurrences,
#   2. the transpose of the input matrix, which gives U-D occurrences,
#   3. diagonal offset (ragged) matrix (inpa_tri), which gives NW-SE 
#           (backslash) occurrences,
#   4. anti-diagonal offset matrix (inpa_tri2), giving SW-NE (slash)
#           occurrences
#
# For part 2, there is some fiddling around with converting matrix (i,j) 
# coordinates to diagonal-offset and antidiagonal-offset coordinates

sample_input = ['MMMSXXMASM',
                 'MSAMXMSMSA',
                 'AMXSXMAAMM',
                 'MSAMASMSMX',
                 'XMASAMXAMM',
                 'XXAMMXXAMA',
                 'SMSMSASXSS',
                 'SAXAMASAAA',
                 'MAMMMXMMMM',
                 'MXMXAXMASX']

fpath = '../../day4_input.txt'
actual_inp = open(fpath).read().split('\n')[:-1]

inp = list(sample_input)
inp = actual_inp

R = len(inp)
C = len(inp[0])

assert R == C

import numpy as np
import re



inpa = np.array([list(x) for x in inp])

inpa_ud = inpa.T

# This looks in backslash diagonals
inpa_tri = [np.diag(inpa,i) for i in np.arange(-(R-1),R)]

# This looks in slash diagonals
inpa_tri2 = [np.diag(np.flipud(inpa),i) for i in np.arange(-(R-1),R)]

xmas = re.compile('XMAS')
samx = re.compile('SAMX')

c = 0

print('count of L-R XMAS by row:')
t1 = [len(list(xmas.finditer(r))) for r in [''.join(x) for x in inpa]]
print(t1)
c += sum(t1)

print('count of R-L XMAS by row:')
t2=[len(list(samx.finditer(r))) for r in [''.join(x) for x in inpa]]
print(t2)
c += sum(t2)

print('count of U-D XMAS by col:')
t3=[len(list(xmas.finditer(r))) for r in [''.join(x) for x in inpa_ud]]
print(t3)
c += sum(t3)

print('count of D-U XMAS by col:')
t4=[len(list(samx.finditer(r))) for r in [''.join(x) for x in inpa_ud]]
print(t4)
c += sum(t4)

print('count of NW-SE XMAS by diagonal offset from SW corner:')
t5=[len(list(xmas.finditer(r))) for r in [''.join(x) for x in inpa_tri]]
print(t5)
c += sum(t5)

print('count of SE-NW XMAS by diagonal offset from SW corner:')
t6=[len(list(samx.finditer(r))) for r in [''.join(x) for x in inpa_tri]]
print(t6)
c += sum(t6)

print('count of SW-NE XMAS by diagonal offset from NW corner:')
t7=[len(list(xmas.finditer(r))) for r in [''.join(x) for x in inpa_tri2]]
print(t7)
c += sum(t7)

print('count of NE-SW XMAS by diagonal offset from NW corner:')
t8=[len(list(samx.finditer(r))) for r in [''.join(x) for x in inpa_tri2]]
print(t8)
c += sum(t8)

print(c)




mas = re.compile('MAS')
sam = re.compile('SAM')

print('index of NW-SE MAS by diagonal offset from SW corner:')
x5=[[y.start() for y in mas.finditer(z)] for z in \
       [''.join(x) for x in inpa_tri]]
print(x5)

print('index of NW-SE SAM by diagonal offset from SW corner:')
x6=[[y.start() for y in sam.finditer(z)] for z in \
       [''.join(x) for x in inpa_tri]]
print(x6)

print('index of SW-NE MAS by diagonal offset from NW corner:')
x7=[[y.start() for y in mas.finditer(z)] for z in \
       [''.join(x) for x in inpa_tri2]]
print(x7)

print('index of SW-NE SAM by diagonal offset from NW corner:')
x8=[[y.start() for y in sam.finditer(z)] for z in \
       [''.join(x) for x in inpa_tri2]]
print(x8)


# Converting xy coordinates to diagonal, offset coordinates starting
# with (0,0) at SW corner, (1,0), (1,1) along next NW-SE diagonal, etc.
def coord2diag(row, col, N):
    return N - 1 + col - row, min(col, row)
# Inverse function
def diag2coord(diag, offset, N):
    diag_i = diag - (N - 1)
    x0 = max(0, -diag_i)
    y0 = max(0, diag_i)
    #print(x0,y0)
    return (x0+offset,y0+offset)

# Same but for antidiagonals starting from NW corner
def coord2antidiag(row, col, N):
    # equivalent to coord2diag on a flipud'ed matrix
    row = N - 1 - row
    return coord2diag(row, col, N)
def antidiag2coord(antidiag, offset, N):
    flipped = diag2coord(antidiag, offset, N)
    return (N - 1 - flipped[0], flipped[1]) 

# Now let's locate coordinates of "A" as part of NW-SE sequences:
import itertools as it
Acoords = []
Mdiagcoords = []
for i,x in enumerate(x5):
    Mdiagcoords += list(zip(it.repeat(i), x))
for diagcoord in Mdiagcoords:
    Mcoord = diag2coord(*diagcoord, R)
    print(diagcoord, Mcoord)
    # Location of a is 1 square SE of the position of the M
    Acoords += [(Mcoord[0]+1, Mcoord[1]+1)]

print('-0-')
Sdiagcoords = []
for i,x in enumerate(x6):
    Sdiagcoords += list(zip(it.repeat(i), x))
for diagcoord in Sdiagcoords:
    Scoord = diag2coord(*diagcoord, R)
    print(diagcoord, Scoord)
    Acoords += [(Scoord[0]+1, Scoord[1]+1)]

print('-----\nNE-SW\n-------')
# and for NE-SW sequences:
Acoords2 = []
Mantidiagcoords = []
for i,x in enumerate(x7):
    Mantidiagcoords += list(zip(it.repeat(i), x))
for antidiagcoord in Mantidiagcoords:
    Mcoord = antidiag2coord(*antidiagcoord, R)
    print(antidiagcoord, Mcoord)
    # Location of A is 1 square NE of the position of the M
    Acoords2 += [(Mcoord[0]-1, Mcoord[1]+1)]

print('-0-')
Santidiagcoords = []
for i,x in enumerate(x8):
    Santidiagcoords += list(zip(it.repeat(i), x))
for antidiagcoord in Santidiagcoords:
    Scoord = antidiag2coord(*antidiagcoord, R)
    print(antidiagcoord, Scoord)
    Acoords2 += [(Scoord[0]-1, Scoord[1]+1)]

# Now intersect coordinates of "A" to get middle coordinates of all X-MASes:
X_MAS_middle_coords = set(Acoords).intersection(Acoords2)

print()
print(f'Answer to part 2 is {len(X_MAS_middle_coords)}')
