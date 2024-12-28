import day22
def test_10():
    assert day22.evolve_n(123, 10) == 5908254

def test_2000():
    assert day22.evolve_n(1, 2000) ==  8685429
    assert day22.evolve_n(10, 2000) == 4700978
    assert day22.evolve_n(100, 2000) == 15273692
    assert day22.evolve_n(2024, 2000) == 8667524

def test_sample():
    sample_input = [1, 10, 100, 2024]
    c = 0
    for n in sample_input:
        c += day22.evolve_n(n, 2000)
    assert c == 37327623

def test_prices():
    g = day22.gen_prices(123)
    tp = [3,0,6,5,4,4,6,4,4,2]
    for i in range(10):
        assert next(g) == tp[i]

def test_diffs():
    g = day22.gen_diffs(123)
    td = [-3,6,-1,-1,0,2,-2,0,-2]
    for i in range(9):
        assert next(g) == td[i]

def test_occurrences():
    assert day22.occurrence(1,[-2,1,-1,3]) == 7
    assert day22.occurrence(2,[-2,1,-1,3]) == 7
    assert day22.occurrence(3,[-2,1,-1,3]) is None
    assert day22.occurrence(2024,[-2,1,-1,3]) == 9

    # Test edge case:
    assert day22.occurrence(123,[0,-2],8) is None
    assert day22.occurrence(123,[0,-2],9) == 2
def test_part2():
    secrets = [1,2,3,2024]
    assert day22.part2(secrets) == ((-2,1,-1,3),23)