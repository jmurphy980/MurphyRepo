import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


myUrl = ('https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch')
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()

print(pageHtml)