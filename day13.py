import euclid

a = 94
b = 22
n = 8400
x,y,d,e = euclid.solveLinearDiophantine(a, b, n, True)
#print(x,y,d,e)
# Here we have ax + by = n

assert a*x + b*y == n

# Also for integer k, we have
# a(x + kd) + b*(y + ke) = n

assert a*(x + d) + b*(y + e) == n
assert a*(x + 2*d) + b*(y + 2*e) == n

# solution only makese sense if x + kd and y + ke are positive

assert x > 0
assert y < 0 

# so x + kd > 0 means
# x > -kd
# -k < x/d
# k > -x/d
#print(x,d,-x/d)

# y + ke > 0
# y > - ke
# -k < y/e
# k > -y/e
#print(y,e,-y/e)

# For first example:
#for k in range(-1519, -1529, -1):
#    print(k, x+k*d, y+k*e)

#import math
#for k in range(math.ceil(-x/d), math.ceil(-y/e)):
#    print(k, x+k*d, y+k*e)

def getk_positive(p,q,T):
    '''Returns (inclusive range for k), x, d, y and e yielding positive solutions to
    p*(x+kd) + q*(y+ke) = T
    '''
    import math, euclid
    x,y,d,e = euclid.solveLinearDiophantine(p, q, T, True)
    q = min(-x/d, -y/e)
    r = max(-x/d, -y/e)
    qp = int(math.floor(q))
    rp = int(math.ceil(r))

    f = lambda k: x+k*d
    g = lambda k: y+k*e

    # Just check that [qp+1, rp-1] are unique solutions for k giving 
    # positive values:
    #print(qp,f(qp),g(qp), rp, f(rp), g(rp))
    #assert f(qp)*g(qp) < 0
    #assert f(rp)*g(rp) < 0
    assert f(qp+1)*g(qp+1) >= 0
    assert f(rp-1)*g(rp-1) >= 0

    return ((qp+1, rp-1), x, d, y, e)

ks, x, d, y, e = getk_positive(a,b,n)
print(ks,x,d,y,e)

def get_range(p_, q_, T_):
    ks, x, d, y, e = getk_positive(p_,q_,T_)

    all_pos = []
    for k in range(ks[0], ks[1]+1):
        #print(x+k*d, y+k*e, p*(x+k*d) + q*(y+k*e))
        assert x+k*d > 0
        assert y+k*e > 0
        assert p_*(x+k*d) + q_*(y+k*e) == T_
        all_pos.append((x+k*d, y+k*e))
    #print('  ', all_pos)
    return all_pos

ay, by = 34, 67
Ty = 5400
print(getk_positive(ay,by,Ty))

print(get_range(a,b,n))
print(get_range(ay,by,Ty))

def find_solutions(ax,bx,Tx, ay,by,Ty):
    return set(get_range(ax,bx,Tx)).intersection(get_range(ay,by,Ty))

print(find_solutions(a,b,n,ay,by,Ty))

sample_values = [(94, 34, 8400, 22, 67, 5400),
                 (26, 66, 12748, 67, 21, 12176),
                 (17, 86, 7870, 84, 37, 6450),
                 (69, 23, 18641, 27, 71, 10279)]

for vs in sample_values:
    try:
        print(find_solutions(*vs))
    except Exception:
        print('no solution')
print()
print(find_solutions(*sample_values[2]))

print(get_range(*sample_values[2][:3]))
print(get_range(*sample_values[2][3:]))
print(euclid.solveLinearDiophantine(*sample_values[2][:3], True))
print(getk_positive(*sample_values[2][:3]))
print(euclid.solveLinearDiophantine(*sample_values[2][3:], True))
print(getk_positive(*sample_values[2][3:]))


sample_input = ['Button A: X+94, Y+34',
    'Button B: X+22, Y+67',
    'Prize: X=8400, Y=5400',
    '',
    'Button A: X+26, Y+66',
    'Button B: X+67, Y+21',
    'Prize: X=12748, Y=12176',
    '',
    'Button A: X+17, Y+86',
    'Button B: X+84, Y+37',
    'Prize: X=7870, Y=6450',
    '',
    'Button A: X+69, Y+23',
    'Button B: X+27, Y+71',
    'Prize: X=18641, Y=10279']

def parse_input(inp_):
    vals = {}
    lvals = []
    for row in inp_ + ['',]:
        if len(row) == 0:
            #print(vals)
            lval = (vals['A'][0], vals['B'][0], vals['Prizes'][0], vals['A'][1], vals['B'][1], vals['Prizes'][1])
            lvals.append(lval)
            vals = {}
        elif row.count('Prize') > 0:
            i,j,k,l = row.index('X='), row.index(','), row.index('Y='), len(row)
            vals['Prizes'] = (int(row[(i+2):j]), int(row[(k+2):l]))
            pass
        elif row.count('Button A') > 0:
            i,j,k,l = row.index('X+'), row.index(','), row.index('Y+'), len(row)
            vals['A'] = (int(row[(i+2):j]), int(row[(k+2):l]))
        elif row.count('Button B') > 0:
            i,j,k,l = row.index('X+'), row.index(','), row.index('Y+'), len(row)
            vals['B'] = (int(row[(i+2):j]), int(row[(k+2):l]))
        else:
            raise Exception
    return(lvals)

lvals_ = parse_input(sample_input)

print('\n'*10)
print(lvals_)
print('---')
all_solns = {}
for i,lval in enumerate(lvals_):
    print(lval)
    try:
        soln = find_solutions(*lval) 
        print(soln)
        all_solns[i] = soln
    except Exception:
        print('no solution')
#print(find_solutions(*(94,34,8400,22,67,5400)))

#print(lvals[0])
#print(get_range(94,22,8400))

# print('xxx')
# print(euclid.solveLinearDiophantine(17,84,7870, True))
# print(get_range(17,84,7870))
# print(getk_positive(17,84,7870))
# print('xxx')
# print(euclid.solveLinearDiophantine(86,37,6450, True))
# print(get_range(86,37,6450))
# print(getk_positive(86,37,6450))

print('\n', all_solns)

actual_input = open('c:/temp/day13_input.txt').read().split('\n')[:-1]
print(actual_input)

import pdb
lvals__ = parse_input(actual_input)
all_solns = {}
for i,lval in enumerate(lvals__):
    print(lval)
    try:
        soln = find_solutions(*lval) 
        print(soln)
        all_solns[i] = soln
    except Exception:
        print('no solution')

print(all_solns)

c = 0
for k in all_solns:
    AB = all_solns[k]
    if AB == set(()): continue
    print(list(AB)[0])
    print(AB)
    A, B = list(AB)[0]
    c += 3 * A + B
print('Part 1 answer is', c)

### part 2

#print(parse_input(sample_input))

import numpy as np
from numpy.linalg import solve
def part2(inp_, C = 0):
    c = 0
    parsed = parse_input(inp_)
    for i, vals in enumerate(parsed):
        ax,bx,nx, ay,by,ny = vals
        try:
            xx,yx,dx,ex = euclid.solveLinearDiophantine(ax, bx, C + nx, True)  
            xy,yy,dy,ey = euclid.solveLinearDiophantine(ay, by, C + ny, True)  
        except Exception:
            print(i, 'no soln')
            continue
        # We have the following sim. equations:
        # x_x + k_x . d_x = x_y + k_y . d_y (1)
        # y_x + k_x . e_x = y_y + k_y . e_y (2)
        # We need to solve for k_x and k_y
        # Do (1a) = (1) * e_x  and  (2a) = (2) * d_x:
        # x_x . e_x + k_x . d_x . e_x = x_y . e_x + k_y . d_y . e_x (1a)
        # y_x . d_x + k_x . e_x . d_x = y_y . d_x + k_y . e_y . d_x (2a)
        #    (1a) - 2(a):
        # x_x.e_x - y_x.d_x           = x_y.e_x - y_y.d_x + k_y.d_y.e_x - k_y.e_y.d_x
        # xx.ex - yx.dx = xy.ex - yy.dx + ky(dy.ex-ey.dx)
        # ky(dy.ex-ey.dx) = xx.ex - yx.dx - xy.ex + yy.dx
        #
        # ky = (xx.ex - yx.dx - xy.ex + yy.dx) / (dy.ex - ey.dx)
        num = xx*ex - yx*dx - xy*ex + yy*dx
        denom = dy*ex - ey*dx
        #print(num, denom)
        if num % denom != 0:
            print(i, 'no soln')
            continue
        ky = num // denom
        #print(ky)
        # sub back into (1)
        # xx + kx.dx = xy + ky.dy
        # kx.dx = xy + ky.dy - xx
        # 
        num = xy + ky*dy - xx
        denom = dx
        if num % denom != 0:
            print(i, 'no soln')
            continue
        kx = num // denom

        # A = np.array(((dx, -dy),
        #               (ex, -ey)))
        # b = np.array((xy-xx, yy-yx))
        # print(A)
        # print(b)
        # print(solve(A,b))
        # kx, ky = solve(A,b)
        #kx = int(kx)
        #ky = int(ky)
        print(xx + kx*dx, xy+ky*dy)
        assert xx + kx * dx == xy + ky * dy
        assert yx + kx * ex == yy + ky * ey
        A = xx + kx * dx
        B = yx + kx * ex
        print(f'{i} A = {A}, B = {B}, tokens = {3*A + B}')
        c += 3*A + B
    return c
C = 10000000000000
print(f'Part 1 sample answer is {part2(sample_input)}')
print(f'Part 1 actual answer is {part2(actual_input)}')
print(f'Part 2 sample answer is {part2(sample_input, C = C)}')
print(f'Part 2 actual answer is {part2(actual_input, C = C)}')
