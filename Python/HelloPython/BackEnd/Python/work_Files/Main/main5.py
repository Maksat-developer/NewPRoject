filename = "learning_python.txt"

with open(filename) as file:
	lines = file.readlines()

py_str = ''

for line in lines:
	rep = line.replace("python", "C")
	rep2 = line.replace("Python", "==C")

print(rep, rep2)
