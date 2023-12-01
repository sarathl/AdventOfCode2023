# Part 1
with open('inputs/1_input.txt', 'r') as f:
    input = f.read()
    input_clean = input.split("\n")

sum = 0
re_str = "[0-9]"

for input_str in input_clean:
    first_int = re.search(re_str, input_str).group(0)
    last_int = re.search(re_str, input_str[::-1]).group(0)
    sum += (10*int(first_int)) + int(last_int)

print(sum)


# Part 2
with open('inputs/1_input.txt', 'r') as f:
    input = f.read()
    input_clean = input.split("\n")

valid_ints = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
valid_ints_reverse = {k[::-1]: v for k, v in valid_ints.items()}

sum = 0
re_str_first = "[0-9]|" + '|'.join(list(valid_ints.keys()))
re_str_last = "[0-9]|" + '|'.join(list(valid_ints_reverse.keys()))

print(re_str)

for input_str in input_clean:
    first_int = re.search(re_str_first, input_str).group(0)
    last_int = re.search(re_str_last, input_str[::-1]).group(0)
    sum += 10*(int(valid_ints.get(first_int, first_int))) + int(valid_ints_reverse.get(last_int, last_int))

print(sum)
