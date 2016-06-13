# encoding=utf-8
import unittest
import sys
sys.path.append('\test_case')
import test_case
from test_case import baidu,youdao,nineteenth
import HTMLTestRunner
import time
now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
testunit = unittest.TestSuite()
testunit.addTest(unittest.makeSuite(baidu.Baidu))
testunit.addTest(unittest.makeSuite(youdao.Youdao))
testunit.addTest(unittest.makeSuite(nineteenth.Login))
runner = unittest.TextTestRunner()
runner.run(testunit)
filename = "C:\\Users\\jing\\Documents\\" + now + "report.html"
fp = file(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度和有道云测试报告", description=u"用例执行情况")
runner.run(testunit)
