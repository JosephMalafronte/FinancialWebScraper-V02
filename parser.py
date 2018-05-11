#Joseph Malafronte
#Web Scraper 1
#Simple Web Scraper practice program
#Pulls graphics card information from Newegg.com


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser") 


filename = "products.csv"
f = open(filename, "w")

headers = "brand, productName, shipping\n"

f.write(headers)


#grabs each product places into array
containers = page_soup.findAll("div", {"class","item-container"})

for container in containers:
	brand = container.div.div.a.img["title"]
	title_container = container.findAll("a", {"class","item-title"})
	productName = title_container[0].text.strip()
	shippingPriceC = container.findAll("li", {"class","price-ship"})
	shippingPrice = shippingPriceC[0].text.strip()

	#Product Price
	infoContainer = container.findAll("div", {"class","item-info"})
	actionContainer = infoContainer[0].findAll("div", {"class", "item-action"})
	priceContainer = actionContainer[0].ul
	lastPriceContainer = priceContainer.findAll("li", {"class","price-current"})
	price = lastPriceContainer[0].strong.text.strip()


	print("Brand: " + brand)
	print("Product Name: " + productName)
	print("Shipping Price: " + shippingPrice)
	print("Product Price: $" + price)
	print("\n")


	f.write(brand + "," + productName.replace(",", "|") + "," + shippingPrice +"\n")


f.close()