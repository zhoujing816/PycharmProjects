# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re

class Login(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.base_url = "http://www.19lou.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_logIn(self):
        u'''登录'''   
        browser=self.browser
        browser.get(self.base_url+"/")
        browser.find_element_by_css_selector("#J_headerLogin > a:nth-child(1)").click()
        browser.get(self.base_url+'/login')
        browser.find_element_by_css_selector("#userName").send_keys("benbendezhu")
        browser.find_element_by_css_selector("#userPass").send_keys("075818")
        browser.find_element_by_css_selector("#loginButton").click()
        browser.get(self.base_url+"/user/password")
        browser.find_element_by_css_selector("#J_headerFloor > dt:nth-child(1) > a:nth-child(1)").click()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()
        self.assertEqual([], self.verificationErrors)

if __name__== "__main__":
    unittest.main()
