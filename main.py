
import json
import requests
import base64

header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.\
        0.4472.164 Safari/537.36"
    }

def fofa_login (mail, key):
    url =  "https://fofa.so/api/v1/info/my?email={FOFA_EMAIL}&key={FOFA_KEY}".format(FOFA_EMAIL=mail, FOFA_KEY=key)
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.\
        0.4472.164 Safari/537.36"
    }
    respones = requests.get(url, header)
    if "errmsg" in respones.text:
        print("login_error!!!")
    else:
        print("login success!!!")
        fofa_search(mail, key)


def fofa_search(mail, key):
    Ip= []
    searcch = input("正确的fofa查询语句：")
    searcch = base64.b64encode(searcch.encode('utf-8')).decode('utf-8')
    url = "https://fofa.so/api/v1/search/all?email={FOFA_EMAIL}&key={FOFA_KEY}&qbase64={se}".format(FOFA_EMAIL=mail, FOFA_KEY=key, se=searcch)
    respones = requests.get(url, header)
    size = (json.loads(respones.text))['size']
    page = size / 100
    if page < 1:    # 判断获取页数
        i = 1
    elif page > 100:
        i = 100
    else:
        i = page
    for i in range(i):
        url = "https://fofa.so/api/v1/search/all?email={FOFA_EMAIL}&key={FOFA_KEY}&qbase64={se}".format(FOFA_EMAIL=mail, FOFA_KEY=key, se=searcch) +'&page=' + str(i+1)
        respones = requests.get(url, header)
        print("第"+str(i+1)+'页采集完成')
        Ip = Ip + json.loads(respones.text)["results"]
    list.sort(Ip,reverse = True)
    print(Ip)
    with open("access.txt","w") as f:
         for i in range(len(Ip)):
             f.write(Ip[i][0]+'\n')
    f.close()
    print("写入access.txt完成！！！！")
if __name__ == '__main__':
    mail = input("mail: ")
    fofa_key = input("key: ")
    fofa_login(mail, fofa_key)
