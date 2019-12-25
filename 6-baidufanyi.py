import requests
import json
import sys
import urllib

class BaiduFanyi:
    def __init__(self,trans_str):
        self.trans_str = trans_str
        self.lang_det_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self, trans_res):
        ret = trans_res["trans"][0]["dst"]
        print(ret)

    def run(self):
        lang_det_data = {"query": self.trans_str}
        lang = self.parse_url(self.lang_det_url, data=lang_det_data)["lan"]

        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else {"query": self.trans_str,
                                                                                               "from": "en", "to": "zh"}
        trans_res = self.parse_url(self.trans_url, data=trans_data)
        self.get_ret(self.trans_res)

if __name__ == '__main__':

    baidufanyi = BaiduFanyi("你好")
    baidufanyi.run()
