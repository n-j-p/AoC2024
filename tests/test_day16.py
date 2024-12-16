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
    print('Sample part 1 answer is',sample_part1_answer)
    assert sample_part1_answer == 7036

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
    print('Second test part 1 answer is',second_part1_answer)
    assert second_part1_answer == 11048
