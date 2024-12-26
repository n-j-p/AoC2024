import day24
simple_example = ['x00: 1',
                  'x01: 1',
                  'x02: 1',
                  'y00: 0',
                  'y01: 1',
                  'y02: 0',
                  '',
                  'x00 AND y00 -> z00',
                  'x01 XOR y01 -> z01',
                  'x02 OR y02 -> z02']

def test_simple_example():
    assert day24.part1(simple_example) == 4

def test_read_sample_input():
    sample_input = open('c:/temp/day24_sample.txt')
    ivs, cons = day24.parse_input(sample_input)
    print(ivs, cons)
    assert len(ivs) == 10
    print(cons[0].result)
    print(cons[0].result.__class__)
    assert cons[0].result.strip() == 'mjb' 
    print(cons[-1].result)
    assert cons[-1].result.strip() == 'gnj'
    #assert False
    
def test_sample_input():
    sample_input = open('c:/temp/day24_sample.txt')
    assert day24.part1(sample_input) == 2024
