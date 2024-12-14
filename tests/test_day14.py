import day14

robot0 = day14.Robot('p=2,4 v=2,-3')
print(robot0.p, robot0.v)

test_space = day14.Space(11, 7)

def test_wrap():
	robot1 = day14.Robot('p=2,4 v=2,-3')
	day_positions = [[2,4],
				  [4,1],
				  [6,5],
				  [8,2],
				  [10,6],
				  [1,3]]
	for day, pos in enumerate(day_positions):
		assert robot1.p == day_positions[day]
							
		robot1.update(11, 7)
def test_count():
	sample_space = day14.Space(11, 7)
	for rstr in day14.sample_input:
		sample_space.add_robot(day14.Robot(rstr))
	for i in range(100):
		sample_space.update()
	print(sample_space.count())
	assert sample_space.count() == (1,3,4,1)
sample_space = day14.Space(11, 7)
for rstr in day14.sample_input:
	sample_space.add_robot(day14.Robot(rstr))
print(sample_space.display())