import requests
import json
#111

class RunMain():
    def __init__(self, no, method, header, url, body, depend, de_method, de_header, de_url, de_body, de_key,ass1, ass2):
            self.no = no
            self.method = method
            self.header = header
            self.url = url
            self.body = body
            self.depend = depend
            self.de_method = de_method
            self.de_header = de_header
            self.de_url = de_url
            self.de_body = de_body
            self.de_key = de_key
            self.ass1 = ass1
            self.ass2 = ass2

    def nodepend(self):#######################################################没有数据依赖时,直接发送请求
        if self.method == 'post':
            if self.header != None:
                res = requests.post(url=self.url, data=self.body, headers=self.header)
            if self.header == None:
                res = requests.post(url=self.url, data=self.body)
            else:
                print('de_method is null')
        else:
            if self.header != None:
                res = requests.get(url=self.url, data=self.body, headers=self.header,verify=False)
            if self.header == None:
                res = requests.get(url=self.url, data=self.body,verify=False)
            else:
                print('de_method is null')
        resp = json.loads(res)
        return resp


    def isdepend(self):
        if self.de_method == 'post':
            if self.de_header != None:
                res = requests.post(url=self.de_url, data=self.de_body, headers=self.de_header)
            if self.de_header == None:
                res = requests.post(url=self.de_url, data=self.de_body)
            else:
                print('de_method is null')
        else:
            if self.de_header != None:
                res = requests.get(url=self.de_url, data=self.de_body, headers=self.de_header,verify=False)
            if self.de_header == None:
                res = requests.get(url=self.de_url, data=self.de_body,verify=False)
            else:
                print('de_method is null')
        a=json.loads(res)
        token=dict[self.de_key]
    # return token
        self.header[self.de_key]=token##########################################################提取依赖数据 把token添加进dict 更新请求头
        self.nodepend()

    def main(self):
        if self.depend == None:
            self.nodepend()
        if self.depend != None:
            self.isdepend()


if __name__ == "__main__":
    lz = RunMain.main()
