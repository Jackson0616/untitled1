import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36"}

post_url = "https://ideas.lego.com"
response = requests.get(post_url, headers=headers)
print(response)
