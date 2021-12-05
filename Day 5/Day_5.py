#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 5
#
# Author: Olli
# --------------------------------

import numpy as np
from aocd.models import Puzzle

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=5)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split("\n")

coordinates = []
coord_pair = []

for element in input:
    element = element.split(" -> ")
    for point in element:
        point = point.split(",")
        coord_pair.append((int(point[0]), int(point[1])))
        if len(coord_pair) == 2:
            coordinates.append(coord_pair.copy())
            coord_pair.clear()

zeors_array = np.zeros((1000, 1000), dtype=np.int8)

for pair in coordinates:
    if pair[0][0] == pair[1][0]:
        for y in range(abs(pair[0][1]-pair[1][1]) + 1):
            zeors_array[pair[0][0]][min(pair[0][1], pair[1][1]) + y] += 1

    elif pair[0][1] == pair[1][1]:
        for x in range(abs(pair[0][0]-pair[1][0]) + 1):
            zeors_array[min(pair[0][0], pair[1][0]) + x][pair[0][1]] += 1

overlapping_count = np.count_nonzero(zeors_array >= 2)
print("Solution Part 1: ", overlapping_count)


# --------------------------------
# Solution Part 2
# --------------------------------

input = puzzle.input_data.split("\n")

coordinates = []
coord_pair = []

for element in input:
    element = element.split(" -> ")
    for point in element:
        point = point.split(",")
        coord_pair.append((int(point[0]), int(point[1])))
        if len(coord_pair) == 2:
            coordinates.append(coord_pair.copy())
            coord_pair.clear()

zeors_array = np.zeros((1000, 1000), dtype=np.int8)

for pair in coordinates:
    if pair[0][0] == pair[1][0]:
        for y in range(abs(pair[0][1]-pair[1][1]) + 1):
            zeors_array[pair[0][0]][min(pair[0][1], pair[1][1]) + y] += 1

    elif pair[0][1] == pair[1][1]:
        for x in range(abs(pair[0][0]-pair[1][0]) + 1):
            zeors_array[min(pair[0][0], pair[1][0]) + x][pair[0][1]] += 1
    # diagonal lines
    else:
        if pair[0][0] < pair[1][0] and pair[0][1] < pair[1][1]:
            diff = min(pair[1][0]-pair[0][0], pair[1][1] - pair[0][1]) + 1
            for step in range(diff):
                zeors_array[pair[0][0] + step][pair[0][1] + step] += 1
        else:
            diff = min(pair[0][0]-pair[1][0], pair[0][1] - pair[1][1]) + 1
            for step in range(diff):
                zeors_array[pair[0][0] - step][pair[0][1] - step] += 1

        if pair[0][0] > pair[1][0] and pair[0][1] < pair[1][1]:
            diff = min(pair[0][0]-pair[1][0], pair[1][1] - pair[0][1]) + 1
            for step in range(diff):

                zeors_array[pair[0][0] - step][pair[0][1] + step] += 1
        elif pair[0][0] < pair[1][0] and pair[0][1] > pair[1][1]:
            diff = min(pair[1][0]-pair[0][0], pair[0][1] - pair[1][1]) + 1
            for step in range(diff):
                zeors_array[pair[0][0] + step][pair[0][1] - step] += 1

overlapping_count = np.count_nonzero(zeors_array >= 2)
print("Solution Part 2: ", overlapping_count)
