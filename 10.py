import re
import numpy as np
import time
from collections import Counter
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/10_input_test.txt')


def is_valid_route(destination, direction):
	if direction.upper() in pipe_directions.get(destination, []):
		return True
	return False

def is_valid_row_col(row_idx, col_idx):
	if (row_idx>=0 and row_idx < len(distance_matrix)) and (col_idx >= 0 and col_idx < len(distance_matrix[0])):
		return True
	return False


def fill_distance_matrix(row_idx, col_idx, distance_matrix):
	print(f"processing {row_idx}-{col_idx}-{input_clean[row_idx][col_idx]}-")
	print(distance_matrix[row_idx])

	rid = row_idx
	cid = col_idx-1
	if is_valid_row_col(rid, cid):
		route = f"{row_idx}-{col_idx}_{rid}-{cid}"
		if (distance_matrix[rid][cid] == -1) and route not in visited_routes:
			destination = input_clean[rid][cid]
			if is_valid_route(destination, direction='E'):
				distance_matrix[rid][cid] = distance_matrix[row_idx][col_idx] + 1
				distance_matrix = fill_distance_matrix(rid, cid, distance_matrix)
			elif destination == ".":
				distance_matrix[rid][cid] = -2
			visited_routes.append(route)

	rid = row_idx-1
	cid = col_idx
	if is_valid_row_col(rid, cid):
		route = f"{row_idx}-{col_idx}_{rid}-{cid}"
		if (distance_matrix[rid][cid] == -1) and route not in visited_routes:
			destination = input_clean[rid][cid]
			# print(f"destination is {destination}")
			if is_valid_route(destination, direction='S'):
				distance_matrix[rid][cid] = distance_matrix[row_idx][col_idx] + 1
				distance_matrix = fill_distance_matrix(rid, cid, distance_matrix)
			elif destination == ".":
				distance_matrix[rid][cid] = -2
			visited_routes.append(route)


	rid = row_idx
	cid = col_idx+1
	if is_valid_row_col(rid, cid):
		route = f"{row_idx}-{col_idx}_{rid}-{cid}"
		if (distance_matrix[rid][cid] == -1) and route not in visited_routes:
			destination = input_clean[rid][cid]
			if is_valid_route(destination, direction='W'):
				distance_matrix[rid][cid] = distance_matrix[row_idx][col_idx] + 1
				distance_matrix = fill_distance_matrix(rid, cid, distance_matrix)
			elif destination == ".":
				distance_matrix[rid][cid] = -2
			visited_routes.append(route)

	# print(f"distance_matrix is {distance_matrix}")
	# time.sleep(1000)

	rid = row_idx+1
	cid = col_idx
	if is_valid_row_col(rid, cid):
		route = f"{row_idx}-{col_idx}_{rid}-{cid}"
		if (distance_matrix[rid][cid] == -1) and route not in visited_routes:
			destination = input_clean[rid][cid]
			if is_valid_route(destination, direction='N'):
				distance_matrix[rid][cid] = distance_matrix[row_idx][col_idx] + 1
				distance_matrix = fill_distance_matrix(rid, cid, distance_matrix)
			elif destination == ".":
				distance_matrix[rid][cid] = -2
			visited_routes.append(route)

	return distance_matrix


# print(f"input_clean is {input_clean}")

for row_idx in range(len(input_clean)):
	try:
		input_line = input_clean[row_idx]
		starting_col = re.search('S', input_line).span()[0]
		starting_row = row_idx
		break
	except:
		pass


distance_matrix = [[-1 for l in range(len(input_clean[0]))] for b in range(len(input_clean))]
# input_clean[starting_row] = input_clean[starting_row].replace('S', 'L')
distance_matrix[starting_row][starting_col] = 0

visited_routes = []

pipe_directions = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['N', 'E'], 'J': ['N', 'W'], '7': ['S', 'W'], 'F': ['S', 'E']}

# for row_idx, col_idx in zip([[starting_row, starting_col], [starting_row-1, starting_col], [starting_row+1, starting_col], [starting_row, starting_col]]):
# 	distance_matrix = fill_distance_matrix(row_idx, col_idx, distance_matrix)

distance_matrix = fill_distance_matrix(starting_row, starting_col, distance_matrix)

print(f"Final distance_matrix is {distance_matrix}")

print(f"Max distance is {(np.amax(distance_matrix)//2) +1}")

