import requests
from bs4 import BeautifulSoup

url ="https://search.shopping.naver.com/search/all?query=%EC%85%94%EC%B8%A0&cat_id=&frm=NVSHATC"
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    basicList_info_area__17Xyo  = bsObj.find("div",{"class":"basicList_info_area__17Xyo"}) #.find() 첫번째거
    aTag = basicList_info_area__17Xyo.find("a",{"class":"basicList_link__1MaTN"})
    title = aTag['title']
    link = aTag['href']
    price_num__2WUXn = bsObj.find("span", {"class": "price_num__2WUXn"}) #가격 뽑아보기
    print(price_num__2WUXn)
    price = price_num__2WUXn.text
    print(title, price, link)
    producntInfo = {"title":title, "price":price, "link":link}
    print(producntInfo)
    return [{}, {}, {}, {}]



pageString = crawl(url)
products = parse(pageString)
print(products)
