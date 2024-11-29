from turtle import Turtle
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

btnHello = KeyboardButton("Привет! ")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(btnHello)


button1 = KeyboardButton("'Лёгкий' варианты отображаютсья ниже \n⬇️")
button2 = KeyboardButton("'Средний' варианты отображаютсья ниже \n⬇️")
button3 = KeyboardButton("'Тяжёлый' варианты отображаютсья ниже \n⬇️")

var1 = KeyboardButton("A) Обито")
var2 = KeyboardButton("B) Хаширама")
var3 = KeyboardButton("C) Итачи и Обито")
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).row(var1, var2, var3)


var4 = KeyboardButton("A) Баку")
var5 = KeyboardButton("B) Гамабунта")
var6 = KeyboardButton("C) Энма")
markup4 = ReplyKeyboardMarkup(resize_keyboard=True).row(var4, var5, var6)


var7 = KeyboardButton("A) Белый")
var8 = KeyboardButton("B) Красный")
var9 = KeyboardButton("C) Оранжевый")
markup5 = ReplyKeyboardMarkup(resize_keyboard=True).row(var7, var8, var9)

markup2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1, button2, button3)






