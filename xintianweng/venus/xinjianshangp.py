from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as  EC



driver = webdriver.Chrome()
driver.get(url = "https://venus-testing.xintianweng.tech/")#浏览器输入链接
driver.maximize_window()#最大化浏览器窗口
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div/span/span[2]').click()#展开商品管理父菜单
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[2]/ul/li[8]/span').click()#进入平台菜单管理
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="orderFilter_menu_id"]').click()#定位菜单id输入框
driver.find_element(By.XPATH,'//*[@id="orderFilter_menu_id"]').send_keys('168')#输入菜单id
driver.find_element(By.XPATH,'//*[@id="orderFilter"]/div/div[3]/div/div/div/div/div/div[1]/button/span').click()#提交搜索
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[3]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/a/div/div[2]').click()#进入菜单详情页面
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[2]/div[2]/div[4]/div[1]/div[1]/div[2]/button/span').click()#创建商品详情页面
ran = (random.sample(string.ascii_letters+string.digits,10))
print(ran)
driver.find_element(By.XPATH,'//*[@id="menuSpuName"]').send_keys(ran)#商品名称随机输入10位字符+数字
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="menuCatId"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div/div/ul/li[2]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//ul[2]/li').click()#选择商品分类
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[3]/div[2]/div/div/form/div[4]/div[2]/div[1]/div/div/div/span/div/span').click()#点击上传图片
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="status"]/label[1]/span[1]/input').click()#选择售卖状态
time.sleep(2)
jiage = random.randint(1,100)
print(jiage)
driver.find_element(By.XPATH,'//*[@id="specList_0_sellingPrice"]').send_keys(jiage)#输入规格价格
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="specList_0_inventoryOwnerId"]').send_keys('测试')
driver.find_element(By.XPATH,'//*[@id="specList_0_inventoryOwnerId"]').send_keys(Keys.ENTER)#选择货主为‘测试’
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[3]/div[2]/div/div/form/div[10]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/table/tbody/tr[2]/td[11]/div/div/div/div/div/div/button/span[1]').click()#点击关联标品
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="bindSpWay"]/label[2]/span[2]').click()#选择文本方式
driver.implicitly_wait(2)
driver.find_element(By.XPATH,'//*[@id="textCommand"]').click()
driver.find_element(By.XPATH,'//*[@id="textCommand"]').send_keys('SP400990642204962216')#输入文本指令

driver.find_element(By.XPATH,'//button[2]/span').click()#保存关联信息


driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div/div[3]/div[2]/div/div/form/div[12]/div/div/div/div/div[2]/button/span').click()#提交并触发同步
