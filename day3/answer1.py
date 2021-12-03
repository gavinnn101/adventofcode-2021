def get_rate(rate_type, data_file) -> int:
	"""pass 'gamma' or 'epsilon' to get either rate from the input file"""
	one_counter = 0
	zero_counter = 0
	answer = ''

	with open(data_file, 'r') as input_file:
		sequence_length = len(input_file.readline())
		input_file.seek(0)
		print(f'Sequence Length: {sequence_length}')
		for i in range(0, sequence_length-1):
			print(f'Iteration: {i}')
			for sequence in input_file:
				val = int(sequence[i])
				print(f'sequnece[i]: {sequence[i]}')
				if val == 0:
					zero_counter += 1
				elif val == 1:
					one_counter += 1
			print(f'Zero Counter: {zero_counter}')
			print(f'One Counter: {one_counter}')
			print('-----------------------------------')
			if rate_type == 'gamma':
				# Add the most used number
				if zero_counter > one_counter:
					answer += '0'
				elif one_counter > zero_counter:
					answer += '1'
			elif rate_type == 'epsilon':
				# Add the least used number
				if zero_counter > one_counter:
					answer += '1'
				elif one_counter > zero_counter:
					answer += '0'
			# Seek to top of file for next column
			input_file.seek(0)
			# Reset counters for next column
			one_counter = 0
			zero_counter = 0
		print(f'Answer: {answer}')
		return answer

# Get both answers in binary
gamma_answer = get_rate('gamma', 'input.txt')
epsilon_answer = get_rate('epsilon', 'input.txt')

# Convert binary to decimal
gamma_answer = (int(gamma_answer,2))
epsilon_answer = (int(epsilon_answer,2))

# Multiple both to get total
total_answer = gamma_answer * epsilon_answer
print(f'Answer: {total_answer}')

		
