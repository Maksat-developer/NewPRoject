filename = "guest_book.txt"

# with open(filename, "a") as file_object:
# 	py_str = ''
# 	a = 0
# 	while a < 5:
# 		user = input("Enter your name: \n")
# 		file_object.write(f"{user}\n")
# 		a += 1

with open(filename, "r") as open_the_file:
	lines = open_the_file.readlines()
py_str = ">>>"
for number, values_line in enumerate(lines):
	print(number, py_str, values_line)

