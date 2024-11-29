print("Give me two numbers, and i'll divide them! ")
print("Enter 'q' to quit! ")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		print("You left the calculator!")
		break

	second_number = input("Second number: ")
	if second_number == 'q':
		print("You left the calculator!")
		break
		
	try:	
		answer = int(first_number) / int(second_number)
		
	except ZeroDivisionError:
		print("You can't divide by zero! ")

	except ValueError:
		print("You can't divide by str")

	else:
		print(answer)

