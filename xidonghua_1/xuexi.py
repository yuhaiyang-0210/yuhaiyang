import random

from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains



driver = webdriver.Chrome()
driver.get(url='https://www.albt.tech/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[2]/ul/li[1]/a').click()
time.sleep(2)
#向下滑动至底端可见固定写法
js1 = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js1)
time.sleep(3)
#向上滑动至顶端可见固定写法

js2 = "window.scrollTo(0,0)"
driver.execute_script(js2)
time.sleep(3)
# driver.quit()
#点击联系我们
driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[2]/ul/li[5]/a').click()
driver.implicitly_wait(4)
time.sleep(3)

#获取当前句柄
handles = driver.window_handles
print(handles)
#切换至最先打开的窗口
driver.switch_to.window(handles[0])
#切换至最新打开的窗口   注释：想要到达哪个窗口后面数字填写即可
driver.switch_to.window(handles[-1])
#获取 WebDriver 对象 当前聚焦的浏览器窗口句柄
driver.current_window_handle

#鼠标悬停
#定位到要悬停的位置
above = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/div/div[2]/ul/li[3]/a')
#对定位的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
time.sleep(3)





