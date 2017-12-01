from selenium import webdriver
from selenium.webdriver.commom.by import By
from selenium.webdriver.commom.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# 基本使用
browser = webdriver.Chrome()
try:
	browser.get('https://www.baidu.com')
	input = browser.find_element_by_id('kw')
	input.send_keys('Python')
	input.send_keys(Keys.ENTER)
	wait = WebDriverWait(brower, 10)  等待ID为content_left的元素加载出来
	wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
	print(browser.current_url)
	print(browser.get_cookies())
	print(browser.page_source)  # 网页的源代码
finally:
	browser.close()

# 声明浏览器对象
from selenium import webdriver
browser = wendriver.Chrome()
browser = wendriver.Firefox()
browser = wendriver.Edge()
browser = wendriver.PhantomJS()
browser = wendriver.Safari()

# 访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)
brower.close()

# 查找元素（单个）
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
brower.close()
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
# find_element(By.ID, 'xxx')

# 查找元素（多个），返回列表
browser.get('https://www.taobao.com')
input_second = browser.find_elements_by_css_selector('#q')
print(input_first, input_second, input_third)
brower.close()
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector
# find_elements(By.CSS_SELECTOR, 'xxx')

# 元素交互操作（登录淘宝，搜索框输入iphone，然后清除，然后输入ipad，然后点击搜索)
browser.get('https://www.taobao.com')
print(browser.page_source)
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn_search')
button.click()
# 更多操作：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement

# 交互动作
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
# 更多操作：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.commom.action_chains

# 执行JS
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')

# 获取元素信息（获取属性）
from selenium.webdriver import ActionChaions
browser.get('https://www.zhihu.com/explore')
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))

# 获取元素信息（获取文本值、获取ID、位置、标签名、大小）
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)

# Frame（在子Frame内获取Frame外的元素是获取不到的）
from selenium.common.exceptions import NoSuchElementException
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
browser.switch_to.frame('iframeResult')  # 切换到子frame
source = browser.find_element_by_css_selector('#draggable')
try:
	logo = browser.find_element_by_class_name('logo')  # 在子frame找父frame的元素
except NoSuchElementException:
	print('No Logo')
browser.switch_to.parent_frame()  # 切换到父frame
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

# 等待
# 隐式等待：当使用了隐式等待执行测试的时候，如果webdriver没有在DOM中找到元素，将继续等待，直到超出设定时间找不到元素抛出异常,默认时间为0
browser.implicitiy_wait(10)
brpwser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)

# 显式等待：指定一个等待条件和最长等待时间，如果最长等待时间内不满足等待条件，会一直等待直到最长等待时间抛出异常
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'btn-search')))
print(input,button)

# title_is  标题是某内容
# title_contains 标题包含某内容
# presence_of_element_located 元素加载出，传入定位元祖，如（By.ID,'p'）
# visibility_of_element_located 元素可见，传入定位元祖
# visibility_of 传入元素对象
# presence_of_all_elements_located 所有元素加载出
# text_to_be_present_in_element 某个元素文本包含某文字
# text_to_be_present_in_element_value 某个元素值包含某文字
# frame_to_be_available_and_switch_to_it_frame 加载并切换
# invisibility_of_element 元素不可见
# element_to_be_clickable 元素可点击
# staleness_of 判断一个元素是否仍在DOM，可判断页面是否已经刷新
# element_to_be_selected 元素可选择，传元素对象
# element_located_to_be_selected 元素可选择，传入定位元祖
# element_selection_state_to_be 传入元素对象以及状态，相等返回True，否则返回False
# element_located_selection_state_to_be 传入定位元祖以及状态，相等返回True，反正返回False
# alert_is_present 是否出现Alert
# 详细内容：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# 前进后退
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()

# Cookies
brpwser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

# 选项卡管理(窗口管理)
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.python.org/')

# 异常处理
from selenium.common.exceptions import TimeoutException, NoSuchElementException
try:
	browser.get('https://www.baidu.com')
except TimeoutException:
	print('time out')
try:
	browser.find_element_by_id('hello')
except NoSuchElementException:
	print('No Element')
finally:
	browser.close()
# 详细内容：http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
