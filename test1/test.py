#encoding:utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
url = "http://www.cnblogs.com/choosewang/articles/2865846.html"
driver.get(url)
print driver.title
driver.find_element_by_css_selector("a[href='http://www.cnblogs.com/choosewang/']").click()
#driver.find_element_by_css_selector("form> input.btn_my_zzk[value=谷歌搜索]").click()

