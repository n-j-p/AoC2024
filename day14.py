class Robot():
	def __init__(self, init_str):
		self.init_str = init_str
		p,v = init_str.split(' ')
		p=p.replace('p=','')
		v=v.replace('v=','')
		px,py = p.split(',')
		vx,vy = v.split(',')
		px = int(px)
		py = int(py)
		vx = int(vx)
		vy = int(vy)
		self.p0 = (px, py)
		self.v0 = (vx, vy)
		self.p = [px, py]
		self.v = [vx, vy]
	def update(self, r, c):
		self.p = [(self.p[0] + self.v[0]) %	r,
			      (self.p[1] + self.v[1]) % c]


class Space():
	def __init__(self, R = 103, C = 101):
		self.R = R
		self.C = C
		self.robots = []
	def add_robot(self, robot):
		self.robots.append(robot)
	def update(self):
		for robot in self.robots:
			robot.update(self.R, self.C)
	def count(self):
		qNW = [x.p for i,x in enumerate(self.robots) if x.p[0] < self.R//2 and x.p[1] < self.C//2]
		qNE = [x.p for i,x in enumerate(self.robots) if x.p[0] > self.R//2 and x.p[1] < self.C//2]
		qSW = [x.p for i,x in enumerate(self.robots) if x.p[0] < self.R//2 and x.p[1] > self.C//2]
		qSE = [x.p for i,x in enumerate(self.robots) if x.p[0] > self.R//2 and x.p[1] > self.C//2]
		#return (qNW, qNE, qSW, qSE)
		return(len(qNW), len(qNE), len(qSW), len(qSE))
	def calc_av_dist(self):
		import itertools as it
		d = 0
		for xy in it.combinations(self.robots, 2):
			r1, r2 = xy
			d += (r1.p[0]-r2.p[0])**2 + (r1.p[1]-r2.p[1])**2
		return d
	def repr(self):
		repr = [['.' for _ in range(self.R)] for _ in range(self.C)]
		#print(repr)
		xR = 0
		xC = 0
		for robot in self.robots:
			#print(robot.p)
			repr[robot.p[1]][robot.p[0]] = 'X'
			xR = max(xR, robot.p[1])
			xC = max(xC, robot.p[0])
		return repr
	def display(self):
		print('\n'.join([''.join(x) for x in self.repr()]))
		#return [''.join(x) for x in repr]
		#print(repr)
		#print('\n'.join(repr))




sample_input = ['p=0,4 v=3,-3',
				'p=6,3 v=-1,-3',
				'p=10,3 v=-1,2',
				'p=2,0 v=2,-1',
				'p=0,0 v=1,3',
				'p=3,0 v=-2,-2',
				'p=7,6 v=-1,-3',
				'p=3,0 v=-1,-2',
				'p=9,3 v=2,3',
				'p=7,3 v=-1,2',
				'p=2,4 v=2,-3',
				'p=9,5 v=-3,-3']

actual_input = open('c:/temp/day14_input.txt').read().split('\n')[:-1]
#print(actual_input)
def part1(R = 101, C = 103, niters = 100):
	space = Space(R, C)
	for rstr in actual_input:
		space.add_robot(Robot(rstr))
	for i in range(niters):
		space.update()
	#print(space.count())
	def mul(alist):
		p = 1
		for x in alist:
			p *= x
		return p
	print('Part 1 answer is', mul(space.count()))

if __name__ == '__main__':
	part1()
