import day15


def test_get_repr2():
	print('\n'.join(day15.get_repr2(day15.sample_input)))



def test_parse_input2():
	print(day15.parse_input2(day15.sample_input))


def test_Warehouse2_what():
	wh = day15.Warehouse2(*day15.parse_input2(day15.sample_input))
	print(wh.R, wh.C)
	r = 0
	print(wh.box_locs)
	print([wh._what((r,c)) for c in range(wh.C)])
	assert wh._what((0,0)) == '.'
	assert wh._what((0,4)) == '['
	assert wh._what((3,6)) == '@'
	assert wh._what((3,5)) == ']'


def test_Warehouse2_repr():
	wh = day15.Warehouse2(*day15.parse_input2(day15.sample_input))
	print(wh)
	
					
def test_part2_example():
	example =  ['#######',
				'#...#.#',
				'#.....#',
				'#..OO@#',
				'#..O..#',
				'#.....#',
				'#######',
				'',
				'<vv<<^^<<^^']
	wh = day15.Warehouse2(*day15.parse_input2(example))
	print(wh)
	while True:
		print()
		try:
			wh.update(VERBOSE=True)
		except IndexError:
			break
		print(wh)



def test_part2():
	
	wh = day15.Warehouse2(*day15.parse_input2(day15.sample_input))
	print(wh)
	while True:
		print()
		try:
			wh.update(VERBOSE=True)
		except IndexError:
			break
		print(wh)
	print(wh.box_locs)
	print([(x[0]+2, x[1]+1) for x in wh.box_locs])
	assert wh.calc_gps() == 9021



	
def test_part2_function():
	assert day15.part2(day15.sample_input).calc_gps()	 == 9021