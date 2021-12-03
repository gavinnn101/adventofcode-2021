counter = 0
nums = []

with open('input.txt', 'r') as input_file:
	for number in input_file:
		number = int(number)
		nums.append(number)

for num in range(len(nums)):
	try:
		sum1 = nums[num] + nums[num+1] + nums[num+2]
		sum2 = nums[num+1] + nums[num+2] + nums[num+3]
	except IndexError:
		print('Hit end of list, index error')
		break
	else:
		if sum2 > sum1:
			counter += 1

print(counter)