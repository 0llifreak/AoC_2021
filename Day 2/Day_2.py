#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 2
#
# Author: Olli
# --------------------------------

from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=2)
#print(len(puzzle.input_data.split("\n")))

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split("\n")

horizontal = 0
depth = 0

for line in input:
    command = line.split(" ")
    direction = str(command[0])
    value = int(command[1])

    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value
    
print("Horizontal: ", horizontal)
print("Depth: ", depth)

print("Solution Part 1: ", horizontal*depth)

# --------------------------------
# Solution Part 2
# --------------------------------

horizontal = 0
depth = 0
aim = 0

for line in input:
    command = line.split(" ")
    direction = str(command[0])
    value = int(command[1])

    if direction == "forward":
        horizontal += value
        depth += aim*value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value

print("Horizontal: ", horizontal)
print("Depth: ", depth)

print("Solution Part 2: ", horizontal*depth)
