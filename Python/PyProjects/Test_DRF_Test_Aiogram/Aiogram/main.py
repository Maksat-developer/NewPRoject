import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram
from aiogram.types import ContentType
import keyboards as kb
from config import API_TOKEN
import emoji




logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, """

    Приветствую вас мой господин {0.first_name} я готова служить вам \n 
    И моя первостепенная задача вывести вам список коталогов
\n Чтобы вывести список коталогов введите сообщение '/Category'
     
     """.format(message.from_user)
    )

@dp.message_handler(commands=['Category'])
async def send_category_button(message: types.Message):
    await bot.send_message(message.from_user.id,"Наши категории в кнопках!", reply_markup=kb.markup2)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await bot.send_message(message.from_user.id, "Нужна помошь?")


@dp.message_handler()
async def send_reply(message: types.Message):
    if message.text == "'Лёгкий' варианты отображаютсья ниже \n⬇️":
        await message.reply("Я рада мой господин, желаю удачи 😌", reply_markup=kb.markup3)
        await bot.send_message(message.from_user.id, "Лёгкий вопрос вам \n Кто уничтожил весь клан Учих во вселенной -Наруто")
    if message.text == "C) Итачи и Обито":
        await message.reply("Верный ответ мой господин 😌")
    elif message.text == "B) Хаширама":
        await message.reply("Ответ не верный")
    elif message.text == "A) Обито":
        await message.reply("Вам надо подумать мой господин!")



    elif message.text == "'Средний' варианты отображаютсья ниже \n⬇️":
        await message.reply("Вижу вы подготовились к моим вопросам хмм... 😌", reply_markup=kb.markup4)
        await bot.send_message(message.from_user.id, "Среднечёк \nИ так Кто был личным призывом третьего Хокаге \n-Хирузена Сарутоби")

    if message.text == "C) Энма":
        await message.reply("Верный ответ мой господин 😌")
    elif message.text == "B) Гамабунта":
        await message.reply("Ответ не верный")
    elif message.text == "A) Баку":
        await message.reply("Вам надо подумать мой господин!")


    elif message.text == "'Тяжёлый' варианты отображаютсья ниже \n⬇️":
        await message.reply("Тут вам придётся подумать мой господин,\n не уж то в Google пойдёте за ответом аа...? 😌", reply_markup=kb.markup5)
        await bot.send_message(message.from_user.id, "Какой цвет имело кольцо Акацуки, которое носила \n-Конан ")

    if message.text == "A) Белый":
        await message.reply("Верный ответ мой господин 😌")
    elif message.text == "B) Красный":
        await message.reply("Ответ не верный")
    elif message.text == "C) Оранжевый":
        await message.reply("Вам надо подумать мой господин!")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)