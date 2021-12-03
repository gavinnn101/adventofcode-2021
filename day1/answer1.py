counter = 0
last = None

with open('input.txt', 'r') as input_file:
	for number in input_file:
		number = int(number)
		if last is None:
			last = number
		if last is not None and number > last:
			counter += 1
		last = number

print(counter)