import re
import math
import numpy as np
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/8_input.txt')

directions = input_clean[0]

def parse_instructions(instr):
    starting_point = re.search("(.*) =", instr).group(1)
    directions = re.search("= (.*)", instr).group(1)
    d = {starting_point: {}}
    d[starting_point]['L'] = re.search("\((.*),", directions).group(1)
    d[starting_point]['R'] = re.search(", (.*)\)", directions).group(1)

    return d

directions_dict = {}
for instr in input_clean[2:]:
    # print(f"instr is {instr}")
    directions_dict = {**directions_dict, **parse_instructions(instr)}

# starting_data = input_clean[2]
# curr_loc = list(parse_instructions(starting_data).keys())[0]
curr_loc = 'AAA'
steps = 0
while curr_loc != 'ZZZ':
    for direction in directions:
        # print(f"curr_loc is {curr_loc}")
        curr_loc = directions_dict[curr_loc][direction]
        steps += 1

print(f"Steps = {steps}")


# Part 2

def lcm(vals):
    from math import gcd
    lcm = 1
    for i in vals:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

all_starting_keys = [k for k in directions_dict.keys() if k.endswith("A")]
steps_list = []
for starting_point in all_starting_keys:
    print(f"starting_point is {starting_point}")
    curr_loc = starting_point
    steps = 0
    while not curr_loc.endswith('Z'):
        for direction in directions:
            # print(f"curr_loc is {curr_loc}")
            curr_loc = directions_dict[curr_loc][direction]
            steps += 1
    steps_list.append(steps)

print(f"Steps taken by all starting points = {steps_list}")

print(f"Total steps for all starting points ending up at **Z = {lcm(steps_list)}")
