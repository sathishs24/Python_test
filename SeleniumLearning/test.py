import time

from selenium import webdriver

url = "https://www.google.co.in/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(5)
driver.quit()


