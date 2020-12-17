# -*- coding: utf-8 -*-
import os


class preApply():

    def test_preApply(self, name):

        aa = 'cd C:\\Users\\cango\\PycharmProjects\\untitled\\1111\\grpcurl\\ &start grpcurl.exe &grpcurl -plaintext -d ' + \
            '"{"customerFlg":"1","dealerId":"13694","dfimId":"1901","fininstId":"15","indBankCardNo":"620407534263585884","indCustomerName":"%s","indMaritalStatus":"1","indMobile":"18980333285","indPaperNo":"512923196912141539","source":"2","secondhandFlg":"0","carEnergyType":""}"' % name + ' ' + \
            '10.42.1.70:31081' + ' ' + 'preApply'
        print(aa)



# os.system(aa)
if __name__ == "__main__":
    #name = user4element.name(1)
    name = '123'
    preApply().test_preApply(name)
