class input_reader:
	def __init__(self):
		pass

	def return_clean_input(self, input_path):
		with open(input_path, 'r') as f:
		    input = f.read()
		    input_clean = input.split("\n")
		return input_clean
