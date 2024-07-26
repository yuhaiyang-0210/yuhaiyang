import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

name = ''.join(random.sample(string.ascii_letters+string.digits,10))
print(name)

jiage = random.randint(1,101)
print(jiage)
guige = random.uniform(1,10)
print(guige)
baozhiqi = random.randint(1,365)
print(baozhiqi)
ean = str(int(time.time()))[2:]
print(ean)

driver = webdriver.Chrome()
driver.get(url = 'https://venus-testing.xintianweng.tech/')
driver.maximize_window()
driver.implicitly_wait(20)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div/span').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[2]/ul/li[5]/span').click()
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div[1]/div/div[2]/div/div[2]/button/span').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="name"]').send_keys(name)
driver.find_element(By.XPATH,'//*[@id="categoryId"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="categoryId"]').send_keys('奶粉')
time.sleep(2)
driver.find_element(By.XPATH,'//li[4]/span[2]').click()
# driver.find_element(By.XPATH,'//*[@id="eanCode"]').send_keys(ean)
time.sleep(3)

driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').send_keys('红科技')

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').send_keys(Keys.UP)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="rc_select_2"]').send_keys(Keys.ENTER)#选择子品牌

driver.find_element(By.XPATH,'//*[@id="dimensions"]').send_keys('3,3,10')

driver.find_element(By.XPATH,'//*[@id="spec"]').send_keys(guige)

driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div[2]/form/div[10]/div[2]/div/div/div/div[1]/span[2]').click()
driver.find_element(By.XPATH,'')

time.sleep(4)
driver.quit()
