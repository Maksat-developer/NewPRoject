
filename = "learning_python.txt"
with open(filename) as open_the_file:
	open_the_file = open_the_file.readlines()

py_str = ''



for i in range(3):
	for line in open_the_file:
		open_the_file += py_str

	print(open_the_file, "\n")

