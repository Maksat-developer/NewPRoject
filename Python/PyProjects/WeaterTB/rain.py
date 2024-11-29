import requests
import aiogram

open_rnm_api ='https://rickandmortyapi.com/api/character/' # ссылка на сайт с которого хочешь выташить json
tb_token ="5070463877:AAFn362g_K88-v46PM7NG5lGQ9Q5AH3iVjU" #

bot = aiogram.Bot(token=tb_token) #
dp = aiogram.Dispatcher(bot) #

@dp.message_handler(commands=['start']) #
async def start_command(message: aiogram.types.Message): #
    await message.reply('hi') #

@dp.message_handler() #
async def get_rick(message: aiogram.types.Message): #
    data = open_rnm_api.json() #
    name = data["name"] #
    status = data["status"] #
    species = data["species"] #
    wind = data["wind"]["speed"] #
    print(f"Character's name: {name}\n Status: {status}\n Species: {species}\n Wind: {wind}") #
for i  in range(0, 200): #
    r = requests.get( #
    f"https://rickandmortyapi.com/api/character/{i}")
    data = r.json() #
    print(data)

