import re
import math
import numpy as np
import input_reader
input_reader_obj = input_reader.input_reader()

input_clean = input_reader_obj.return_clean_input('inputs/11_input.txt')

image_matrix = np.array([[el for el in row] for row in input_clean])


def get_empty_rows_cols(image_matrix, axis):
	ret_list = []
	if axis==0:
		length = image_matrix.shape[0]
	else:
		length = image_matrix.shape[1]
	idx = 0
	while idx < length:
		if axis==0:
			search_arr = image_matrix[idx]
		else:
			search_arr = image_matrix[:, idx]
		if '#' not in search_arr:
			ret_list.append(idx)
		idx += 1
	return ret_list


# Inserting extra rows and columns
empty_rows = get_empty_rows_cols(image_matrix, 0)
empty_cols = get_empty_rows_cols(image_matrix, 1)


def get_galaxies(image_matrix):
	positions_of_galaxies = []
	for idx in range(image_matrix.shape[0]):
		for col_pos in np.where(image_matrix[idx] == '#')[0]:
			positions_of_galaxies.append((idx, col_pos))

	return positions_of_galaxies


positions_of_galaxies = get_galaxies(image_matrix)


def get_answer(multiplier):
	pair_dist_sum = 0
	for id1 in range(len(positions_of_galaxies)):
		for id2 in range(id1, len(positions_of_galaxies)):
			intersect_rows = []
			for er in empty_rows:
				if (er < max(positions_of_galaxies[id2][0], positions_of_galaxies[id1][0])) and (er > min(positions_of_galaxies[id2][0], positions_of_galaxies[id1][0])):
					intersect_rows.append(er)
			intersect_cols = []
			for ec in empty_cols:
				if (ec < max(positions_of_galaxies[id2][1], positions_of_galaxies[id1][1])) and (ec > min(positions_of_galaxies[id2][1], positions_of_galaxies[id1][1])):
					intersect_cols.append(ec)
			dist = np.abs(positions_of_galaxies[id2][0] - positions_of_galaxies[id1][0]) + np.abs(positions_of_galaxies[id2][1] - positions_of_galaxies[id1][1]) + ((len(intersect_rows) + len(intersect_cols))*multiplier) - (len(intersect_rows) + len(intersect_cols))
			# print(f"dist is {dist}")
			pair_dist_sum += dist
	return pair_dist_sum

# Part 1
print(f"Sum of pair lengths is {get_answer(2)}")


# Part 2
print(f"Sum of pair lengths is {get_answer(1000000)}")

