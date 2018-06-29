from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select


# 下面的代码实现了模拟提交提交搜索的功能，首先等页面加载完成，然后输入到搜索框文本，点击提交
driver = webdriver.Chrome()
driver.get("http://www.python.org")


# assert "Python" in driver.title
# elem = driver.find_element_by_name('q')
# # 模拟键盘输入
# elem.send_keys("pycon")
# # 回车
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)


# '''
# <input type="text" name="passwd" id="passwd-id" />
# '''
# element = driver.find_element_by_id("passwd-id")
# element = driver.find_element_by_name("passwd")
# element = driver.find_elements_by_tag_name("input")
# # I like it 如果有多个元素匹配了 xpath，它只会返回第一个匹配的元素
# element = driver.find_element_by_xpath("//input[@id='passwd-id']")


'''
表单元素 下拉选项卡
'''
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name('option')
for option in all_options:
    print('value is %s ' % option.get_attribute('value'))
    option.click()

select = Select(driver.find_element_by_name('name'))
index = 1
value = 'red'
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
# 所有可选项
options = select.options
# 所有已选选项
all_selected_options = select.all_selected_options
# 全部取消
select.deselect_all()

# 提交表单
driver.find_element_by_id('submit').click()

'''
元素拖拽
'''
from selenium.webdriver import ActionChains

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

'''
页面切换
'''
# 切换窗口
driver.switch_to.window("windowName")
# 获取每个窗口对象
for handle in driver.window_handles:
    driver.switch_to.window(handle)
# 切换frame
driver.switch_to.frame("frameName.0.child")

'''
弹窗处理
'''
alert = driver.switch_to.alert()


'''
历史记录
'''
driver.forward()
driver.back()

'''
Cookies处理
'''
# go to the correct domain
driver.get("http://www.example.com")

# Now set the cookie. This one's valid for the entire domain
cookie = {'name': 'foo', 'value': 'bar'}
driver.add_cookie(cookie)


'''
元素选取
'''
from selenium.webdriver.common.by import By
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
driver.find_element(By.XPATH,'//button[text()="some text]')
driver.find_elements(By.XPATH,'//button')


''''
页面等待  显示等待/隐式等待
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get('http://www.baidu.com')
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,'idElement'))
        )
finally:
    driver.quit()


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

# 隐式等待
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")
