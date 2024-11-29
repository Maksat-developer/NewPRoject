import requests
from bs4 import BeautifulSoup as bs

""" С этим парсингом всё готова он проходится по всем страничкам и вытаскивает 
все данные хорошо если просто  доделать её чтобы она сохраняла данные в "CSV" файл или "json" """


# page = 1
#
# while True:
#
#     # """ Тут мы будем указывать прямую ссылку на страницу сайта """
#     r = requests.get("https://stopgame.ru/review/new/izumitelno" + str(page))
#
#     html = bs(r.content, 'html.parser')
#
#     items = html.select(".items > .article-summary")
#         # """ Будем использовать "" для получения данных """
#
#     if (len(items)):
#         """ так как "" заходит в страничку и с помошью "" мы получаем там данные с нужных тегов """
#         for el in html.select(".items > .article-summary"):
#                 # "используем "for" для того чтобы пройтись по "html" который заходит в сайт "
#             title = el.select('.caption > a')
#                 # Тут надо разобраться!
#             print( title[0].text )
#
#             page  += 1
#             """ Нужно чтобы он проходил погинацию """
#     else:
#         break



""" Делаем так чтобы парсер вытаскивал уровень чела после регистрации в сайте в котором у человека повышается скилл,
и мы будем вытаскивать именно их развитие """


"""
 
 Сперва делаем пустой запрос на страницу с авторизацией, 
для этого сперва найди токен в на этой жэ странице который будет скорее всего скрыт и будет выглядеть примерно так

' <input type="hidden" value="ba1b82b2d4358f8e9ad554f634283780e869da16" name="YII_CSRF_TOKEN"> ' 


"""

s = requests.Session()

# get CSRF

auth_html = s.get("https://smartprogress.do/")
auth_bs = bs(auth_html.content, "html.parser")
csrf = auth_bs.select("input[ name=YII_CSRF_TOKEN]")[0]['value'] 
# """ Для того чтобы вытащить токены"""

# print(csrf)


#  do login указваем свои данные чтобы спарсить, Имя, Уровень, и Опыт.
payload = {
    "YII_CSRF_TOKEN": csrf,
    "returnUrl": "/",
    "UserLoginForm[email]": "stalkerciber@gmail.com",
    "UserLoginForm[password]": "Yjy2fVs3!rigd6b",
    "UserLoginForm[rememberMe]": 1,
     }

answ = s.post("https://smartprogress.do/user/login/", data = payload) 
    # нужно чтобы "" который заходит на сайт и страничку в котором расположены аккаунт пользователя
answ_bs = bs(answ.content, "html.parser") 

print( "Name: {}\nlevel: {}\nExperience: {}".format( #
    answ_bs.select(".user-menu__name")[0].text.strip(), #
    answ_bs.select(".user-menu__info-text--lvl")[0].text.strip(), #
    answ_bs.select(".user-menu__info-text--exp")[0].text.strip(), #

))

