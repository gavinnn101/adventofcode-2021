answer = 0
horizontal = 0
depth = 0

with open('input.txt', 'r') as input_file:
	for line in input_file:
		movement, number = line.split(' ')
		number = int(number)
		if movement == 'forward':
			horizontal += number
		elif movement == 'down':
			depth += number
		elif movement == 'up':
			depth -= number

answer = horizontal * depth
print(answer)