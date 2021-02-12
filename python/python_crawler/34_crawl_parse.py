import requests
from bs4 import BeautifulSoup

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p",{"class":"no_today"})
    blind = noToday.find("span",{"class":"blind"})
    price = blind.text
    # tag, class div, a, p, span <> -> 태그 <div>내용</div>
    # class <p class ="no_today> 내용 </p>
    return price


#url = "https://finance.naver.com/item/main.nhn?code=005930"
url = "https://finance.naver.com/item/main.nhn?code=035720"
pageString = crawl(url)
price = parse(pageString)
print("price:", price)