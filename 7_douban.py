import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start=0&count=18&loc_id=108288"

        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        print(response)
        return response.content.decode()

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"]
        return content_list, total

    def save_content_list(self, content_list):
        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False ))
                f.write("\n")

    def run(self):

        # 1.准备一个起始URL
        num = 0
        total=100
        while num < total+20:
            url = self.url_temp.format(num)
            # 2. 发送请求，获取相应
            json_str = self.parse_url(url)
            # content_list,total = self.get_content_list(json_str)
            # # 3.提取数据
            # # 4.保存
            # self.save_content_list(content_list)
            # # 5.构造下一页URL,进如循环
            # # if len(content_list)<18:
            # #     break
            num += 20

        pass


if __name__ == '__main__':
    doubanSpider = DoubanSpider()
    doubanSpider.run()
