# LABORATORY 1 - A*
## Some comment related to my A* alghoritm

I've worked with Gregorio Nicora to reach this heuristic function h().
We shifted our attention to the part of the set that still need to be covered. So, at each step, h() compute the number of part that would remain uncovered with the current_set (previous step best_set + one of the not_taken ).

In a first analysis we thought it was a good solution, before we ran into some inconvenience:

1) The first tile taken will influence future choices, even leading to using more tiles than necessary