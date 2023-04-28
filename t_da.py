'''
登录页面: https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F
抢购页面 https://detail.damai.cn/item.htm?id=707098209282

selector
# #fm-login-id

selenium 3.141.0
'''
import time

from selenium import webdriver

login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
target_url = 'https://detail.damai.cn/item.htm?id=707098209282'

# 浏览器配置对象
options = webdriver.ChromeOptions()
# 禁用自动化栏
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

# 屏蔽保存密码提示框
prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}
options.add_experimental_option('prefs', prefs)
# 反爬虫特征处理
options.add_argument('--disable-blink-features=AutomationControlled')

# 打开浏览器
driver = webdriver.Chrome(options=options)

# f = open('stealth.min.js', mode='r', encoding='utf-8').read()
# 移除selenium当中爬虫的特征
# driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': f})


# 打开登录页
driver.get(login_url)

# 进入iframe
driver.switch_to.frame(0)

# sector
# account
driver.find_element_by_css_selector('#fm-login-id').send_keys('1213')
# pwd
driver.find_element_by_css_selector('#fm-login-password').send_keys('1213')

time.sleep(1)

# 过滑块
driver.switch_to.frame(0)
slider = driver.find_element_by_css_selector('#nc_1_n1z')
if slider.is_displayed():
    # 让鼠标执行, 点击并且保持按住元素 slider
    webdriver.ActionChains(driver).click_and_hold(on_element=slider).perform()
    # 往x轴横向移动鼠标
    # webdriver.ActionChains(driver).move_by_offset(xoffset=258, yoffset=0).perform()
    webdriver.ActionChains(driver).move_by_offset(xoffset=200, yoffset=0).perform()
    time.sleep(0.3)
    webdriver.ActionChains(driver).move_by_offset(xoffset=50, yoffset=0).perform()
    time.sleep(0.5)
    webdriver.ActionChains(driver).move_by_offset(xoffset=10, yoffset=0).perform()
    time.sleep(0.5)

    # 松开鼠标
    webdriver.ActionChains(driver).pause(1.5).release().perform()

driver.switch_to.parent_frame()

# button
driver.find_element_by_css_selector('#login-form > div.fm-btn > button').click()

# 等待登录
time.sleep(3)
