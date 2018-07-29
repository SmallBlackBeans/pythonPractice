# 如果用Selenium来驱动浏览器加载网页的话，就可以直接拿到JavaScript渲染的结果了
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome()
try:
    brower.get('https://www.baidu.com')
    input = brower.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(brower, 10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(brower.current_url)
    print(brower.get_cookies())
    print(brower.page_source)
finally:
    brower.close()


# 无界面浏览器PhantomJS
brower = webdriver.Chrome()
brower = webdriver.Firefox()
brower = webdriver.Edge()
brower = webdriver.PhantomJS()
brower = webdriver.Safari()

# 节点交互
import time
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()

""" 动作链 比如鼠标拖曳、键盘按键 """
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()


""" 执行 JS 因为可能一些功能API没有提供 那么就用js实现"""
brower = webdriver.Chrome()
brower.get('https://www.zhihu.com/explore')
brower.execute_script('window.scrollTo(0, document.body.scrollHeight)')
brower.execute_script('alert("To Bottom")')


""" 获取节点信息 """
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

""" 切换 iFrame """
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

""" 延时等待 """
# 隐式等待 指定页面加载时间
browser = webdriver.Chrome()
browser.implicitly_wait(10) # 等待10s 如果超时还没有指定的元素出现，则报异常
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)

# 显示等待 指定指定元素等待时间
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

""" 前进和后退 """
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()