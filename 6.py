import re
import math
import numpy as np


input_path = 'inputs/6_input.txt'
with open(input_path, 'r') as f:
    input = f.read()


input_clean = [re.search(":(.*)", el).group(1).strip() for el in input.split("\n")]

time_list = [int(el) for el in re.findall("[0-9]+", input_clean[0])]
dist_list = [int(el) for el in re.findall("[0-9]+", input_clean[1])]

# Part 1

prod_num_ways = 1

for time, dist in zip(time_list, dist_list):
	root1 = ((time) + math.sqrt(math.pow(time, 2)-(4*dist)))/(2)
	root2 = ((time) - math.sqrt(math.pow(time, 2)-(4*dist)))/(2)
	print(f"root1 is {root1} and root2 is {root2}")

	# if isinstance(root1, int) and isinstance(root2, int):
	# 	num_ways = np.abs(math.ceil(max(root1, 0)) - math.ceil(max(root2, 0))) - 1
	# else:
	if root1 > root2:
		num_ways = np.abs(math.ceil(max(root1, 0)) - math.floor(max(root2, 0))) -1
	else:
		num_ways = np.abs(math.ceil(max(root2, 0)) - math.floor(max(root1, 0))) -1
	print(f"num_ways is {num_ways}")

	prod_num_ways = prod_num_ways * num_ways

print(f"Product of number of ways to win = {prod_num_ways}")

# Part 2

time = int(input_clean[0].replace(" ", ""))
dist = int(input_clean[1].replace(" ", ""))

root1 = ((time) + math.sqrt(math.pow(time, 2)-(4*dist)))/(2)
root2 = ((time) - math.sqrt(math.pow(time, 2)-(4*dist)))/(2)
print(f"root1 is {root1} and root2 is {root2}")

# if isinstance(root1, int) and isinstance(root2, int):
# 	num_ways = np.abs(math.ceil(max(root1, 0)) - math.ceil(max(root2, 0))) - 1
# else:
if root1 > root2:
	num_ways = np.abs(math.ceil(max(root1, 0)) - math.floor(max(root2, 0))) -1
else:
	num_ways = np.abs(math.ceil(max(root2, 0)) - math.floor(max(root1, 0))) -1

print(f"Product of number of ways to win = {num_ways}")
