import  re


class repl:
    def replace(self, string):
        ab = re.sub("'", r'\\"', string)
        return ab

if __name__ == "__main__":
    str = r"{'reqId': '017650cbef0800778a7286c176467782', 'reqType': 1001, 'orderNo': 'BPA0212011013990', 'fininstId': '11', 'status': 'P'}"

    aa = repl()
    aa1 = aa.replace(str)
    print(aa1)

