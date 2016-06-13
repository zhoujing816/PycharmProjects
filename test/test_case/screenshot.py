# encoding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.baidu.com/"
driver.get(url)
try:
    driver.find_element_by_css_selector("input#kw").send_key("selenium")
    driver.find_element_by_css_selector("input#su").submit()
except:
    driver.get_screenshot_as_file("C:\Users\jing\Documents\error1.png")
