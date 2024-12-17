import day15

actual_input = open('c:/temp/day15_input.txt').read().split('\n')[:-1]

#wh = day15.Warehouse2(*day15.parse_input2(day15.sample_input))
wh = day15.Warehouse2(*day15.parse_input2(actual_input))
wh.interactive()