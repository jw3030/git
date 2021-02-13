import requests
from bs4 import BeautifulSoup

url ="https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&cat_id=&frm=NVSHATC"
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul",{"class":"list_basis"})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})
   # 반복문 1번째 상품, 2번째 상품 동시에 출력
    for li in lis:
        print(li)
    basicList_info_area__17Xyo = bsObj.find("div", {"class": "basicList_info_area__17Xyo"})
    aTag = basicList_info_area__17Xyo.find("a",{"class":"basicList_link__1MaTN"})
    title = aTag['title']
    link = aTag['href']
    price_num__2WUXn = li.find("span", {"class": "price_num__2WUXn"})
    price = price_num__2WUXn.text


    return [{}, {}, {}, {}]



pageString = crawl(url)
products = parse(pageString)
print(products)
