import requests

session= requests.session()
post_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
post_data = {"username": "18560113515", "password": "xinlei123"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    # "Cookie":"_xsrf=zOCrmj0xcYbRXdGUYqbG166VJSEK8McT; _zap=71f4c360-126f-4edf-9d5c-d78185f1d2d1; __guid=74140564.4541751785386207700.1574496825786.9155; d_c0='ABCh12zoZRCPTvGEiIqsj_AOCF6YnqT2ZD4=|1574496831'; tgw_l7_route=1834ebf1acd448097141c3bb455d5563; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1574497031,1574498789,1574498796; monitor_count=12; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1574498812; capsion_ticket='2|1:0|10:1574499095|14:capsion_ticket|44:YzU4Y2YyNWY3ZjZmNDJhODkyNDU0M2ViNjFkYmZjOTg=|28ca67e97ed934498be06ac283e114dcdb317757a99ca7eb9e5dce4bd98aba2e'; z_c0='2|1:0|10:1574499100|4:z_c0|92:Mi4xd084TENnQUFBQUFBRUtIWGJPaGxFQ1lBQUFCZ0FsVk5IRUhHWGdBRnVPZWZyWGh4T25rRGNGRDFHYVIwV3ZIbmNB|cc71f7a9fb315103724a300a674069b02595fd49cf3d149f28abf988ebe9923c'"}
}
session.post(post_url,data=post_data,headers=headers)
response = session.get("http://https://www.zhihu.com/", headers=headers)
with open("zhihu1.html", "w", encoding="utf-8")as f:
    f.write(response.content.decode())
