import day20

sample_input = open('c:/temp/day20_sample_input.txt').read().split('\n')

race = day20.Race(sample_input)
race.traverse_both()

def test_page_examples():
    # Test examples on page:
    assert race.remove_single_pt((1,8)) == 84 - 12
    assert race.remove_single_pt((7,10)) == 84 - 20
    assert race.remove_single_pt((8,8)) == 84 - 38
    assert race.remove_single_pt((7,6)) == 84 - 64

def test_other_examples():
    import numpy as np
    sample_input = open('c:/temp/day20_sample_input.txt').read().split('\n')

    race = day20.Race(sample_input)
    race.traverse_both()
    # Removing a non-connected wall does nothing:
    assert race.remove_single_pt((5,5)) == np.inf

    # This should do nothing:
    # The way it is set up it just adds two to the fastest time.
    assert race.remove_single_pt((6,10)) > 84
    #print(race.remove_single_pt((6,10)))

    assert race.remove_single_pt((10,8)) == 84 - 2

    assert race.remove_single_pt((2,11)) == 84 - 4
    # This is not equivalent to:
    #assert race.remove_two_pts(((2,11),(2,12))) == 84 - 4
    # due to the extra step added (it is assumed that
    # we step on both squares removed).
    assert race.remove_single_pt((2,12)) == 84 - 2
    # However, due to the description that
    # "cheats are uniquely identified by their start position and end position."
    # We should be able to disregard this one?
    # Namely, if a double removal doesn't result in a faster cheat than
    # both single removals, we won't include it.

def test_part1():
    print('Part 1 savings:')
    res = day20.part1(sample_input)
    assert res == set(((14,2),
                      (14,4),
                      (2,6),
                      (4,8),
                      (2,10),
                      (3,12),
                      (1,20),
                      (1,36),
                      (1,38),
                      (1,40),
                      (1,64)))
    
def test_part1_answer():
    assert day20.get_part1_answer(sample_input, 0) == 44