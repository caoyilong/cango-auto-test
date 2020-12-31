# -*- coding: utf-8 -*-
from xlrd import open_workbook
# path = getpathInfo.get_Path()


class readExcel():
    def get_xls(self, sheet_name='Sheet1'):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        # xlsPath = 'C:\\Users\cango\PycharmProjects\\untitled\gRPC\data\data.xls'
        xlsPath ="..\data\data.xls"
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):  # 根据行数做循环
            # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        cls.pop(0)
        return cls


if __name__ == '__main__':
    a = readExcel().get_xls()
    print(a)
    print(type(a))
    # a1 = a[0][3]
    # print(a1)
    # print(type(a1))
    # adic = eval(a1)
    # print(adic)
    # print(type(adic))

