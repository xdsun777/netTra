import requests
import json
import os


# 翻译
class Tra:
    def __init__(self):
        self.url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        self.state = True

        try:
            r = requests.get('http://fanyi.youdao.com')
        except:
            print('网络错误')
            self.state = False

    def dic(self, tr):
        headers = {
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome80.0.3987.149 Safari/537.36",
            "Cookie": "_uab_collina=158557459111903368554625; JSESSIONID=72462467DF2AE695E96A9DF490D010FB; zh_choose=n; firstvisit_backurl=http%3A//www.wanfangdata.com.cn; Hm_lvt_838fbc4154ad87515435bf1e10023fab=1585574342,1585574541,1585619189; Hm_lpvt_838fbc4154ad87515435bf1e10023fab=1585619196; SEARCHHISTORY_0=UEsDBBQACAgIANFNf1AAAAAAAAAAAAAAAAABAAAAMOWUy0rDQBSG32UgXZW2qYnJFIpUrSiKLgzU%0ACy7GZEwiaRJyMVYpKIiWgmARFbWoCLaIFwQ3Cl4exibWt3BiFReiW4uu5j8z55w5fD8zk4vAQdMa%0AHkZ5DFK6q2lRoEogBRJMVjP7cjYDGRAFro2tAekjwcbIEhWhYJISmhxaGilQHMdMxeOe58U8pM8g%0AXZaQg2KikY%2BJerxV8r4MqbYTk4yuzz5ppGkRWzG8tyBiIhmPqgtEtVJyhiWlzYKjGDqV5SiepzI9%0AVJanIKQy3RHVFixVlrElIDlNhsXzpoVtWzV0Mlar6rl03tw9I2fO29AgqB76pfLT0rJ%2FUWvcrxPR%0AuNtrXl6G4mbTL50S8VyvBOWloHziV8qfYWkjOKiSMDha89dWQ3G91ayvhK2qV8H2rf%2B4Q3Szvvpy%0AXAk39x8atzVyse7m%2BwxXJwwZJhEFooWRgwU1pE6zPNtJQ5rnCOxi9DtH%2Bgu53gnOHORpvk0cmUVz%0A6Gf6YUZ7UKeTHM11fAXPcgzLJgnT78G744MjYwtSD%2FxN7snEv3kLoSWdMAF%2FsEQR4SyaMAWY5Nrk%0ALfxpR8LfCTIEdnHqFVBLBwi1vgpQtgEAADEGAAA%3D%0A"
        }
        data = {"i": tr,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "15856133842464",
                "sign": "dde2ff8f8bee63ecac9ead5a8e043dc4",
                "ts": "1585613384246",
                "bv": "70244e0061db49a9ee62d341c5fed82a",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTlM"
                }
        response = requests.post(self.url, data=data)
        pretext = response.text
        text = json.loads(pretext)
        arr = text["translateResult"][0]
        # print(text)
        # for i in range(len(arr)):
        #     print(arr[i]["tgt"])
        return arr


# if __name__ == '__main__':
#     a = Tra()
#     while True:
#         if a.state:
#             val = input(">")
#
#             if val == "":
#                 continue
#             elif val == "h":
#                 print("q:exit | cls:clean shell | h:help")
#             elif val == 'q':
#                 print("已退出")
#                 break
#             elif val == "cls":
#                 os.system('clear')
#             else:
#                 a.dic(val)
#         else:
#             break
