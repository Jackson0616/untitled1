import requests
from lxml import etree
import telnetlib
import numpy as np
import pandas as pd
import request

class Proxies_Poll:
    def __init__(self):
        self.url_temp = "https://www.xicidaili.com/nn/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def get_proxies(self):
        response_page = requests.get(self.url_temp, headers=self.headers)
        page_info = response_page.content.decode()

        html = etree.HTML(page_info)

        # 存储所有的URL列表
        all_url = html.xpath('//tr[@class="odd"]/td/text()')
        all_url2 = html.xpath('//table[@id="ip_list"]/tr/td/text()')

        # ip地址
        list_1 = html.xpath('//table[@id="ip_list"]/tr/td[2]/text()')
        # 端口号
        list_2 = html.xpath('//table[@id="ip_list"]/tr/td[3]/text()')

        # IP和端口汇总数据
        list_all = []
        for i in range(len(list_1)):
            #print(list_1[i] + ":" + list_2[i])
            list_all.append(list_1[i] + ":" + list_2[i])

        proxies=[]
        for i in range(len(list_all)):
            try:
                telnetlib.Telnet(list_1[i], port=list_2[i], timeout=20)
            except:
                print('{}:{}检测失败'.format(list_1[i], list_2[i]))
            else:
                print('{}:{}检测成功'.format(list_1[i], list_2[i]))
                proxies.append([list_1[i] + ":" + list_2[i]])
        print("检测完成")
        print(proxies)

        random_ip=np.random.choice(pd.DataFrame(proxies)[0].values)
        proxy={"http":random_ip}

        proxyHeader = request.ProxyHandler(proxy)
        # 创建Opener
        opener = request.build_opener(proxyHeader)
        # 安装Opener
        requests.install_opener(opener)
        # 然后剩下的就跟正常使用差不多，只不过此时的request已经是绑定了代理之后的request
        url = 'https://www.taobao.com/'
        req = request.Request(url)
        response = request.urlopen(req)
        print(response.read().decode())



if __name__=='__main__':
    proxies_poll=Proxies_Poll()
    proxies_poll.get_proxies()
