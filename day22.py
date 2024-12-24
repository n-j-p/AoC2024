
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

if __name__ == '__main__':
    import tqdm
    actual_input = open('c:/temp/day22_input.txt').read().split('\n')[:-1]
    c = 0
    for x in tqdm.tqdm(actual_input):
        c += evolve_n(int(x), 2000)
    print('Part 1 answer is',c)

    

