import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Ввели не верный url")
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://context.reverso.net/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9/site")

