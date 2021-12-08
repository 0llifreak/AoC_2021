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

for pos in range(max(input)):
    cost_list.append(sum(abs(input_np - pos))) 

solution = min(cost_list)
print("Solution Part 1: ", min(cost_list))


# --------------------------------
# Solution Part 2
# --------------------------------
input = puzzle.input_data.split(",")
input = [int(i) for i in input]

input_np = np.array(input)
cost_list = []

for pos in range(max(input)):
    # use gauß sum: https://www.wikiwand.com/de/Gau%C3%9Fsche_Summenformel
    n = np.array(abs(input_np - pos) + 1) # add + 1 because gauß sum starts at 0
    gauß_sum = n*(n - 1) // 2 # calculate gauß sum: 1+2+3+...+n = n(n+1)/2
    cost_list.append(sum(gauß_sum)) 

solution = min(cost_list)
print("Solution Part 2: ", solution)
