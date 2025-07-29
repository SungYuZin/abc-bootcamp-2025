
import requests

page_url = "https://www.melon.com/chart/age/list.htm"

params = {
    "idx": "1",
    "chartType": "YE",
    "chartGenre": "KPOP",
    "chartDate": "2019",
    "moved": "Y",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

res = requests.get(page_url, params=params, headers=headers)
print(res)  # 상태코드 출력

html: str = res.text
with open("melon_dump.html", "wt", encoding="utf8") as f:
    f.write(html)
    print("written to", f.name)
