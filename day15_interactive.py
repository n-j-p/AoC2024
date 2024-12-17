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

wh = day15.Warehouse(*day15.parse_input(small_input))
wh.interactive()