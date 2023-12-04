import re
import numpy as np
import math
from collections import defaultdict
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/4_input.txt')

# Part 1

def get_nums(inpt_line):
	nums_list = []
	for num in re.finditer("[0-9]+", inpt_line):
		nums_list.append(int(num.group(0)))
	return nums_list

winning_numbers_sum = 0
for idx in range(len(input_clean)):
	inpt_line = input_clean[idx]
	inpt_line = re.search("Card[ \t]+[0-9]+: (.*)", inpt_line).group(1).strip()
	winning_nums = get_nums(inpt_line.split(" | ")[0].strip())
	our_nums = get_nums(inpt_line.split(" | ")[1].strip())
	matches = np.intersect1d(winning_nums, our_nums)
	if len(matches) > 0:
		winning_numbers_sum += int(math.pow(2, len(matches)-1))

print(f"winning_numbers_sum is {winning_numbers_sum}")

# Part 2

num_cards_dict = defaultdict(lambda: 1)

for idx in range(len(input_clean)):
	inpt_line = input_clean[idx]
	card_num = int(re.search("[0-9]+:", inpt_line).group(0)[:-1])
	inpt_line = re.search("Card[ \t]+[0-9]+: (.*)", inpt_line).group(1).strip()
	winning_nums = get_nums(inpt_line.split(" | ")[0].strip())
	our_nums = get_nums(inpt_line.split(" | ")[1].strip())
	matches = np.intersect1d(winning_nums, our_nums)
	for i in range(1, len(matches)+1):
		num_cards_dict[card_num+i] += num_cards_dict[card_num]
	if len(matches) == 0:
		num_cards_dict[card_num] += 0

total_cards = np.sum(list(num_cards_dict.values()))

print(f"total_cards are {total_cards}")
