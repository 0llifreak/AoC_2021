#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 1
#
# Author: Olli
# --------------------------------
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=1)

# --------------------------------
# Solution Part 1
# --------------------------------
numbers = puzzle.input_data.split("\n") # convert string to list

num_prev = 0
count = 0

for number in numbers:
    if num_prev == 0:
        num_prev = number # don't compare first number
    elif int(number) > int(num_prev):
        count += 1
    num_prev = number

print("Solution Part 1: ", count)


# --------------------------------
# Solution Part 2
# --------------------------------
count = 0
length = len(numbers)
for index in range(length):
    if index == length - 3:
        break # exit the loop, if window2 ist at the end of the list
    window1 = int(numbers[index]) + int(numbers[index+1]) + int(numbers[index+2])
    window2 = int(numbers[index+1]) + int(numbers[index+2]) + int(numbers[index+3])
    if window2 > window1:
        count += 1

print("Solution Part 2: ", count)