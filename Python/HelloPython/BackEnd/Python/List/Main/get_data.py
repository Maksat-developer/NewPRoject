from rich import print as rp
from time import sleep
from rich.console import Console
from rich.progress import track
import random

console = Console()

list_guets = ["kairat", "mirbek", "dastan"]

message_invite = "Приглошение выслано:"
for name in list_guets:
    sleep(0.10)
    str(list_guets)
    with console.status(f"[bold green]Обработка данных клиента: {name.title()}[/bold green]") as status:
        sleep(3)
        console.log(status)
    rp(f"[italic red]{message_invite}[/italic red] [italic Green]{name.title()}[/italic Green]")

sleep(2)

rp("[italic purple]|---------------------------------------------------------------------------------------------|[/italic purple]")

with console.status(f"[italic white]IP-Адреса получены.[/italic white]") as get_ip:
    sleep(3)
    console.log(get_ip)

with console.status(f"[italic white]Личные данные клиентов сохранены.[/italic white]") as get_path:
    sleep(3)
    console.log(get_path)


def do_step(step):
    sleep(random.uniform(0.01, 0.02))


for step in track(
        range(101),
        description="[italic white]Проверка системы безопасности:[/italic white]"):
    do_step(step)
sleep(1)
with console.status("[italic white] Система работает в штатном режиме [/italic white]") as status_security:
    sleep(3)
    console.log(status_security)
