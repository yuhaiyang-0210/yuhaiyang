from selenium import webdriver
import time

friver=webdriver.Edge()
friver.get(url='https://www.baidu.com')
friver.maximize_window()
time.sleep(2)
quit()
