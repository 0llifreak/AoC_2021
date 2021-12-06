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

for days in range(80):
    for idx, fischie in enumerate(input):
        if fischie != 0:
            input[idx] -= 1
        else:
            input[idx] = 6
            input.append(9)

print("Solution Part 1: ", len(input))


# --------------------------------
# Solution Part 2
# --------------------------------
input = puzzle.input_data.split("\n")




#print("Solution Part 2: ", )
