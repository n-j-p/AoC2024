import day23
sample_input = open('c:/temp/day23_sample.txt').read().split('\n')[:-1]


def test_group_generator():
    assert len(list(day23.group_generator(sample_input))) == 12

def test_part1():
    assert len(list(day23.part1(sample_input))) == 7

def test_part2():
    assert day23.part2(sample_input) == 'co,de,ka,ta'
