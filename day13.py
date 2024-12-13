####################################
# # from my project euler functions:
    
def solveLinearDiophantine(a,b,n=1,return_increments=False):
    '''Solves (finds x,y) for the linear Diophantine equation ax+by=n.
    If return_increments, solveLinearDiophantine also returns increments for
    the full complement of solutions, i.e. if
    x,y,d,e = solveLinearDiophantine(a,b,n,True),
    then a(x+kd) + b(y+ke) = n for any integral k.'''
    assert a > 0
    assert b > 0
    assert n > 0
    x,y,d = eeuclid(a,b)
    
    if n % d == 0:
        if return_increments:
            return (x*(n//d),y*(n//d),b//d,-a//d)
        else:
            return (x*(n//d),y*(n//d))
    else:
        raise Exception('No solution')

def eeuclid(x,y):
    '''Extended Euclid algorithm for gcd and inverse.
    This implementation means the results need not be backtracked to find
    inverses and solution to linear Diophantine equations.
    Returns (a,b,g) such that ax + by = g = gcd(x,y)'''
    # Crandall and Pomerance, algo. 2.1.4

    assert x > 0
    assert y > 0

    SWAP = False
    if x > y:
        SWAP = True
        x,y=y,x
    
    olda = 1
    oldb = 0
    oldg = x
    u = 0
    v = 1
    w = y

    g = oldg

    while w > 0:
        q = g // w

        a = u
        b = v
        g = w
        u = olda - q*u
        v = oldb - q*v
        w = oldg - q*w

        olda = a
        oldb = b
        oldg = g
    if SWAP:
        return (b,a,g)
    else:
        return (a,b,g)


# e.g. 
# x,y,d,e = solveLinearDiophantine(a, b, n, True)
# Here we have ax + by = n
#
# # Also for integer k, we have
# a(x + kd) + b*(y + ke) = n

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


actual_input = open('c:/temp/day13_input.txt').read().split('\n')[:-1]

### part 2 (also use for part 1 with C = 0!)

def part2(inp_, VERBOSE = False, C = 0):
    all_solns = {}
    c = 0
    parsed = parse_input(inp_)
    for i, vals in enumerate(parsed):
        ax,bx,nx, ay,by,ny = vals
        try:
            xx,yx,dx,ex = solveLinearDiophantine(ax, bx, C + nx, True)  
            xy,yy,dy,ey = solveLinearDiophantine(ay, by, C + ny, True)  
        except Exception:
            if VERBOSE:
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
            if VERBOSE:
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
            if VERBOSE:
                print(i, 'no soln')
            continue
        kx = num // denom

        #print(xx + kx*dx, xy+ky*dy)
        assert xx + kx * dx == xy + ky * dy
        assert yx + kx * ex == yy + ky * ey
        A = xx + kx * dx
        B = yx + kx * ex
        if VERBOSE:
            print(f'{i} A = {A}, B = {B}, tokens = {3*A + B}')
        all_solns[i] = (A,B)
        c += 3*A + B
    return c, all_solns
C = 10000000000000
if __name__ == '__main__':
    print(f'Part 1 answer is {part2(actual_input)[0]}')
    print(f'Part 2 answer is {part2(actual_input, C = C)[0]}')
