
#coding=utf-8

import time
from gRPC.page_obj.demo import demo
from gRPC.page_obj.replace import repl
import sys






class is_de():

    def is_depend(self,body, url, server, de_key, de_url, de_body, de_server, ass, interval = 5 ):
        res1 = demo().request(body=body, url=url, server=server)
        print(res1)
        dict_de_body = eval(de_body)
        dict_res1 = eval(res1)
        dict_de_body[de_key] = dict_res1[de_key]  ##拼接查询接口的新body
        new_de_body2 = str(dict_de_body)
        fi_body = '"'+ new_de_body2+ '"' ##  body  加""
        time.sleep(2)
        count = 0

        while count < 10:
            check_res = demo().request(body=fi_body, url=de_url, server=de_server)
            count += 1
            print(count)
            time.sleep(interval)
            if ass in check_res:
                print(ass, check_res, "成功：%sin%s" % (ass, check_res))
                return True
        else:
            print((ass, check_res, "失败原因：%s!in%s" % (ass, check_res)))
            raise AssertionError


if __name__ == "__main__":
    aa = is_de()
    aa1 = aa.is_depend(body="{'orderNo':'BPA0212011013990','fininstId':11,'coFininstId':11,'name':'张三一','paperType':1,'paperNo':'520101199009050018','paperValidityStartTime':1537513123000,'paperValidityEndTime':1695279523000,'bankAccount':'310109199003074432','bankMobile':'15900008911','sex':1,'customerFlg':1,'secondhandFlg':0,'dealerId':1234,'maritalStatus':1,'spouseOptional':'1'}",
                       url='10.42.2.18:30053',
                       server='org.cango.fininst.gw.api.FininstGwService.preApply',
                       de_key="reqId",
                       de_url='10.42.2.18:30053',
                       de_body="{'orderNo': 'BPA0212011013990','fininstId': 11}"     ,
                       de_server='org.cango.fininst.gw.api.FininstGwService.preApplyQuery'     ,
                       ass='11111'
                       )

