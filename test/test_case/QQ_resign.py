# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
url = "https://login.taobao.com/member/login.jhtml?spm=a21bo.50862.754894437.1.HqxfzY&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F"
driver.get(url)
driver.maximize_window()
#driver.find_element_by_id("J_Quick2Static").click()
if url == driver.current_url:
    print "same!"
else:
    print "different!"
driver.find_element_by_id("TPL_username_1").send_keys("zhoujing")
driver.find_element_by_id("TPL_password_1").send_keys("tonyjing618")
driver.find_element_by_id("J_SubmitStatic").click()
