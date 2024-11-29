# I love programming.
filename = "answer.txt"
a = 0
while a < 3:
	user = input("Three reasons why you like programming? ")
	print(user)
	a += 1

	with open(filename, "a") as file_object:
		file_object.write(f"{user}\n")

