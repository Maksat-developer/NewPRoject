from time import sleep
from rich.console import Console
from rich import print

main_data = 17576

data_1 = [34**2, 26*3, 17*33, 4394*4]

list_1 = [
data_1[0],
data_1[1], 
data_1[2],
data_1[3], 
]


console = Console()
tasks = [f"задача {n}" for n in range(0, 5)]
with console.status("[bold green]Выполнение задачи  ...[/bold green]") as status:
	while tasks:
		task = tasks.pop(0)
		sleep(1)
		console.log(f"{task} Выполнено!!!")
for i in list_1:
	if i != list_1[0] and i  == main_data:
		a = f"{i} == {main_data}"
		with console.status("[bold green]Выполнение задачи  ...[/bold green]") as status:
			sleep(1)
			console.log(f"{a} Успешное совпадение!")
	else:
		b = f"{i} != {main_data}"
		with console.status("[bold green]Выполнение задачи  ...[/bold green]") as status:
			sleep(1)
			console.log(f"{b} Эти варианты нам не подходять! ")