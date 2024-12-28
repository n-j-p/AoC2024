def mix(a, b):
    return a ^ b
def prune(a, MOD):
    return a % MOD
def evolve(secret, MOD = 16777216):
    # Step 1
    result = secret * 64
    secret = prune(mix(result, secret),MOD)

    # Step 2
    result = secret // 32
    secret = prune(mix(result, secret),MOD)
    
    # Step 3
    result = secret * 2048
    secret = prune(mix(result, secret),MOD)

    return secret

def evolve_n(secret, n):
    for i in range(n):
        secret = evolve(secret)
    return secret

def gen_prices(secret):
    while True:
        yield secret % 10
        secret = evolve(secret)

def gen_diffs(secret):
    gp = gen_prices(secret)
    last = next(gp)
    while True:
        num = next(gp)
        yield num - last
        last = num

# Function nont really needed...
def occurrence(secret, seq, maxn=2000):
    assert seq.__class__ == list
    from collections import deque
    test = deque(maxlen=len(seq))
    last_price = None
    g = gen_diffs(secret)
    last_price = secret % 10
    for i in range(maxn):
        diff = next(g)
        last_price = last_price + diff
        test.append(diff)
        if list(test) == list(seq):
            return last_price
    return None


def iterate(secret,maxn=2000):
    from collections import deque
    last4 = deque(maxlen=4)
    bids = {}
    last_price = secret % 10
    g = gen_diffs(secret)
    for i in range(4):
        diff = next(g)
        last_price += diff
        #print(diff)
        last4.append(diff)
        #print(tuple(last4), last_price)

    for i in range(maxn-4):
        diff = next(g)
        last_price += diff
        #print(diff)
        last4.append(diff)
        tlast4 = tuple(last4)
        #print(tlast4,last_price)
        if tlast4 not in bids:
            bids[tlast4] = last_price
    return bids
        

def part2(secrets):
    import tqdm
    all_bids = {}
    print('Iterating bids')
    for secret in tqdm.tqdm(secrets):
        bids_i = iterate(secret)
        for seq in bids_i:#tqdm.tqdm(bids_i):
            if seq in all_bids:
                all_bids[seq][secret] = bids_i[seq]
            else:
                all_bids[seq] = {secret: bids_i[seq]}
    print(len(all_bids))
    print('Summing bids')
    max_bananas = 0
    max_seq = None
    for seq in tqdm.tqdm(all_bids):
        bananas = sum(all_bids[seq].values())
        if bananas > max_bananas:
            max_bananas = bananas
            max_seq = seq
    return (max_seq, max_bananas)

if __name__ == '__main__':
    import tqdm
    actual_input = open('c:/temp/day22_input.txt').read().split('\n')[:-1]
    c = 0
    for x in tqdm.tqdm(actual_input):
        c += evolve_n(int(x), 2000)
    print('Part 1 answer is',c)

    print('Part 2 answer is ',part2([int(x) for x in actual_input]))
