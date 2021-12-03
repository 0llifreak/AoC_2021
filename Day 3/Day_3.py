#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 3
#
# Author: Olli
# --------------------------------

from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=3)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split("\n")

length = len(input)
line_length = len(input[0])

final_bit = [0] * line_length
gamma_rate = [None] * line_length
epsilon_rate = [None] * line_length

for line in input:
    line = [int(i) for i in line] # cast all elements to integers

    for index, value in enumerate(line):
        final_bit[index] += value # add each bit to final_bit list

for index, bit in enumerate(final_bit):
    if bit - length // 2 > 0: # check if there are more 1 than 0
        gamma_rate[index] = 1
        epsilon_rate[index] = 0
    else: 
        gamma_rate[index] = 0
        epsilon_rate[index] = 1

# binary to decimal
gamma_rate_int = int("".join(str(i) for i in gamma_rate),2)
epsilon_rate_int = int("".join(str(i) for i in epsilon_rate),2)

print(gamma_rate, gamma_rate_int)
print(epsilon_rate, epsilon_rate_int)
print("Solution Part 1: ", epsilon_rate_int*gamma_rate_int)

# --------------------------------
# Solution Part 2
# --------------------------------


#print("Solution Part 2: ", solution)
