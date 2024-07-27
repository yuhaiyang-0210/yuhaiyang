import time

import allure
from selenium import webdriver

def test_case_baidu ():
    driver = webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")
    driver.get(url='http://www.baidu.com')
    driver.maximize_window()
    time.sleep(5)
    #下面这条为故意失败
    try:
        driver.find_element(by=id(1234))
    except Exception as e:
        img = driver.get_screenshot_as_png()
        allure.attach(img,'失败截图',allure.attachment_type.PNG)


