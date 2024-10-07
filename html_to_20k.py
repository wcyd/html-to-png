from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# 启动 Chrome 浏览器
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 无界面模式
options.add_argument('--start-maximized') # 最大化窗口
options.add_argument("--window-size=(3840*5)x(2160*5)")  # 设置窗口大小为20K分辨率

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 获取本地 HTML 文件的绝对路径
# html_file_path = os.path.abspath("7年级上册第1章.html")
# file_url = "file:///" + html_file_path.replace("\\", "/")
file_url = r"D:/小学数学/电子教材/7年级上册第1章.html"

# 打开本地 HTML 文件
driver.get(file_url)

# 等待页面加载完成
time.sleep(2)

# 设置页面缩放比例（5倍放大）
driver.execute_script("document.body.style.transform = 'scale(5)'; document.body.style.transformOrigin = '0 0';")

# 动态调整窗口大小以适应整个页面
S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))  # 根据内容动态调整窗口大小

# 截取全页面的截图
screenshot_path = "full_page_screenshot.png"
driver.save_screenshot(screenshot_path)

# 关闭浏览器
driver.quit()

print(f"Screenshot saved as {screenshot_path}")