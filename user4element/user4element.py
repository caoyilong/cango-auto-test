# coding=utf-8

import random as r
import string
import random
import datetime

# class user4element():
# def __init__(self,name,phone):
# self.name=name
# self.phone=phone


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)   # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
    val = '{0:x} {1:x}'.format(head, body)  # 格式化输出
    str = bytes.fromhex(val).decode('gb2312')
    # print(str)
    return str
# GBK2312()


def name(name_num):
    a1 = ['刘']  # ['锺','蔺','江','邗','郁'，'范']
    a2 = ['玉', '明', '龙', '芳', '军', '玲', '芝', '睿', '怜', '莉', '雨', '霜', '从', '鸿', '梦', '寒', '小', '云', '念', '怀', '鸿',
          '兰', '立', '玲', '娅', '国', '南', '雨', '炳', '念', '湛', '德', '双', '巍', '涵', '舒', '夏', '萱', '含', '英', '若', '振']
    # a3=['兰','立','玲','娅','国','南','雨','炳','念','湛','德','双','巍','涵','舒','夏','萱','含','英','若','振']

    for i in range(name_num):  # name_num生成循环次数
        a4 = GBK2312()
        a4 = list(a4)
        a5 = GBK2312()
        a5 = list(a5)
        a6 = (a2, a4)
        a6 = r.choice(a6)
        # name=r.choice(a1)+r.choice(a6)+r.choice(a5)
        name = r.choice(a1) + r.choice(a2) + r.choice(a2)
        # print(name)
        return name
# name(1)#传入循环次数


def company():
    a7 = GBK2312()
    a8 = GBK2312()
    a9 = '公司'
    return a7 + a8 + a9


def phone(phone_num):
    all_phone_nums = set()
    num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187', '188',
                 '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']
    for i in range(phone_num):
        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))  # random.sample随机不重复
        res = start + end  # +'\n'
        all_phone_nums.add(res)
        # print(res)#手机号
        # print(type(res))#查看类型为function
        phone = str(res)  # function转为字符串
        # print(phone)
        # print(type(phone))
        return phone  # return def
# phone(1)


def bankCardNo(bankCardNo_num):  # 银行卡号
    # num_start = ('456351',)  # 微众小程序能过
    num_start = ('620407', '621305', '621606')  # 工行cardbin
    # num_start = ('622260',)#中国银行能过微众验四，不能小程序还款
    # num_start = ('433670','621492')#中信,光大cardbin#微众面签还款卡授权成功
    # num_start = '621332'#中国银行cardbin
    # num_start = ('421349',)#建设银行cardbin
    # num_start = ('622260',)#壹账通乐山行白名单建行cardbin
    # num_start = ('621460',)#贵州行cardbin
    # num_start = ('621691',)#民生

    num_start = random.choice(num_start)

    # for i in range(12):
    for i in range(11):
        num_start = num_start + str(random.randint(0, 9))

    summation = 0
    for i in range(16):
        if i == 0:
            continue

        tmp1 = int(num_start[15 - i: 16 - i])

        if ((i + 1) % 2 == 0):
            if tmp1 < 5:
                summation = summation + tmp1 * 2
            else:
                tmp2 = str(tmp1 * 2)
                summation = summation + int(tmp2[0]) + int(tmp2[1])
        else:
            summation = summation + tmp1

#----------------生成校验码--------------------------
    check = str(10 - (summation % 10))
    if check == '10':
        check = '0'

    return num_start + check
# bankCardNo
# print(bankCardNo(1))


def vim(vim_num):  # 车架号

    for i in range(vim_num):
        # all_vim_nums=set()#写不写都可以
        start = ''.join(random.sample(string.digits, 7))
        end = ''.join(random.sample(string.digits, 7))
        vimres = start + 'BCD' + end
        # all_vim_nums.add(vimres)#写不写都可以
        # print(vimres)
        vim = str(vimres)
        return vim
# vim(1)


def getCheckBit(num17):
    """
    获取身份证最后一位，即校验码
    :param num17: 身份证前17位字符串
    :return: 身份证最后一位
    """
    Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    checkCode = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    zipWiNum17 = zip(list(num17), Wi)
    S = sum(int(i) * j for i, j in zipWiNum17)
    Y = S % 11
    return checkCode[Y]


def getAddrCode():
    """
    获取身份证前6位，即地址码
    :return: 身份证前6位
    """
    from addr import addr
    addrIndex = random.randint(0, len(addr) - 1)
    return addr[addrIndex]

    #addr = [(110000, u'北京市'),(140202, u'大同市城区'),(220702, u'宁江区'),(410200, u'开封市'),(620700, u'张掖市'),(451302, u'兴宾区'),(410421, u'宝丰县')]
    #addr = [(430481, u'耒阳市')]
    #addrIndex = random.randint(0,len(addr)-1)
    return addr[addrIndex]


def getBirthday(start="1975-01-01", end="1995-12-31"):
    """
    获取身份证7到14位，即出生年月日
    :param start: 出生日期合理的起始时间
    :param end: 出生日期合理的结束时间
    :return: 份证7到14位
    """
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") -
            datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthday = datetime.datetime.strptime(
        start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days))
    return datetime.datetime.strftime(birthday, "%Y%m%d")


def getRandomIdCard(sex=1):  # 1男，2女
    """
    获取随机身份证
    :param sex: 性别，默认为男
    :return: 返回一个随机身份证
    """
    idNumber, addrName = getAddrCode()
    idCode = str(idNumber) + getBirthday()
    for i in range(2):
        idCode += str(random.randint(0, 9))
    idCode += str(random.randrange(sex, 9, 2))  # 男sex,9,2
    idCode += getCheckBit(idCode)
    # return idCode
    # print(idCode)
    getRandomIdCard = str(idCode)
    return getRandomIdCard

# getRandomIdCard()


if __name__ == "__main__":
    #print('姓名                身份证                        手机号                       银 行卡号                        车架号 ')
    print('姓名\t\t身份证\t\t手机号\t\t银 行卡号\t\t\t车架号 ')
    for i in range(20):
        print(name(1) + '\t' + getRandomIdCard() + '\t' +
              phone(1) + '\t' + bankCardNo(1) + '\t' + vim(1))

    '''
    #另存为文件
    f = open('./user4element.txt','w') 
    f.write('姓名\t\t身份证\t\t手机号\t\t银 行卡号\t\t\t车架号 \n')
    for i in range (100):
        f.write(name(1)+'\t' +getRandomIdCard()+'\t'+phone(1)+'\t'+bankCardNo(1)+'\t'+vim(1)+'\n')
    

    f.close()
    f = open('./user4element.txt','r')
    print(f.read())
    f.close()#关闭文件
    '''
