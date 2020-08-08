import time

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
time.sleep(6)

# driver.find_element_by_id("kw").send_keys("明日之子")
# driver.find_element_by_id("su").click()

#driver.find_element_by_name("wd").send_keys("明日之子")
#driver.find_element_by_id("su").click()
#元素不唯一
# driver.find_element_by_class_name("s_ipt").send_keys("明日之子")
# driver.find_element_by_class_name("btn").click()
#元素不唯一
# driver.find_element_by_tag_name("input").send_keys("明日之子")
# driver.find_elements_by_id("su").click()
#连接内容必须唯一
# driver.find_element_by_link_text("视频").click()
# driver.find_element_by_partial_link_text("频").click()
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("明日之子")
# driver.find_element_by_xpath("//*[@id='su']").click()

driver.find_element_by_css_selector("#kw").send_keys("明日之子")
driver.find_element_by_css_selector("#su").click()
time.sleep(6)
driver.quit()
