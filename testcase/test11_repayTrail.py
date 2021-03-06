# -*- coding: utf-8 -*-
import unittest
import sys
import random
sys.path.append("./page_obj")
sys.path.append("./user4element")
from page_obj.demo import demo

import paramunittest
from testcase.Excel import readExcel
from page_obj.is_de import is_de
import time
from page_obj import HTMLTestReportCN

login_xls = readExcel().get_xls(sheet_name='repayTrail')
@paramunittest.parametrized(*login_xls)
class test_repayTrail(unittest.TestCase):
    def setParameters(self, body, url, server, ass, is__de, de_key, de_body, de_url, de_server):
        self.body = body
        self.url = url
        self.server = server
        self.ass = ass
        self.is_de = is__de
        self.de_key = de_key
        self.de_url = de_url
        self.de_body = de_body
        self.de_server = de_server


    '''自动化框架'''
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        # testCase.abc = demo()  # 不同文件class之间关联
        # testCase.ab = preApply()

    def setUp(self):
        print('开始单个测试')

    def test_case_1(self):
        '''还款试算'''
        if self.is_de is 'N':
            res = demo().request(body=self.body, url=self.url, server=self.server)
            if self.ass in res:###############断言
               print((self.ass, res, "成功：%sin%s" % (self.ass, res)))
               return True
            else:
               print((self.ass, res, "失败原因：%s!in%s" % (self.ass, res)))
               raise AssertionError

        if self.is_de == 'Y':
            is_de().is_depend(body=self.body,
                                    url=self.url,
                                    server=self.server,
                                    de_key=self.de_key,
                                    de_url=self.de_url,
                                    de_body=self.de_body,
                                    de_server=self.server,
                                    ass=self.ass)

        else:
           print('Wrong')

    # def test_case_2(self):
    #     '''case2 preApply'''
    #     name = user4element.name(1)
    #     # print(name)
    #     self.ab.test_preApply(name)

    def tearDown(self):
        print('结束单个测试')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

if __name__ == '__main__':
    # suite = unittest.TestSuite()  # 定义一个测试集合
    # suite.addTest(unittest.makeSuite(testCase))  # 把写的用例加进来（将TestCalc类）加进来
    # now = time.strftime('%Y-%m-%d %H_%M_%S')
    # report_dir = './report/'
    # filename = report_dir + now + 'result.html'
    # f = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='用例', description='报告')
    # runner.run(suite)  # 运行用例（用例集合)
    # f.close()
    unittest.main(verbosity=2)