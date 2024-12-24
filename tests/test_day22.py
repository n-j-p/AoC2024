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