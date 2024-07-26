from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
riqi = random.randint(1,10)
print(riqi)
driver = webdriver.Chrome()
driver.get(url = 'https://mercury-testing.xintianweng.tech/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[3]/div/span/span[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[3]/ul/li[3]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[2]/div/span/button/span').click()
driver.find_element(By.XPATH,'//*[@id="demandCycle"]').send_keys(riqi)
driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').send_keys('测试仓库')
driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div[1]/div/div[2]/div/div[2]/button').click()#点击添加商品
time.sleep(6)

driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[1]/label').click()
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[1]/span').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[4]/div/div[2]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[4]/div/div[2]/input').send_keys(riqi)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[4]/div[2]/form/div[5]/div/div/div/div/div[2]/button/span').click()
driver.implicitly_wait(5)
time.sleep(5)
driver.quit()