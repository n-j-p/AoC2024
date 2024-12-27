# AoC2024


```
   ___     __              __         ___  _____        __   
  / _ |___/ /  _____ ___  / /_  ___  / _/ / ___/__  ___/ /__ 
 / __ / _  / |/ / -_) _ \/ __/ / _ \/ _/ / /__/ _ \/ _  / -_)
/_/ |_\_,_/|___/\__/_//_/\__/  \___/_/   \___/\___/\_,_/\__/ 
                                                             
```
* ASCII letters courtesy of patorjk.com/software/taag/

**Every time I think I worked out how the numbers on the Stats page relate to the numbers on the personal times page, turns out I was wrong again.**

Day 6 part 2 was the first puzzle where the answer wasn't instantaneously solvable with the right algo. I had some troubles with the python negative index pitfall.

TIL: Using python classes takes more time up-front but is easier when it's time to swap the actual input for the sample input. 

Day 9 (defragmentation), part 2 was the hardest so far (for me). I came up with the method just after finishing part 1, which was updating a rle representation (including concatentation of consecutive dot representation). However, I got stuck on debugging the indices and lengths, but finally got there.

Day 12 onwards I've started using pytest to organise testing of each day's code

Day 15, part 2: Complete. day15_part2_interactive.py provides an interactive version of the problem!

Day 17: I really have no idea how to approach part 2.

Day 18: no testing, and brute force for part 2 :-O

I got 42* by the end of the timed competition (+24 hours after last puzzle release).

Day 23: I feel like I cheated by using networkx to calculate this. I don't know the graph algorithms to generate the solutions by hand.