import day12
import pytest


sample_input = ['RRRRIICCFF',
                'RRRRIICCCF',
                'VVRRRCCFFF',
                'VVRCCCJFFF',
                'VVVVCJJCFE',
                'VVIVCCJJEE',
                'VVIIICJJEE',
                'MIIIIIJJEE',
                'MIIISIJEEE',
                'MMMISSJEEE']


test_input = ['AAAA',
              'ABAA',
              'AAAC',
              'ACCC']
#print(traverse(test_input,(0,0)))
#print('\n'*5)
#print(get_partition(test_input))

def test_part1_test_input():
    assert day12.part1(test_input) == 264

def test_part1_sample_input():
    p1_sample = day12.part1(sample_input)
    print(f'Part 1 sample answer is {p1_sample}')
    assert p1_sample == 1930

## Part 2

# Let's test this on the following holey region:
test_pts0 = ((0,0),(0,1),(0,2),\
             (1,0),      (1,2),(1,3),(1,4),\
             (2,0),(2,1),(2,2),(2,3),(2,4))
# This has 12 edges (including internal)
shifted_test_pts = [(x[0]+2,x[1]+2) for x in test_pts0]
#print(draw_partition(shifted_test_pts,'A',6,8))
#print()
# work out all points exactly one square adjacent to the region:
#print(draw_partition(calc_border(shifted_test_pts),'X',6,8))


test_pts2 = list(shifted_test_pts)
test_pts2.remove((3,4))
test_suite = [
    [(2,2),(2,3),(2,4),(2,5),
     (3,2),(3,3),(3,4),(3,5),
     (4,2),(4,3),(4,4),(4,5),
     (5,2),(5,3),(5,4),(5,5)],
    [(2,2),(2,3),(2,4),(2,5),
     (3,2),            (3,5),
     (4,2),            (4,5),
     (5,2),(5,3),(5,4),(5,5)],
     shifted_test_pts,
     test_pts2,
     [(1,1),(1,2),(1,3),
      (2,1),      (2,3),
      (3,1),      (3,3),      
      (4,1),(4,2),
      (5,1),      (5,3),
      (6,1),(6,2),(6,3)],
    [(1,1),(1,2),(1,3),(1,4),
      (2,1),           (2,4),
      (3,1),           (3,4),      
      (4,1),(4,2),(4,3),
      (5,1),           (5,4),      
      (6,1),           (6,4),
      (7,1),(7,2),(7,3),(7,4)]

    ]

test_pts2 = list(shifted_test_pts)
test_pts2.remove((3,4))
test_suite = [
    [(2,2),(2,3),(2,4),(2,5),
     (3,2),(3,3),(3,4),(3,5),
     (4,2),(4,3),(4,4),(4,5),
     (5,2),(5,3),(5,4),(5,5)],
    [(2,2),(2,3),(2,4),(2,5),
     (3,2),            (3,5),
     (4,2),            (4,5),
     (5,2),(5,3),(5,4),(5,5)],
     shifted_test_pts,
     test_pts2,
     [(1,1),(1,2),(1,3),
      (2,1),      (2,3),
      (3,1),      (3,3),      
      (4,1),(4,2),
      (5,1),      (5,3),
      (6,1),(6,2),(6,3)],
    [(1,1),(1,2),(1,3),(1,4),
      (2,1),           (2,4),
      (3,1),           (3,4),      
      (4,1),(4,2),(4,3),
      (5,1),           (5,4),      
      (6,1),           (6,4),
      (7,1),(7,2),(7,3),(7,4)]

]
def test_calc_edges_testsuite():
    print('Test 1, 4 edges:')
    print(day12.draw_partition(test_suite[0],'A',10,10))
    assert day12.calc_edges(test_suite[0])[1] == 4
    print('Test 2, 8 edges:')
    print(day12.draw_partition(test_suite[1],'B', 10,10))
    assert day12.calc_edges(test_suite[1])[1] == 8
    print('Test 3, 16 edges:')
    print(day12.draw_partition(test_suite[4], 'C', 10, 10))
    assert day12.calc_edges(test_suite[4])[1] == 16
    print('Test 4, also 16 edges:')

    print(day12.draw_partition(test_suite[5], 'D', 10,10))
    assert day12.calc_edges(test_suite[5])[1] == 16
