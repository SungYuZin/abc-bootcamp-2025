import requests  # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

url = "" \
"" \
res = requests.get(url)
html = res.text
soup = BeautifulSoup(res.text, "html.parser")  
el_list = soup.select("#song-list li") 
for el in el_list:
    el.select