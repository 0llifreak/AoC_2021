#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 6
#
# Author: Olli
# --------------------------------

import numpy as np
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=6)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split(",")
input = [int(i) for i in input]

def lanternfish(input):
    for _ in range(80):
        for idx, fischie in enumerate(input):
            if fischie != 0:
                input[idx] -= 1
            else:
                input[idx] = 6
                input.append(9)
    return len(input)

def lanternfish_numpy(input):
    """Slower but with numpy^^"""
    input = np.array(input, dtype=np.int8)
    for _ in range(80):
        for idx in np.where(input == 0)[0]:
            input[idx] = 7
            input = np.append(input, 9)
        input = input - 1
    return len(input)

#solution = lanternfish(input)
#print("Solution Part 1: ", solution)


# --------------------------------
# Solution Part 2
# --------------------------------


input = puzzle.input_data.split(",")
input = [int(i) for i in input]

fisch_day = {0: 0, 1: 0, 2: 0, 3 : 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
lifetime, counts = np.unique(input, return_counts=True)

for idx in lifetime:
    fisch_day[idx] += counts[idx - 1]

for days in range(256):
    count0 = fisch_day[0]
    count6 = fisch_day[6]

    for idx in range(8):
        fisch_day[idx] = fisch_day[idx + 1]

    fisch_day[6] += count0
    fisch_day[8] = count0

solution = []
for x in fisch_day:
    solution.append(fisch_day[x])

print("Solution Part 2: ", sum(solution))
