
from rich import print as rp
from rich.console import Console

console = Console()

def get_hello(username):
	rp(f"[italic black]Hello [/italic black] [italic red]{username.title()}[/italic red]")


username = input("Введите имя пользователя: ")
get_hello(username)
