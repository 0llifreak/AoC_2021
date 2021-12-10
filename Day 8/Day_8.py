#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 8
#
# Author: Olli
# --------------------------------

from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=8)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.splitlines()

input_filtered = []

for line in input:
    input_filtered.append(line.split(" | "))
# [[vorne, hinten],[vorne, hinten], ...]
#   ------1------   ------2------

# Count all of length 2,3,4 and 7
counter = 0
for line in input_filtered:
    for digit in line[1].split():   # digits im hinteren Teil als array
        if len(digit) >= 2 and len(digit) <= 4 or len(digit) == 7:
            counter += 1

print("Solution Part 1: ", counter)



# --------------------------------
# Solution Part 2
# --------------------------------
input = puzzle.input_data.split(",")
#input = [int(i) for i in input]


solution = 0
print("Solution Part 2: ", solution)
