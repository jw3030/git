import requests
from bs4 import BeautifulSoup

url ="https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EC%85%94%EC%B8%A0&pagingIndex=5&pagingSize=80&productSet=total&query=%EC%85%94%EC%B8%A0&sort=rel&timestamp=&viewType=list"
def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

def getProductInfo(li):
    basicList_info_area__17Xyo = li.find("div", {"class": "basicList_info_area__17Xyo"})
    aTag = basicList_info_area__17Xyo.find("a", {"class": "basicList_link__1MaTN"})
    title = aTag['title']
    link = aTag['href']
    price_num__2WUXn = li.find("span", {"class": "price_num__2WUXn"})
    price = price_num__2WUXn.text
    price = price.replace(",","").replace(",","")
    return {"title":title,"price":price,"link":link}


def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    ul = bsObj.find("ul",{"class":"list_basis"})
    lis = ul.findAll("li",{"class":"basicList_item__2XT81"})
   # 반복문 1번째 상품, 2번째 상품 동시에 출력
    products = []
    for li in lis:
        try:
            productInfo = getProductInfo(li)
            products.append(productInfo)
        except Exception as e:
            print("--- error ---", e)
    return products





pageString = crawl(url)
products = parse(pageString)
print(products)
print(len(products))