from selenium import webdriver
import time

driver = webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")

driver.get(url = 'https://v.qq.com/')
driver.maximize_window()

time.sleep(5)

driver.close()