from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#s=Service(path)
#driver=webdriver.Chrome(service=s)
driver.get('https://lalafo.kg/')
driver.find_element(By.NAME, 'main-feed__container')