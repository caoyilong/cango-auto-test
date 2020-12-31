
# -*- coding: utf-8 -*-

import os
import unittest
import json
import ast
from page_obj.replace import repl
import encodings
import subprocess
# class demo(unittest.TestCase):
class demo():
    def request(self, body, url, server):
        body2 = repl().replace(body)


        cmd = 'cd .. &start grpcurl.exe &grpcurl -plaintext -d ' + "\""+ body2 +"\""+ ' ' +   url + ' ' + server
        print(cmd)

        # result = os.popen(cmd)
        # res = result.buffer.read().decode(encoding='utf8')
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,stderr=subprocess.STDOUT)
        res = result.stdout.read().decode("utf8")
        # res.close()
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
    aa1 = aa.request(body="{'orderNo': 'BPA0212011013990', 'fininstId': 11, 'reqId': '0176658bded801f18a7286c176467782'}"     ,
                       url='grpc-cango-fininst-gw.cango.local:8080',
                       server='org.cango.fininst.gw.api.FininstGwService.preApplyQuery')

    # bo = "{'orderNo':'BPA0212011013869','fininstId':11,'coFininstId':11,'name':'闫凯','paperType':1,'paperNo':'310109199306010137','paperValidityStartTime':1537513123000,'paperValidityEndTime':253402185600000,'bankAccount':'623185009100000154','bankMobile':'17787598603','sex':1,'customerFlg':1,'secondhandFlg':0,'dealerId':13694,'maritalStatus':2,'spouseName':'阿伊','spousePaperType':1,'spousePaperNo':'310106199112170010','spouseMobile':'13111112233','spouseSex':2,'spouseOptional':1,'files':[]}"
    # aa1 = aa.request(body= bo,
    #                    url='grpc-cango-fininst-gw.cango.local:8080',
    #                    server='org.cango.fininst.gw.api.FininstGwService.preApply')
    print(aa1)
    print(type(aa1))






