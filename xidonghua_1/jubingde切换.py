from selenium import webdriver
from  selenium.webdriver.common .by import By
from  selenium.webdriver.common.keys import Keys
import time
#导入鼠标操作悬停类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get(url='https://www.baidu.com/')
driver.maximize_window()
#设置浏览器的大小
driver.set_window_size(480,800)
driver.implicitly_wait(8)
driver.refresh()

driver.find_element(By.XPATH,'//*[@id="kw"]').click()
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('光山天气')
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="1"]/div/div/div[2]/div[1]/div[1]/div/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="1"]/div/div/div[2]/div[1]/div[3]/div/a').click()
#打印最新窗口的句柄
h = driver.current_window_handle
print(h)
#打印浏览器所有的句柄
all_h =driver.window_handles
print(all_h)
#切换句柄到第二个页面
driver.switch_to.window(all_h[2])
print (driver.title)
driver.switch_to.window(h)

#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

time.sleep(1)

#访问新闻页面
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
driver.back()


#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()

time.sleep(3)
driver.quit()