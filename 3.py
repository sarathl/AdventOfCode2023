import re
import input_reader
from collections import defaultdict
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/3_input.txt')

# Part 1
def is_adjacent_to_symbol(row_id, num_idx):
	start = num_idx[0] if num_idx[0] == 0 else num_idx[0]-1
	end = num_idx[1]+1
	comparison_row = input_clean[row_id][start: end].replace(".", "")
	if len(re.findall("[^0-9]", comparison_row)) > 0:
		return True
	return False

def is_part_number(idx, num_idx):
	if idx == 0:
		if is_adjacent_to_symbol(row_id=idx, num_idx=num_idx):
			return True
		elif is_adjacent_to_symbol(row_id=idx+1, num_idx=num_idx):
			return True
	elif idx == len(input_clean)-1:
		if is_adjacent_to_symbol(row_id=idx, num_idx=num_idx):
			return True
		elif is_adjacent_to_symbol(row_id=idx-1, num_idx=num_idx):
			return True
	else:
		if is_adjacent_to_symbol(row_id=idx, num_idx=num_idx):
			return True
		elif is_adjacent_to_symbol(row_id=idx-1, num_idx=num_idx):
			return True
		elif is_adjacent_to_symbol(row_id=idx+1, num_idx=num_idx):
			return True
	return False


part_numbers_sum = 0
for idx in range(len(input_clean)):
	inpt_line = input_clean[idx]
	for num_match in re.finditer("[0-9]+", inpt_line):
		num = int(num_match.group(0))
		num_idx = num_match.span()
		if is_part_number(idx, num_idx):
			part_numbers_sum += num

print(f"part_numbers_sum is {part_numbers_sum}")

# Part 2

def find_part_nums_given_gear(gear_idx, row_id):
	if row_id == 0:
		ids_to_check = [0, 1]
	elif row_id == len(input_clean)-1:
		ids_to_check == [row_id-1, row_id]
	else:
		ids_to_check = [row_id-1, row_id, row_id+1]

	part_nums = []
	for id_to_check in ids_to_check:
		for num_match in re.finditer("[0-9]+", input_clean[id_to_check]):
			num_span = num_match.span()
			if gear_idx >= num_span[0]-1 and gear_idx <= num_span[1]:
				# the gear index should be between the start and end index of the number
				part_nums.append(int(num_match.group(0)))
	return part_nums

gear_ratio_sum = 0

for idx in range(len(input_clean)):
	inpt_line = input_clean[idx]
	for gear_match in re.finditer("\*", inpt_line):
		gear_idx = gear_match.span()[0]
		part_nums = find_part_nums_given_gear(gear_idx, row_id=idx)
		if len(part_nums) == 2:
			gear_ratio_sum += part_nums[0] * part_nums[1]

print(f"gear_ratio_sum is {gear_ratio_sum}")