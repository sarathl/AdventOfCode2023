import re
import input_reader
from collections import defaultdict
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/2_input.txt')

# Part 1

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

def isCombinationPossible(combination):
	for color_info in combination.split(', '):
		num = int(color_info.split(' ')[0])
		color = color_info.split(' ')[-1].lower()
		if max_cubes.get(color, 0) < num:
			return False
	return True


possible_game_ids_sum = 0
for input_str in input_clean:
	is_possible = True
	cubes_info = re.search("Game [0-9]+: (.*)", input_str).group(1)
	for cube_info in cubes_info.split('; '):
		if not isCombinationPossible(cube_info):
			is_possible = False
			break
	if is_possible:
		game_num = int(re.search("Game [0-9]+", input_str).group(0).split(" ")[-1])
		possible_game_ids_sum += game_num

print(f"possible_game_ids_sum is {possible_game_ids_sum}")

# Part 2

power_sum = 0
for input_str in input_clean:
	is_possible = True
	cubes_info = re.search("Game [0-9]+: (.*)", input_str).group(1)
	req_cubes = defaultdict(int)
	for cube_info in cubes_info.split('; '):
		for color_info in cube_info.split(', '):
			num = int(color_info.split(' ')[0])
			color = color_info.split(' ')[-1].lower()
			req_cubes[color] = max(req_cubes[color], num)
	power = 1
	for req_cube_num in req_cubes.values():
		power = power * req_cube_num
	power_sum += power

print(f"power_sum is {power_sum}")
