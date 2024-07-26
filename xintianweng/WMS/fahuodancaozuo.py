from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import service

driver = webdriver.Edge(executable_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")#打开浏览器
driver.get(url = "https://mercury-testing.xintianweng.tech/")#浏览器输入链接
driver.maximize_window()#最大化浏览器窗口
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys('信天翁（上海）')#定位到选择租户筛选框输入租户名称选择租户
driver.find_element(By.XPATH,'//*[@id="rc_select_0"]').send_keys((Keys.ENTER))#回车
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="root"]/section/aside/div/ul/li[2]/div/span/span[2]').click()#点击发货单管理展开发货单子菜单
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/section/aside/div/ul/li[2]/ul/li[1]/span').click()#点击发货通知单
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="so_filter_status_list"]/label[1]/span[1]/input').click()#筛选状态为已确认
driver.find_element(By.XPATH,'//*[@id="so_filter"]/div[1]/div[5]/div/div/div/div/div/div[1]/button').click()#点击提交
# js = 'window.scrollTo(0,document.body.scrollHeight)'
# driver.execute_script(js)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[1]/div/div/div/div[1]/span/a').click()#选择筛选的第一个结果点击
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/ul/li/span/div/div[1]/button/span').click()#点击开始拣货
time.sleep(2)
driver.find_element(By.XPATH,'//div[2]/div/div[2]/div[3]/button/span').click()#复制错误信息
driver.find_element(By.XPATH,'//*[@id="root"]/section/section/main/div[3]/div/div[1]/ul/li/span/div/div[3]/button/span').click()#点击上报异常
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="remark"]').send_keys(Keys.CONTROL,'V')#粘贴错误信息
time.sleep(3)
driver.find_element(By.XPATH,'//div[2]/div/div[2]/div[3]/button[2]/span').click()#点击确定
time.sleep(5)

driver.quit()

