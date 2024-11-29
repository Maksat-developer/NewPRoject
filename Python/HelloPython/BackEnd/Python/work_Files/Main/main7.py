guest = input("Enter your name my dear: ")

filename = "guest.txt"
with open(filename, "a") as file_object:
	file_object.write(guest)
