# crawl() -> 데이터 받아오기
# parse() -> 받아온 데이터에서 필요한 정보 뽑기
# g o f(X) -> parse o crawl(url)
# crawl -> requests
# parse -> bs4
# ctrl + tab + tab

import requests
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

# crawl(url) -> data 받아오는 함수
url = "https://finance.naver.com/item/main.nhn?code=005930"
pageString = crawl(url)
print(pageString)

