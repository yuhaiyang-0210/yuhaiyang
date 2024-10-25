from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get(url= 'https://www.baidu.com')
driver.maximize_window()
time.sleep(3)