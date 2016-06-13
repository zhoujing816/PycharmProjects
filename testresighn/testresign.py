#coding=utf-8
from selenium import webdriver
url="http://www.csdn.net/?ref=toolbar"
driver=webdriver.Firefox
driver.get(url)
#driver.find_element_by_css_selector("a[href='https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn']").click()
