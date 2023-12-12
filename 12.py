import re
import math
import numpy as np
from functools import lru_cache
import input_reader
input_reader_obj = input_reader.input_reader()

spring_clue_list = input_reader_obj.return_clean_input('inputs/12_input_test.txt')


'???.### 1,1,3'
@lru_cache
def get_num_arrangements(springs, clues, curr_run=0):
	# print(f"springs is {springs}")
	# print(f"clues is {clues}")

	if springs == "":
		# print(f"SPRINGS EMPTY, clues is {clues}, curr_run is {curr_run}")
		if (len(clues) == 1 and curr_run == int(clues)) or (len(clues) == 0 and curr_run == 0):
			return 1
		return 0
	spring = springs[0]
	springs = springs[1:]

	if spring == "?":
		return get_num_arrangements('#'+springs, clues, curr_run) + get_num_arrangements('.'+springs, clues, curr_run)
	elif spring == "#":
		curr_clue_match = int(clues.split(",")[0])
		if curr_run > curr_clue_match:
			return 0
		else:
			return get_num_arrangements(springs, clues, curr_run+1)
	elif spring == ".":
		# print(f"INSIDE DOT, {curr_run}.")
		if curr_run == 0:
			return get_num_arrangements(springs, clues, 0)
		curr_clue_match = int(clues.split(",")[0])
		# print(f"INSIDE DOT, {curr_run}, {curr_clue_match}")
		if curr_run == curr_clue_match:
			# print("MATCHED")
			curr_run = 0
			clues = clues.split(",", 1)[-1]
			# print(f"clues is {clues}")
			return get_num_arrangements(springs, clues, curr_run)
		return 0


num_arrangements = 0
for spring_clue in spring_clue_list:
	springs = spring_clue.split(" ")[0]
	print(f"springs is {springs}")
	clues = spring_clue.split(" ")[1]
	arrangements = get_num_arrangements(springs, clues)
	print(f"arrangements is {arrangements}")
	num_arrangements += arrangements
	# break


print(f"num_arrangements is {num_arrangements}")