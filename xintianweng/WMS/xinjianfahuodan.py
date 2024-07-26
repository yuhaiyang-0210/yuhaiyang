from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
from random import  choice



def random_phonenuber():
    aret_num = ['135','166','187','186','158','144','147','156','176','177','187']

    eightnum = "".join(random.sample(string.digits,8))
    return random.choice(aret_num)+eightnum
print(random_phonenuber())
shuliang = random.randint(1,100)
print(shuliang)
driver = webdriver.Chrome()
driver.get(url='https://mercury-testing.xintianweng.tech/')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div/span').click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[2]/ul/li[3]/span').click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[2]/div/span/button').click()#点击创建发货单
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[1]/div/div[2]/div/div[2]/button').click()#点击添加按钮
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="product_filter_code"]').send_keys('SP119983920462731730')#输入商品编码，可改动动
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="product_filter_code"]').send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div/div/table/thead/tr/th[1]/div/label').click()
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()#添加至发货通知单
driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[1]/span').click()#点击完成

driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').click()
driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').send_keys('测试货主')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="rc_select_7"]').send_keys(Keys.ENTER)#选择货主
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[5]/div/div[2]/input').click()

driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr[2]/td[5]/div/div[2]/input').send_keys(shuliang)

driver.find_element(By.XPATH,'//*[@id="type"]/label[1]/span[1]/input').click()#手动发货
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="createReason"]').click()
driver.find_element(By.XPATH,'//*[@id="createReason"]').send_keys(Keys.ENTER)#建单原因
danhao = random.randint (100,10000)
print(danhao)
driver.find_element(By.XPATH,'//*[@id="relatedSerialNumber"]').send_keys(danhao)#输入关联单号
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').click()
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').send_keys('2022-08-25 13:56:31')
driver.find_element(By.XPATH,'//*[@id="expectedArrivalTime"]').send_keys(Keys.ENTER)#选择日期
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'/html/body/div[1]/section/section/main/div[3]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/div[2]/div/div/div/div/span[1]/input').click()
driver.find_element(By.XPATH,'//html/body/div[1]/section/section/main/div[3]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/div[2]/div/div/div/div/span[1]/input').send_keys('mtps测试仓库')
driver.find_element(By.XPATH,'/html/body/div[1]/section/section/main/div[3]/div/div[2]/div[2]/div/div/div/div[1]/form/div[6]/div[2]/div/div/div/div/span[1]/input').send_keys(Keys.ENTER)#选择发货仓库
xingm = (random.sample(string.ascii_letters+string.digits,7))
print(xingm)
driver.find_element(By.XPATH,'//*[@id="consigneeInfo_name"]').send_keys(xingm)#输入姓名
driver.implicitly_wait(3)

driver.find_element(By.XPATH,'/html/body/div[1]/section/section/main/div[3]/div/div[2]/div[2]/div/div/div/div[1]/form/div[8]/div[2]/div/div/input').send_keys(random_phonenuber())#输入电话
driver.implicitly_wait(3)
driver.find_element(By.XPATH,'//*[@id="consigneeInfo_poiAddress"]').send_keys('曹杨路地铁站')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="consigneeInfo_poiAddress"]').send_keys(Keys.UP)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="consigneeInfo_poiAddress"]').send_keys(Keys.ENTER)#选择poi地址
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="consigneeInfo_detailAddress"]').send_keys('曹杨路街道450号绿创大厦')
driver.find_element(By.XPATH,'//*[@id="remark"]').send_keys('自动化脚本创建')
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[2]/div[2]/div/div/div/div[1]/form/div[15]/div/div/div/div/div[2]/button').click()#保存发货单

print('发货单创建成功了，收货人姓名为{}，手机号为{}，商品数量为{}'.format(xingm,random_phonenuber(),shuliang))

time.sleep(6)

driver.quit()