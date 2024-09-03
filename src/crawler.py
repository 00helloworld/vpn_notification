from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from src.log_config import info_logger, error_logger

# 设置 Chrome 选项
chrome_options = Options()

# 启用无头模式
# chrome_options.add_argument("--headless")

# 添加隐藏 WebDriver 的特征的选项
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("blink-settings=imagesEnabled=false")
chrome_options.page_load_strategy = 'eager'

# 创建 Chrome WebDriver
# 注意：需要提前下载对应版本的 ChromeDriver，并指定其路径

def save_html(driver, name='tmp'):
    html_content = driver.page_source
    with open(f'dev/{name}.html', 'w') as f:
        f.write(html_content)

def crawler(url='https://qytcc01a.qingyunti.pro/dashboard'):
    # 指定driver路径（如果需要）
    driver_path = '/Users/dongyanshen/Desktop/DYSProjects/VPNMonitor/driver/chromedriver-mac-arm64/chromedriver'
    service = Service(driver_path)
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.implicitly_wait(30)
    driver.get(url)

    try:
        # 等待指定的 input 元素出现
        element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
        info_logger.debug("等待登陆邮箱出现出现 Succeed")
    except:
        info_logger.debug("等待登陆邮箱出现出现 Fail")
        pass

    save_html(driver, name='login')

    user = 'd497465762@gmail.com'
    password = 'Dd963214@'

    # Login
    time.sleep(3)
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(user)
    time.sleep(3)
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(password)
    time.sleep(3)
    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg'))
    )
    submit_button.click()

    # Read data
    element_usage = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '已使用')]"))
    )
    print(element_usage.text)
    save_html(driver, name='dashboard')

    return element_usage.text




