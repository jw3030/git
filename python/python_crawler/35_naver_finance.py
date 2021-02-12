# crawl, parse
import requests
from bs4 import BeautifulSoup
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    print(bsObj)
    noToday = bsObj.find("p",{"class":"no_today"})
    blind = noToday.find("span",{"class":"blind"})
    price = blind.text

    wrapCompany = bsObj.find("div",{"class":"wrap_company"})
    aTag = wrapCompany.find("a")
    name = aTag.text
    description = bsObj.find("div",{"class":"description"})
    code = description.find("span",{"class":"code"})
    img = description.find("img")
    category = img['alt']
    print(img['alt'])
    catEng = img['class']

    return {"price":price, "name":name,"code":code.text,"category":category,"catEng":catEng[0]}

# 001360 004140
def getCompanyInfo(code):
    url = "https://finance.naver.com/item/main.nhn?code={}".format(code)
    pageString = crawl(url)
    companyInfo = parse(pageString)
    return companyInfo

print(getCompanyInfo("004140"))
print(getCompanyInfo("001360"))

codes = ["001360", "004140"]
for code in codes:
    print(getCompanyInfo(code))