import re
from collections import Counter
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/9_input.txt')

# Part 1

predictions_sum = 0

for input_line in input_clean:
	nums = list(map(lambda el: int(el), input_line.split(" ")))
	print(f"nums is {nums}")
	nums_tree_dict = {}
	idx=1
	nums_tree_dict[idx] = nums

	while len(set(nums)) != 1:
		nums = [nums[idx+1] - nums[idx] for idx in range(len(nums)-1)]
		idx += 1
		nums_tree_dict[idx] = nums

	diff_to_add = nums[1]-nums[0]

	while idx >= 1:
		nums_tree_dict[idx].append(nums_tree_dict[idx][-1] + diff_to_add)
		diff_to_add = nums_tree_dict[idx][-1]
		idx -= 1

	prediction = nums_tree_dict[1][-1]
	predictions_sum += prediction

print(f"Sum of predictions is {predictions_sum}")


# Part 2

predictions_sum_back = 0

for input_line in input_clean:
	nums = list(map(lambda el: int(el), input_line.split(" ")))
	print(f"nums is {nums}")
	nums_tree_dict = {}
	idx=1
	nums_tree_dict[idx] = nums

	while len(set(nums)) != 1:
		nums = [nums[idx+1] - nums[idx] for idx in range(len(nums)-1)]
		idx += 1
		nums_tree_dict[idx] = nums

	diff_to_add = nums[1]-nums[0]

	while idx >= 1:
		nums_tree_dict[idx].insert(0, nums_tree_dict[idx][0] - diff_to_add)
		diff_to_add = nums_tree_dict[idx][0]
		idx -= 1

	prediction = nums_tree_dict[1][0]
	predictions_sum_back += prediction

print(f"Sum of backward predictions is {predictions_sum_back}")
