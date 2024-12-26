import day25
import itertools as it
def test_pin_encoding():
    sample_input = open('c:/temp/day25_sample.txt').read().split('\n')
    schematics = day25.read_input(sample_input)
    print(schematics[0])
    assert schematics[0].encode() == [0,5,3,4,3]
    print(schematics[2])
    assert schematics[2].encode() == [5,0,2,1,3]
def test_sample_input():
    sample_input = open('c:/temp/day25_sample.txt').read().split('\n')
    schematics = day25.read_input(sample_input)
    c = 0
    for xy in it.combinations(schematics, 2):
        x,y = xy
        try:
            OK = x.fits(y)
            if OK:
                c += 1
        except ValueError:
            continue
    assert c == 3