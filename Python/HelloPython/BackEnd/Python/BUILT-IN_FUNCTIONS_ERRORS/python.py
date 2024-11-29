# Принцып единствоенной ответственности:

class Journal:
	def __init__ (self):
		self.entries = []
		self.count = 0


	def add_entry(self, text):
		self.count += 1
		self.entries.append(f"{self.count}: {text}")


	def remove_entrties(self, pos):
		del self.entries[pos]

	def __str__(self):
		return "\n".join(self.entries)

j = Journal()

j.add_entry("i learned a lot to day")
j.add_entry("and i want to study further")

print(f"Journal entries: \n{j}")
