from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get('https://lalafo.kg/')
    btn_elem = driver.find_element("main-feed__container")
    print(btn_elem)
    price = driver.find_elements('a')
    print(price)


if __name__ == "__main__":
    main()



