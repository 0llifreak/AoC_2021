#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- Advent of Code 2021 ---------
#
# Puzzle 4
#
# Author: Olli
# --------------------------------

from aocd.models import Puzzle
import pandas as pd
import numpy as np

# --------------------------------
# Get input data from AoC
# --------------------------------
puzzle = Puzzle(year=2021, day=4)

# --------------------------------
# Solution Part 1
# --------------------------------
input = puzzle.input_data.split("\n")
#print(input)
raw_drawn_numbers = input[0]

drawn_numbers = []
temp_number = ""
for number in raw_drawn_numbers:
    if number == "," and len(temp_number) > 0:
        drawn_numbers.append(temp_number)
        temp_number = ""
    else:
        temp_number += number
drawn_numbers.append(int(temp_number))
#print(drawn_numbers)

raw_bingo_values = input[2:]
bingo_values = []


temp_number = ""
for line in raw_bingo_values:
    #print(line)
    for number in line:
        if number == " " and len(temp_number) > 0:
            bingo_values.append(temp_number)
            temp_number = ""
        else:
            temp_number += number
            #print(temp_number)

    # found no better way than doing this -.-        
    try:
        bingo_values.append(int(temp_number))
    except:
        pass
    temp_number = ""

bingo_cards = np.array(bingo_values)
bingo_cards_count = int(bingo_cards.shape[0] / 25) # calculate number of bingo cards
bingo_cards = np.resize(bingo_cards, (bingo_cards_count, 5, 5)) # generate nx5x5 matrix
#print(bingo_cards)

win = 0
for number in drawn_numbers:
    #print(number)
    if win == 1:
        break

    for bingo_card_index, bingo_card in enumerate(bingo_cards):
        #print(bingo_card_index)
        if win == 1:
            break

        for row_index, row in enumerate(bingo_card):
            if np.all(row == "X"):
                print("row win")
                win = 1
                break

            column = bingo_card[:,row_index]
            if np.all(column == "X"):
                print("column win")
                win = 1
                break

            for column_index, element in enumerate(row):
                if element == number:
                    #print(number)
                    bingo_cards[bingo_card_index, row_index, column_index] = "X"
#print(bingo_cards)
print("Winner")
bingo_card_winner = bingo_cards[bingo_card_index - 1]
number_idx = drawn_numbers.index(number) - 1
print(bingo_card_winner)
number_winner = int(drawn_numbers[number_idx])
print("Winning number", number_winner)

sum = 0
for row in bingo_card_winner:
    for number in row:
        if number != "X":
            sum += int(number)
print("sum", sum)


print("Solution Part 1: ", sum*number_winner)
# 37840 is to low



# --------------------------------
# Solution Part 2
# --------------------------------


#rint("Solution Part 2: ", horizontal*depth)
