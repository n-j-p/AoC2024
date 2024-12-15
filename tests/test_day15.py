import day15

small_input =  ['########',
				'#..O.O.#',
				'##@.O..#',
				'#...O..#',
				'#.#.O..#',
				'#...O..#',
				'#......#',
				'########',
				'',
				'<^^>>>vv<v>>v<<']

small_completed =   '########' + \
					'\n#....OO#' + \
					'\n##.....#' + \
					'\n#.....O#' + \
					'\n#.#O@..#' + \
					'\n#...O..#' + \
					'\n#...O..#' + \
					'\n########'
def test_small_input():

	
	warehouse = day15.Warehouse(*day15.parse_input(small_input))

	#print(warehouse)

	assert warehouse.__repr__() ==    '########' + \
									'\n#..O.O.#' + \
									'\n##@.O..#' + \
									'\n#...O..#' + \
									'\n#.#.O..#' + \
									'\n#...O..#' + \
									'\n#......#' + \
									'\n########'

	print(warehouse)
	while True:
		print()
		try:
			warehouse.update(VERBOSE=True)
		except IndexError:
			break
		print(warehouse)

	assert warehouse.__repr__() == small_completed 

def test_small_input_with_function():
	wh_completed = day15.part1(small_input)
	assert wh_completed.__repr__() == small_completed
	assert wh_completed.calc_gps() == 2028
def test_sample_input():
	sample_input = ['##########',
					'#..O..O.O#',
					'#......O.#',
					'#.OO..O.O#',
					'#..O@..O.#',
					'#O#..O...#',
					'#O..O..O.#',
					'#.OO.O.OO#',
					'#....O...#',
					'##########',
					'',
					'<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^',
					'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v',
					'><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<',
					'<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^',
					'^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><',
					'^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^',
					'>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^',
					'<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>',
					'^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>',
					'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^']
	sample_completed =    '##########' + \
						'\n#.O.O.OOO#' + \
						'\n#........#' + \
						'\n#OO......#' + \
						'\n#OO@.....#' + \
						'\n#O#.....O#' + \
						'\n#O.....OO#' + \
						'\n#O.....OO#' + \
						'\n#OO....OO#' + \
						'\n##########'
	wh_completed = day15.part1(sample_input)
	assert wh_completed.__repr__() == sample_completed

	print(wh_completed.calc_gps())
	assert wh_completed.calc_gps() == 10092