'''
登录页面: https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F
抢购页面 https://detail.damai.cn/item.htm?id=707098209282

selector
# #fm-login-id

selenium 3.141.0
'''

from selenium import webdriver

login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
target_url = 'https://detail.damai.cn/item.htm?id=707098209282'


driver = webdriver.Chrome()
driver.get(login_url)

# 进入iframe
driver.switch_to.frame(0)

# sector
driver.find_element_by_css_selector('#fm-login-id').send_keys('1213')
