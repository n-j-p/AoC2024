import pdb
import time

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
def parse_input(inp):
	map_end = False
	box_locs = []
	wall_locs = []
	robot_loc = None
	move_list = ''
	for i,row in enumerate(inp):
		if i == 0:
			C = len(row) - 2
			continue
		elif map_end and len(row) > 0:
			move_list += row
		elif row == '#'*(C+2):
			#print('end')
			map_end = True
			R = i-1
		else:
			#print(row[1:-1])
			blocs = [i for i,x in enumerate(row[1:-1]) if x == 'O']
			for j in blocs:
				box_locs.append((i-1, j))
			rloc = [i for i,x in enumerate(row[1:-1]) if x == '@']
			if len(rloc) == 1:
				if robot_loc is None:
					robot_loc = (i-1, rloc[0])
				else:
					raise Exception('More than one robot detected')

			wlocs = [i for i,x in enumerate(row[1:-1]) if x == '#']
			for j in wlocs:
				wall_locs.append((i-1, j))

	return box_locs, robot_loc, wall_locs, move_list, R, C

class Warehouse():
	def __init__(self, blocs, rloc, wlocs, move_list, R, C):
		self.box_locs = blocs
		self.robot_loc = rloc
		self.wall_locs = wlocs
		self.move_list = move_list
		self.R = R
		self.C = C

		self.move = 0
	_diff = {'<': (0,-1),
		     '>': (0, 1),
			 '^': (-1,0),
			 'v': ( 1,0)}
	def _what(self, position):
		'''Map lookup function, ! represents a position off the map'''
		if (position[0] < 0 or position[0] >= self.R) or \
		   (position[1] < 0 or position[1] >= self.C):
			return '!'

		elif self.robot_loc == position:
			return '@'
		elif position in self.wall_locs:
			return '#'
		elif position in self.box_locs:
			return 'O'
		else:
			return '.'
	def __repr__(self):

		wh = [[self._what((r,c)) for c in range(self.C)] for r in range(self.R)]

		## Add in exterior walls
		for i in range(len(wh)):
			wh[i].append('#')
			wh[i].insert(0, '#')
		wh.insert(0,['#' for _ in range(self.C+2)])
		wh.append(['#' for _ in range(self.C+2)])
		return '\n'.join([''.join(x) for x in wh])
	def update(self, VERBOSE=False):
		if VERBOSE:
			print(self.move_list[self.move])
		cur_move = self.move_list[self.move]
		self.move += 1
		new_loc = (self.robot_loc[0] + self._diff[cur_move][0],
				   self.robot_loc[1] + self._diff[cur_move][1])
		X = self._what(new_loc)
		if VERBOSE:
			print(new_loc, self._what(new_loc))
		#		pdb.set_trace()

		if X == '!':
			if VERBOSE:
				print("Can't move off map")
			return
		if X == '#': # New position is a wall, do nothing
			if VERBOSE:
				print("Wall in the way")
			return
		elif X == '.': # Nothing in the way, move there
			self.robot_loc = new_loc
		elif X == 'O': # Moving up against a box
			#pdb.set_trace()
			# Look for next available free space
			post_box_loc = (new_loc[0] + self._diff[cur_move][0],
				            new_loc[1] + self._diff[cur_move][1])
			nboxes = 1
			#pdb.set_trace()
			while True:
				if self._what(post_box_loc) == '!':
					if VERBOSE:
						print("Can't push off edge of map")
					return
				if self._what(post_box_loc) == '#':
					if VERBOSE:
						print('Wall in the way')
					return
				if self._what(post_box_loc) == '.':
					if VERBOSE:
						print(f'Empty space! row of {nboxes} detected')
					assert self._what(new_loc) == 'O'
					assert self._what(post_box_loc) == '.'
					self.box_locs.remove(new_loc)
					self.box_locs.append(post_box_loc)
					self.robot_loc = new_loc
					return
				if self._what(post_box_loc) == 'O':
					nboxes += 1
					# Continue on in loop
				post_box_loc = (post_box_loc[0] + self._diff[cur_move][0],
				                post_box_loc[1] + self._diff[cur_move][1])
	def calc_gps(self):
		c = 0
		for bloc in self.box_locs:
			ci = bloc[1] + 1 + 100*(bloc[0] + 1)
			#print(ci)
			c += ci
		return c
	def interactive(self):
		import msvcrt 
		print(self)
		self.move_list = ''
		while True:
			symbol = ''
			key = ord(msvcrt.getch())
			if key == 27:
				return
			if key == 224: #Special keys (arrows, f keys, ins, del, etc.)
				key = ord(msvcrt.getch())
				if key == 80: #Down arrow
					#print('down arrow')
					symbol = 'v'
				elif key == 72: #Up arrow
					#print('up arrow')
					symbol = '^'
				elif key == 77:
					#print('right arrow')
					symbol = '>'
				elif key == 75:
					#print('left arrow')
					symbol = '<'
			
			if len(symbol) > 0:
				self.move_list += symbol
				#print(self.move_list)
				self.update()
				print(self)

def part1(inp, VERBOSE=True):
	warehouse = Warehouse(*parse_input(inp))
	while True:
		if VERBOSE:
			print()
		try:
			warehouse.update(VERBOSE)
		except IndexError:
			break
		
	return warehouse



def get_repr2(inp):
	'''Get repr for part 2 of problem by parsing smaller map input'''
	tmp = Warehouse(*parse_input(inp))
	tmp2 = tmp.__repr__().split('\n')
	input2_rev = []
	for row in tmp2:
		row2_rev = []
		for x in row[::-1]:
			if x == '#':
				row2_rev.append('##')
			elif x == '.':
				row2_rev.append('..')
			elif x == '@':
				row2_rev.append('@.')
			elif x == 'O':
				row2_rev.append('[]')
		input2_rev.append(''.join(row2_rev[::-1]))
	return input2_rev

def parse_input2(inp):
	box_locs = []
	wall_locs = []
	robot_loc = None
	move_list = ''

	repr = get_repr2(inp)
	for i, row in enumerate(repr):
		if i == 0:
			C = len(row) - 4
			continue
		elif row == '#'*(C+4):
			R = i-1
		else:
			for j, x in enumerate(row[2:-2]):
				if x == '[':
					box_locs.append((i-1,j))
				elif x == '#':
					wall_locs.append((i-1,j))
				elif x == '@':
					robot_loc = (i-1,j)

	map_end = False
	for i, row in enumerate(inp):
		if not map_end:
			if len(row) == 0:
				map_end = True
		else:
			move_list += row

	return box_locs, robot_loc, wall_locs, move_list, R, C

class Warehouse2(Warehouse):
	def _what(self, position):
		'''Map lookup function, ! represents a position off the map'''
		if (position[0] < 0 or position[0] >= self.R) or \
		   (position[1] < 0 or position[1] >= self.C):
			return '!'

		elif self.robot_loc == position:
			return '@'
		elif position in self.wall_locs:
			return '#'
		elif position in self.box_locs:
			return '['
		elif (position[0], position[1]-1) in self.box_locs:
			return ']'
		else:
			return '.'
	def _get_neighbour(self, point, direction):
		'''returns neighbouring point in direction'''
		return (point[0] + self._diff[direction][0],
				point[1] + self._diff[direction][1])
	def gn(self, point, directions):
		new_pt = point
		for direction in directions:
			new_pt = self._get_neighbour(new_pt, direction)
		return new_pt
	def __repr__(self):
		repr1 = super().__repr__()
		repr2 = repr1.split('\n')
		repr2 = ['#' + x + '#' for x in repr2]

		return '\n'.join(repr2)
	def update(self, VERBOSE=False):
		if VERBOSE:
			print(self.move_list[self.move])
		cur_move = self.move_list[self.move]
		self.move += 1
		new_loc = self._get_neighbour(self.robot_loc, cur_move)
		X = self._what(new_loc)
		if VERBOSE:
			print(new_loc, self._what(new_loc))

		if X == '!':
			if VERBOSE:
				print("Can't move off map")
			return
		if X == '#': # New position is a wall, do nothing
			if VERBOSE:
				print("Wall in the way")
			return
		else:
			# edges holds a list of the positions on the edge of all boxes being pushed.
			# initially we start with the position in direction of movement of the robot.
			edges = [new_loc,]

			# This holds position of '[' of any boxes being pushed.
			box_stack = []
			if VERBOSE:
				print(new_loc,cur_move, edges)
			
			# Expand edges, checking for boxes (and walls!).
			# If a box is found, update the edges list.
			while sum([self._what(pos)!='.' for pos in edges]) > 0:	# If there is something non-empty in the edges list...
				# There is a wall in the way, can't move, exit
				if sum([self._what(pos) in ['#', '!'] for pos in edges]) > 0:
					return
				if VERBOSE:
					print(edges, [self._what(pos) for pos in edges])
				new_edges = []
				# This for loop expands the edges list...
				for edge in edges[::-1]:
					if cur_move == '>' and self._what(edge) == '[':
						new_edges.append(self.gn(edge, '>>'))
						box_stack.append(edge)
					elif cur_move == '<' and self._what(edge) == ']':
						new_edges.append(self.gn(edge, '<<'))
						box_stack.append(self.gn(edge, '<'))
					elif cur_move == '^':
						if self._what(edge) == '[':
							new_edges.append(self.gn(edge, '^'))
							new_edges.append(self.gn(edge, '^>'))
							box_stack.append(self.gn(edge, ''))
						elif self._what(edge) == ']':
							new_edges.append(self.gn(edge, '^'))
							new_edges.append(self.gn(edge, '^<'))
							box_stack.append(self.gn(edge, '<'))
						else:
							new_edges.append(edge)
					elif cur_move == 'v':
						if self._what(edge) == '[':
							new_edges.append(self.gn(edge, 'v'))
							new_edges.append(self.gn(edge, 'v>'))
							box_stack.append(self.gn(edge, ''))
						elif self._what(edge) == ']':
							new_edges.append(self.gn(edge, 'v'))
							new_edges.append(self.gn(edge, 'v<'))
							box_stack.append(self.gn(edge, '<'))
						else:
							new_edges.append(edge)
				edges = list(new_edges)
				box_stack=list(set(box_stack))
				if VERBOSE:
					print('  ',new_edges, box_stack)
						

			# Done.
			# If we are here, there are no walls in the way.
			# Move any boxes in the box_locs list as well as the robot.
			for box_pos in box_stack:
				self.box_locs.remove(box_pos)
				self.box_locs.append(self.gn(box_pos, cur_move))
			self.robot_loc = new_loc


	def calc_gps(self):
		c = 0
		for bloc in self.box_locs:
			ci = bloc[1] + 2 + 100*(bloc[0] + 1)
			#print(ci)
			c += ci
		return c
	
def part2(inp, VERBOSE=True):
	warehouse = Warehouse2(*parse_input2(inp))
	while True:
		if VERBOSE:
			print()
		try:
			warehouse.update(VERBOSE)
		except IndexError:
			break
		
	return warehouse

if __name__ == '__main__':
	tt = time.time()
	actual_input = open('c:/temp/day15_input.txt').read().split('\n')[:-1]
	wh = part1(actual_input, VERBOSE=False)
	print(f'Part 1 answer is {wh.calc_gps()}. Done in {time.time()-tt:.1f}s')

	tt = time.time()
	wh2 = part2(actual_input, VERBOSE=False)
	print(wh2)
	print(f'Part 2 answer is {wh2.calc_gps()}. Done in {time.time()-tt:.1f}s')


