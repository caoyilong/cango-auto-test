# -*- coding: utf-8 -*-
import unittest
import time
from gRPC.page_obj import HTMLTestReportCN
from jzjgRPC.HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib


report_dir = './report/'
tc_dir = './testcase'
#discover=unittest.defaultTestLoader.discover(testcase_dir,pattern= 'test*.py')
# discover=unittest.defaultTestLoader.discover(testcase_dir,pattern='test001_PREAPPLY_sta.py')
discover = unittest.defaultTestLoader.discover(
    tc_dir, pattern='Test*.py')

#添加Suite
# def Suite():
#     #定义一个单元测试容器
#     suiteTest = unittest.TestSuite()
#     #将测试用例加入到容器
#     suiteTest.addTest(testCase("test_case_1"))
#     return suiteTest


if __name__ == '__main__':
    # unittest.main()

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = report_dir + now + 'result.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况')
    # runner.run(discover)
    # fp.close()
    fp = open(filename,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='统一网关测试报告',
        description='一期接口自动化',
        tester='罗哲'
        )
    runner.run(discover)
    fp.close()
    #file_path = new_report('./report/')


