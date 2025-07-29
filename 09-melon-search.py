import time
import requests
search_url = "멜론 노래 검색 주소 : https://www.melon.com/search/keyword/index.json"

#Query parameters
params = {
"jscallback":"_",
"query":"idol",
"_":int(time.time()),
}


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
res = requests.get(search_url, params=params)
print(res)
print(res.text)
