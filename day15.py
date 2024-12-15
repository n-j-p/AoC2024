import pdb
import time

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

if __name__ == '__main__':
	tt = time.time()
	actual_input = open('c:/temp/day15_input.txt').read().split('\n')[:-1]
	wh = part1(actual_input, VERBOSE=False)
	print(f'Part 1 answer is {wh.calc_gps()}. Done in {time.time()-tt:.1f}s')