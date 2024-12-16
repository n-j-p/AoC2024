import day16

#                012345678901234
sample_input = ['###############',
                '#.......#....E#',
                '#.#.###.#.###.#',
                '#.....#.#...#.#',
                '#.###.#####.#.#',
                '#.#.#.......#.#',
                '#.#.#####.###.#',
                '#...........#.#',
                '###.#.#####.#.#',
                '#...#.....#.#.#',
                '#.#.#.###.#.#.#',
                '#.....#...#.#.#',
                '#.###.#.#.#.#.#',
                '#S..#.....#...#',
                '###############']

def test_sample_input():
    maze = day16.Maze(sample_input)

    #print(maze._what((1,13)))
    #print(maze.locate_start())

    sample_part1_answer = maze.traverse()
    print('Sample part 1 answer is',sample_part1_answer[0])
    assert sample_part1_answer[0] == 7036

second_input = ['#################',
                '#...#...#...#..E#',
                '#.#.#.#.#.#.#.#.#',
                '#.#.#.#...#...#.#',
                '#.#.#.#.###.#.#.#',
                '#...#.#.#.....#.#',
                '#.#.#.#.#.#####.#',
                '#.#...#.#.#.....#',
                '#.#.#####.#.###.#',
                '#.#.#.......#...#',
                '#.#.###.#####.###',
                '#.#.#...#.....#.#',
                '#.#.#.#####.###.#',
                '#.#.#.........#.#',
                '#.#.#.#########.#',
                '#S#.............#',
                '#################']

def test_second_input():
    maze = day16.Maze(second_input)

    second_part1_answer = maze.traverse()
    print('Second test part 1 answer is',second_part1_answer[0])
    assert second_part1_answer[0] == 11048

def test_sample_part2():
    maze = day16.Maze(sample_input)

    sample_part1_answer = maze.traverse()
    #print(sample_part1_answer[1])
    all_paths = sample_part1_answer[1]
    all_ops = [x.ops for x in all_paths]
    all_tiles = [[x.position for x in ops] for ops in all_ops]
    unique_tiles = set(())
    for tiles in all_tiles:
        unique_tiles.update(tiles)
    assert len(unique_tiles) == 45


def test_part2_function():
    sample_part2_answer = day16.part2(sample_input)
    assert sample_part2_answer == 45

def test_part2_second_input():
    second_part2_answer = day16.part2(second_input)
    assert second_part2_answer == 64
