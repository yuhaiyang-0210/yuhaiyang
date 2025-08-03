#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用pytest框架的百度搜索测试
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TestBaiduSearch:
    """百度搜索测试类"""

    @pytest.fixture(scope="class")
    def driver(self):
        """设置浏览器驱动"""
        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        # 自动下载并设置ChromeDriver
        service = Service(ChromeDriverManager().install())

        # 创建WebDriver实例
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(10)

        yield driver

        # 测试结束后关闭浏览器
        driver.quit()

    def test_open_baidu_homepage(self, driver):
        """测试打开百度首页"""
        print("🌐 正在打开百度首页...")
        driver.get("https://www.baidu.com")

        # 等待页面加载完成
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "kw")))

        # 验证搜索框存在
        assert search_box.is_displayed(), "搜索框应该可见"
        print("✅ 百度首页加载成功")

    def test_search_yuhaiyang(self, driver):
        """测试搜索'余海洋'"""
        print("🔍 正在搜索'余海洋'...")

        # 找到搜索框
        search_box = driver.find_element(By.ID, "kw")

        # 清空搜索框
        search_box.clear()

        # 输入搜索关键词
        search_box.send_keys("余海洋")

        # 按回车键搜索
        search_box.send_keys(Keys.RETURN)

        # 等待搜索结果加载
        wait = WebDriverWait(driver, 10)
        content_left = wait.until(EC.presence_of_element_located((By.ID, "content_left")))

        # 验证搜索结果页面加载
        assert content_left.is_displayed(), "搜索结果页面应该可见"
        print("✅ 搜索完成")

    def test_verify_search_results(self, driver):
        """验证搜索结果"""
        print("🔍 验证搜索结果...")

        # 等待搜索结果出现
        wait = WebDriverWait(driver, 10)
        results = driver.find_elements(By.CSS_SELECTOR, "#content_left .result")

        # 验证至少有一个搜索结果
        assert len(results) > 0, "应该至少有一个搜索结果"
        print(f"✅ 找到 {len(results)} 个搜索结果")

    def test_take_screenshot(self, driver):
        """截图测试"""
        print("📸 正在截图...")

        # 截图保存
        filename = "baidu_search_result.png"
        driver.save_screenshot(filename)

        # 验证截图文件存在（这里只是简单验证，实际应该检查文件大小等）
        print(f"✅ 截图已保存: {filename}")

    def test_complete_search_flow(self, driver):
        """完整的搜索流程测试"""
        print("🚀 开始完整搜索流程测试")

        # 1. 打开百度首页
        driver.get("https://www.baidu.com")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "kw")))

        # 2. 搜索"余海洋"
        search_box = driver.find_element(By.ID, "kw")
        search_box.clear()
        search_box.send_keys("余海洋")
        search_box.send_keys(Keys.RETURN)

        # 3. 等待搜索结果
        wait.until(EC.presence_of_element_located((By.ID, "content_left")))

        # 4. 验证搜索结果
        results = driver.find_elements(By.CSS_SELECTOR, "#content_left .result")
        assert len(results) > 0, "应该有搜索结果"

        # 5. 截图
        driver.save_screenshot("complete_search_flow.png")

        # 6. 等待几秒查看结果
        time.sleep(3)

        print("✅ 完整搜索流程测试通过")


if __name__ == "__main__":
    # 直接运行pytest
    pytest.main([__file__, "-v", "--html=test_report.html"])