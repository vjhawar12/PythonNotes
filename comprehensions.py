# a list comprehension is a faster way to create a list with a for loop
# it allows you to write the for loop inside of the list

def oneD():
	# list with each letter in the string
	phrase = "this is a sentence"
	lis = [letter for letter in phrase]
	print(lis)

	# list with all the odd numbers from 1 - 20
	lis = [num for num in range(21) if num % 2 == 1]
	print(lis)

	# list with all the odd factors of 5 from 1 - 20
	lis = [num for num in range(21) if num % 2 == 1 and num % 5 == 0]
	print(lis)

	# square of all numbers from 1 - 10
	lis = [num ** 2 for num in range(1, 11)]
	print(lis)

# nested list comprehension
l = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], ['30', '20', '30', '50', '10', '30', '20', '20', '20']]
# convert each number to int 
print(l)
lis = [[int(i) for i in j] for j in l] 
print(lis)

