from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url = 'https://www.baidu.com')
driver.maximize_window()