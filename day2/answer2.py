answer = 0
horizontal = 0
depth = 0
aim = 0

with open('input.txt', 'r') as input_file:
	for line in input_file:
		movement, number = line.split(' ')
		number = int(number)
		if movement == 'forward':
			horizontal += number
			depth += aim * number
		elif movement == 'down':
			aim += number
		elif movement == 'up':
			aim -= number

answer = horizontal * depth
print(answer)