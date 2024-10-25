from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get(url = "https://venus-testing.xintianweng.tech/")#浏览器输入链接
driver.maximize_window()#最大化浏览器窗口
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div/span/span[2]').click()#展开商品管理父菜单
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[2]/ul/li[8]/span').click()#进入平台惨淡管理
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="orderFilter_menu_id"]').click()#定位菜单id输入框
driver.find_element(By.XPATH,'//*[@id="orderFilter_menu_id"]').send_keys('168')#输入菜单id
driver.find_element(By.XPATH,'//*[@id="orderFilter"]/div/div[3]/div/div/div/div/div/div[1]/button/span').click()#提交搜索
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/a/div/div[2]').click()#进入菜单详情页面
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/button/span').click()#创建商品详情页面
time.sleep(3)
driver.quit()