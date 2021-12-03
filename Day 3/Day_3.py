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

input = puzzle.input_data.split("\n")

def rate_calc(input, gas):
    
    bit_index = 0
    new_list = []

    while len(input) > 1:
        length = len(input)
        bit_sum = 0

        for line in input:
            bit_sum += int(line[bit_index])

        for line in input:
            if gas == "o2":
                if (bit_sum - (length / 2)) < 0:
                    if int(line[bit_index]) == 0:
                        new_list.append(line)
                else:
                    if int(line[bit_index]) == 1:
                        new_list.append(line)

            elif gas == "co2":
                if (bit_sum - (length / 2)) >= 0:
                    if int(line[bit_index]) == 0:
                        new_list.append(line)
                else:
                    if int(line[bit_index]) == 1:
                        new_list.append(line)

        input = new_list.copy()
        new_list.clear()
        bit_index += 1

    return(input)

oxygen_rate = rate_calc(input, "o2")
co2_rate = rate_calc(input, "co2")

# binary to decimal
oxygen_rate_int = int("".join(str(i) for i in oxygen_rate),2)
co2_rate_int = int("".join(str(i) for i in co2_rate),2)

print(oxygen_rate, oxygen_rate_int)
print(co2_rate, co2_rate_int)
print("Solution Part 2: ", oxygen_rate_int*co2_rate_int)
