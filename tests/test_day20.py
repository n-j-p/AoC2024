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
    # So we can ignore any result that produces a slower time.

    assert race.remove_single_pt((10,8)) == 84 - 2
    assert race.remove_single_pt((2,11)) == 84 - 4
    assert race.remove_single_pt((2,12)) == 84 - 2

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

def test_part2_on_part1_sample():
    # Test whether we get the same distribution of cheat times
    # from part1() function and part2() function
    sample_times = day20.part2(sample_input,2)
    print(sample_times)
    print(day20.part1(sample_input))
    assert sample_times == day20.part1(sample_input)
    

def test_part2_actual():
    # Check whether we get the same actual answer with part2() 
    # and get_part1_answer()
    actual_input = open('c:/temp/day20_input.txt').read().split('\n')[:-1]
    part1_cheats = day20.part2(actual_input, 2)
    c = 0
    for count, time in part1_cheats:
        if time >= 100:
            c += count
    print(c)
    assert day20.get_part1_answer(actual_input, 100) == c
    
def test_part2_sample_answer():

    sample_times = day20.part2(sample_input,20)
    st_50 = set(())
    for count, time in sample_times:
        if time >= 50:
            print(count, time)
            st_50.add((count, time))
    assert st_50 == set(((32, 50),
                         (31, 52),
                         (29, 54),
                         (39, 56),
                         (25, 58),
                         (23, 60),
                         (20, 62),
                         (19, 64),
                         (12, 66),
                         (14, 68),
                         (12, 70),
                         (22, 72),
                         (4, 74),
                         (3, 76)))
