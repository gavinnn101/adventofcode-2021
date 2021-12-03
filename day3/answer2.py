def get_oxygen_rate(sequence_list:list, index:int) -> list:
	zero_list = []
	one_list = []

	print('-------------------------')
	print(f'Oxygen function using list: {sequence_list}')
	print(f'Index: {index}')

	if len(sequence_list) == 1:
		return sequence_list

	for sequence in sequence_list:
		val = sequence[index]
		if val == '0':
			zero_list.append(sequence)
		elif val == '1':
			one_list.append(sequence)
	if len(zero_list) > len(one_list):
		print(f'Returning Zero List: {zero_list}')
		return zero_list
	elif len(one_list) > len(zero_list):
		print(f'Returning One List: {one_list}')
		return one_list
	elif len(one_list) == len(zero_list):
		# Return the one list if the lists are even per instructions
		return one_list


def get_scrubber_rate(sequence_list:list, index:int) -> list:
	zero_list = []
	one_list = []

	print('-------------------------')
	print(f'Scrubber function using list: {sequence_list}')
	print(f'Index: {index}')

	if len(sequence_list) == 1:
		return sequence_list

	for sequence in sequence_list:
		val = sequence[index]
		if val == '0':
			zero_list.append(sequence)
		elif val == '1':
			one_list.append(sequence)
	if len(zero_list) < len(one_list):
		print(f'Returning Zero List: {zero_list}')
		return zero_list
	elif len(one_list) < len(zero_list):
		print(f'Returning One List: {one_list}')
		return one_list
	elif len(one_list) == len(zero_list):
		# Return the zero list if the lists are even per instructions
		return zero_list


def main():
	sequences = []
	sequence_length = 0

	with open('input.txt', 'r') as input_file:
			sequence_length = len(input_file.readline())
			input_file.seek(0)
			print(f'Squence Length:  {sequence_length}')
			for line in input_file:
				line = line.strip()
				sequences.append(line)

	counter = 0
	oxygen_rate = sequences
	scrubber_rate = sequences
	print(oxygen_rate)
	print(scrubber_rate)

	while len(oxygen_rate) > 1: # We only check oxygen but both lists are made from the same original so they decrease at the same rate.
		oxygen_rate = get_oxygen_rate(oxygen_rate, counter)
		scrubber_rate = get_scrubber_rate(scrubber_rate, counter)
		counter += 1
	print(oxygen_rate)

	# Convert binary to decimal
	oxygen_answer = (int(oxygen_rate[0],2))
	scrubber_answer = (int(scrubber_rate[0],2))
	# Get answer
	total = oxygen_answer * scrubber_answer

	print(f"Answer: {total}")

main()