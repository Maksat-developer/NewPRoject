from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
url = "https://www.vk.com/"
# для запросов


driver = webdriver.Firefox(executable_path='firefoxdriver/geckodriver')
# Наш браузер которому мы будем отдавать команды
try:
    driver.get(url=url)
    driver.save_screenshot("vk.png")
    time.sleep(5)
    # driver.get(url='https://www.facebook.com/')
    # time.sleep(5)

    # driver.refresh() # обновляет окно браузера
    # time.sleep(2)

    # driver.get_screenshot_as_file("1.png") # для получения скриншота с браузера указ к 1 скрин
    # driver.get(url='https://www.facebook.com/')
    # time.sleep(5)
    # driver.save_screenshot("2.png") # указ ко 2 скрину


except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()



#
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Firefox(executable_path='firefoxdriver/geckodriver')
# driver.get("http://www.instagram.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()