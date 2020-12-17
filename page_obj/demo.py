
# -*- coding: utf-8 -*-

import os
import unittest
import json
import ast
from gRPC.page_obj.replace import repl
import encodings
# class demo(unittest.TestCase):
class demo():
    def request(self, body, url, server):
        body2 = repl().replace(body)


        aa = 'cd C:\ &start grpcurl.exe &grpcurl -plaintext -d ' + \
            body2 + ' ' + \
            url + ' ' + server

        result = os.popen(aa)
        res = result.buffer.read().decode(encoding='utf8')
        result.close()
        # res = result.read()
        # sp_res = res.replace('\n', '').replace(' ', '')
        # res2 = eval(res)
        return res


        # str_res = str(NoneType)
        # return str_res
        # return  NoneType
        # ab = str(os.system(aa))
        # print(ab)
        # print(type(ab))
        # dic = eval(ab)
        # print(type(dic))


        # b = ass
        # try:
        #     #self.assertIn(ab, b)
        #     ab in b
        # except AssertionError:
        #     print((ab, b, "失败原因：%s!in%s" % (ab, b)))


if __name__ == "__main__":

    aa = demo()
    aa1 = aa.request(body="\"{'orderNo': 'BPA0212011013990', 'fininstId': 11, 'reqId': '0176658bded801f18a7286c176467782'}\""     ,
                       url='10.42.2.18:30053',
                       server='org.cango.fininst.gw.api.FininstGwService.preApplyQuery')

    # aa1 = aa.test_demo(body="{'orderNo': 'BPA0212011013990', 'fininstId': 11, 'reqId': '01765138e9f400bd8a7286c176467782'}" ,
    #                    url='10.42.2.18:30053',
    #                    server='org.cango.fininst.gw.api.FininstGwService.preApplyQuery')
    print(aa1)






