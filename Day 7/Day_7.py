#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 7
#
# Author: Olli
# --------------------------------

from aocd.models import Puzzle
import numpy as np

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=7)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split(",")
input = [int(i) for i in input]

input_np = np.array(input)
cost_list = []

unique_input = set(input) # nice way to remove duplicate values ;-)

for pos in unique_input:
    cost_list.append(sum(abs(input_np - pos))) 

solution = min(cost_list)
print("Solution Part 1: ", solution)


# --------------------------------
# Solution Part 2
# --------------------------------
input = puzzle.input_data.split(",")
input = [int(i) for i in input]


solution = 0
print("Solution Part 2: ", solution)
