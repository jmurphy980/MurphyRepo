import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl = 'https://www.newegg.com/p/pl?d=cpus'

#opening up connection, grabbing the page
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()

#html parsing
pageSoup = soup(pageHtml, "html.parser")

containers = pageSoup.findAll("div", {"class":"item-container"})

#getting to the right spot
for container in containers:
	
	brand = containers[0].find("div","item-info").img["title"]
	titleContainer = container.findAll("a", {"class":"item-title"})
	productName = titleContainer.text

	shippingContainer = container.findAll("li", {"class":"price-ship"})
	shipping = shippingContainer[0].text.strip()


	print("brand" + brand)
	print("productName" + productName)
	print("shipping" + shipping)
