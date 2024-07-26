from selenium import webdriver
from selenium.webdriver.common .by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string



driver = webdriver.Chrome()
driver.get(url = 'https://mercury-testing.xintianweng.tech/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[3]/div/span').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[3]/ul/li[4]/span').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[2]/div/span/div/div[3]/button/span[2]').click()#点击创建到货单
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[1]/div/div[2]/div/div[2]/button/span[2]').click()
time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="product_filter_ean_code"]').send_keys(21212215666)
driver.find_element(By.XPATH,'//*[@id="product_filter"]/div[1]/div[4]/div/div/div/div/div/div[1]/button').click()#点击提交
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/label/span/input').click()#选择搜索出来的第一个商品
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()#添加至到货通知单
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[1]').click()#点击完成
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').send_keys('测试货主')
driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').send_keys(Keys.ENTER)
driver.implicitly_wait(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[5]/div/div[2]/input').click()
jiage = random.randint(1,1000)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[5]/div/div[2]/input').send_keys(jiage)
daohuoshuliang = random.randint(1,10)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[6]/div/div[2]/input').click()
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[6]/div/div[2]/input').send_keys(daohuoshuliang)
#已添加商品（指定）货主测试货主，价格以及数量随机
driver.find_element(By.XPATH,'//*[@id="type"]/label[1]/span[2]').click()#选择退货收获
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').click()
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').send_keys('2022-08-30')
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="rc_select_4"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_4"]').send_keys('测试仓库')
driver.find_element(By.XPATH,'//*[@id="rc_select_4"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[2]/div[2]/form/div[4]/div[2]/div/div/div/label[2]/span[1]/input').click()#选择优惠率

driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[2]/div[2]/form/div[4]/div[2]/div/div/div/label[2]/span[2]/input').send_keys(10)
danhao =  ''.join(str(random.choice(range(10))) for _ in range(10))
driver.find_element(By.XPATH,'//*[@id="relatedSerialNumber"]').send_keys(danhao)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[2]/div[2]/form/div[11]/div/div/div/div/div[2]/button/span').click()
time.sleep(5)
driver.quit()