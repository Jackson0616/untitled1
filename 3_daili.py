import requests

proxies={"http":"122.2.37.38:34817"}
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"}
response=requests.get("https://ideas.lego.com/",proxies=proxies,headers=headers)
print(response.status_code)