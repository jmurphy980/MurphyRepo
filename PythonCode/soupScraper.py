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

filename = "products.csv"
f = open(filename, "w")

headers = "brand, productName, shipping\n"

f.write(headers)


#getting to the right spot
for container in containers:
	
	brand = containers[0].find("div","item-info").img["title"]

	titleContainer = container.findAll("a", {"class":"item-title"})
	productName = titleContainer[0].text

	shippingContainer = container.findAll("li", {"class":"price-ship"})
	shipping = shippingContainer[0].text.strip()


	print("brand " + brand)
	print("productName " + productName)
	print("shipping " + shipping)

	f.write(brand + "," + productName.replace(",", "|") + "," + shipping + "\n")

f.close()


