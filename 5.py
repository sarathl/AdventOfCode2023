import re

input_path = 'inputs/5_input.txt'
with open(input_path, 'r') as f:
    input = f.read()


inpt_wo_labels = [re.search(":((.|\n)*)", el).group(1).strip() for el in input.split("\n\n")]
inpt_clean = [el.split("\n") for el in inpt_wo_labels]

# Default dict with value=key
class MyDict(dict):
   def __init__(self, factory):
       self.factory = factory
   def __missing__(self, key):
       self[key] = self.factory(key)
       return self[key]

# Part 1

original_dict = {}

for seed_str in inpt_clean[0][0].split(" "):
	seed = int(seed_str)
	original_seed = seed
	original_dict[seed] = seed
	for map_index in range(1, 8):
		# print(f"map_index is {map_index}")
		mapping_dict = MyDict(lambda x: x)
		for map_line in inpt_clean[map_index]:
			dest = int(map_line.split(" ")[0])
			source = int(map_line.split(" ")[1])
			s_range = int(map_line.split(" ")[-1])
			if seed >= source and seed < source+s_range:
				mapping_dict[seed] = (seed - source) + dest
				original_dict[original_seed] = (seed - source) + dest
				break
			else:
				mapping_dict[seed] += 0
				original_dict[original_seed] = seed
		seed = mapping_dict[seed]


# print(f"original_dict is {original_dict}")
print(f"lowest location number is {min(list(original_dict.values()))}")


# Part 2

original_dict = {}
seeds_info = inpt_clean[0][0].split(" ")

def get_location():
	for location_og in count():
		# Starting from minimum possible location and returning when there's an appropriate seed number as input for a location
		loc = location_og
		for map_index in range(7, 0, -1):
			# print(f"map_index is {map_index}")
			mapping_dict = MyDict(lambda x: x)
			for map_line in inpt_clean[map_index]:
				dest = int(map_line.split(" ")[0])
				source = int(map_line.split(" ")[1])
				s_range = int(map_line.split(" ")[-1])
				if loc >= dest and loc < dest+s_range:
					mapping_dict[loc] = (loc-dest) + source
			loc = mapping_dict[loc]

		for seed_start_idx in range(0, len(seeds_info), 2):
			seed_start = int(seeds_info[seed_start_idx])
			seed_start_range = int(seeds_info[seed_start_idx+1])
			if loc>= seed_start and loc < (seed_start+seed_start_range):
				return location_og

print(f"lowest location number is {get_location()}")

